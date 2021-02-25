#!/usr/bin/env python
import sys

def main():
	try:
		from .core import main
		exit_status = main()
	except KeyboardInterrupt:
		from log2json.status import ExistStatus
		exit_status = ExistStatus.ERROR_CTRL_C

	sys.exit(exit_status)

if __name__ == '__main__':
	main()
