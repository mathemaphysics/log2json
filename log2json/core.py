#!/usr/bin/env python
import argparse
import shutil
import sys
import os
import json
import cchardet
from typing import List, Optional, Tuple, Union
from log2json.status import ExitStatus
from log2json.cli.definition import parser


def main(args: List[Union[str, bytes]] = sys.argv) -> ExitStatus:
	"""
	main
	"""

	try:
		parsed_args = parser.parse_args(
			args=args
		)
	except KeyboardInterrupt:
		exit_status = ExitStatus.ERROR_CTRL_C
	except SystemExit:
		exit_status = ExitStatus.ERROR
	else:
		try:
			exit_status = program(
				args=parsed_args
			)
		except KeyboardInterrupt:
			exit_status = ExitStatus.ERROR_CTRL_C
		except SystemExit:
			exit_status = ExitStatus.ERROR
		except Exception:
			exit_status = ExitStatus.ERROR

	return exit_status


def program(args: argparse.Namespace) -> ExitStatus:
	exit_status = ExitStatus.SUCCESS

	# Remove console entry point
	args.logfile.pop(0)

	if (len(args.logfile) > 1 and args.o):
		parser.error(
			"If multiple log file(s) provided. You cannot use output file flag. Use directory flag instead.")
		exit_status = ExitStatus.ERROR

	if args.t == "text":
		if len(args.logfile) == 1:
			input_path = os.path.abspath(args.logfile[0])

			if (args.o):
				output_path = os.path.abspath(args.o)

				if (os.path.splitext(output_path)[1] != '.txt'):
					output_path += '.txt'

			else:
				output_path = os.path.abspath(
					os.path.join(
						os.getcwd(),
						os.path.splitext(args.logfile[0])[0] + '.txt'
					)
				)

			shutil.copyfile(input_path, output_path)
		else:
			if (args.d):
				output_dir = os.path.abspath(args.d)
			else:
				output_dir = os.path.abspath(
					os.path.join(
						os.getcwd(),
						'log2json_output'
					)
				)

				if (not os.path.isdir(output_dir)):
					os.mkdir(output_dir)

			for logfile in args.logfile:
				input_path = os.path.abspath(logfile)
				output_path = os.path.join(
					output_dir,
					os.path.splitext(os.path.basename(input_path))[0] + '.txt'
				)

				shutil.copyfile(input_path, output_path)
	elif args.t == "json":
		if (len(args.logfile) == 1):
			input_path = os.path.abspath(args.logfile[0])

			if (args.o):
				output_path = os.path.abspath(args.o)

				if (os.path.splitext(output_path)[1] != '.json'):
					output_path += '.json'

			else:
				output_path = os.path.abspath(
					os.path.join(
						os.getcwd(),
						os.path.splitext(args.logfile[0])[0] + '.json'
					)
				)

			write2json(input_path, output_path, args.e)
		else:
			if (args.d):
				output_dir = os.path.abspath(args.d)
			else:
				output_dir = os.path.abspath(
					os.path.join(
						os.getcwd(),
						'log2json_output'
					)
				)

				if (not os.path.isdir(output_dir)):
					os.mkdir(output_dir)

			for logfile in args.logfile:
				input_path = os.path.abspath(logfile)
				output_path = os.path.join(
					output_dir,
					os.path.splitext(os.path.basename(input_path))[0] + '.json'
				)

				write2json(input_path, output_path, args.e)

	return exit_status

def write2json(input_path: str, output_path: str, regex: str):
	if (regex):
		import re
		try:
			re.compile(regex)
		except re.error:
			parser.error("Provided regex is not valid.")

	o_fp = open(output_path, mode="w", encoding="utf-8")

	lines = []
	encoding = cchardet.detect(open(input_path, mode="rb").read())['encoding']
	with open(input_path, mode="r", encoding=encoding) as i_fp:
		for line in i_fp:
			if (regex):
				r = re.compile(regex)
				x = [m.groupdict() for m in r.finditer(line.strip())]
				lines.append(x[0])
			else:
				lines.append(line.strip())

	json.dump(lines, fp=o_fp, indent=2)

	o_fp.close()
