#!/usr/bin/env python
import argparse
import sys
from log2json.status import ExistStatus

def main(args: List[Union[str, bytes]] = sys.argv) -> ExitStatus:
	"""
	main
	"""

	exit_status = ExistStatus.SUCCESS
	return exit_status
