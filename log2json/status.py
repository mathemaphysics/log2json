from enum import IntEnum

class ExistStatus(IntEnum):
	"""Program exit status code constants."""
	# https://tldp.org/LDP/abs/html/exitcodes.html
	SUCCESS = 0
	ERROR = 1
	ERROR_CTRL_C = 130
