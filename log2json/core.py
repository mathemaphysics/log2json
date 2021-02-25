#!/usr/bin/env python
import argparse
import shutil
import sys
import os
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

			if (args.o[0]):
				output_path = os.path.abspath(args.o[0])

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
			if (args.d[0]):
				output_dir = os.path.abspath(args.d[0])
			else:
				output_dir = os.path.abspath(
					os.path.join(
						os.getcwd(),
						'log2json_output'
					)
				)

			for logfile in args.logfile:
				input_path = os.path.abspath(logfile)
				output_path = os.path.join(
					output_dir,
					os.path.splitext(os.path.basename(input_path))[0] + '.txt'
				)

				shutil.copyfile(input_path, output_path)
	elif args.t == "json":
		if (len(args.logfile) == 1):
			if (args.o[0]):
				output_path = os.path.abspath(args.o[0])

				if (os.path.splitext(output_path)[1] != '.json'):
					output_path += '.json'

			else:
				output_path = os.path.abspath(
					os.path.join(
						os.getcwd(),
						os.path.splitext(args.logfile[0])[0] + '.json'
					)
				)

				# Convert to json process here
		else:
			if (args.d[0]):
				output_dir = os.path.abspath(args.d[0])
			else:
				output_dir = os.path.abspath(
					os.path.join(
						os.getcwd(),
						'log2json_output'
					)
				)

			for logfile in args.logfile:
				input_path = os.path.abspath(logfile)
				output_path = os.path.join(
					output_dir,
					os.path.splitext(input_path)[0] + '.json'
				)

				# Convert to json process here

	return exit_status
