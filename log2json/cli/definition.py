"""
CLI arguments definition.

"""
import argparse

parser = argparse.ArgumentParser(
	prog="log2json",
	description="Convert log file to plain text or json"
)

#######################################################################
# Input log file.
#######################################################################
parser.add_argument(
	"logfile",
	type=str,
	nargs="+",
	help="Input log file(s)"
)


#######################################################################
# Output file format.
#######################################################################
parser.add_argument(
	"-t",
	type=str,
	nargs="?",
	default="text",
	choices=["text", "json"],
	help="Output format (default: text)"
)


#######################################################################
# Output file.
#######################################################################
parser.add_argument(
	"-o",
	type=str,
	nargs="?",
	help="Output file path."
)

#######################################################################
# Destination directory.
#######################################################################
parser.add_argument(
	"-d",
	type=str,
	nargs="?",
	help="Output file directory for multiple log files"
)

#######################################################################
# RegEx for json type
#######################################################################
parser.add_argument(
	"-e",
	type=str,
	nargs="?",
	default="",
	help="RegEx for json type format"
)
