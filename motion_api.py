from ctypes import *


_library = CDLL('./motion.so')


off_t = c_long
size_t = c_uint
ssize_t = c_int
uint8_t = c_uint8


http_digest = _library.http_digest
http_digest.restype = c_int
http_digest.argtypes = [c_char_p]


#class option_t(Structure):
#	_fields_ = [
#		('opt', c_char),
#		('arg', c_char_p),
#		('desc', c_char_p),
#	]

#g_opt_config_file = (c_char_p).in_dll(_library, 'g_opt_config_file')


try:
	pass
	#_set_config_file_path = _library._set_config_file_path
	#_set_config_file_path.restype = c_int
	#_set_config_file_path.argtypes = [c_char_p]
except:
	pass
