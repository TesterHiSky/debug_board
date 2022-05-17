# import ctypes.util
#
#
# def load_library(*alternates):
#     for base_name in alternates:
#         lib_name = ctypes.util.find_library(base_name)
#         try:
#             if lib_name:
#                 return ctypes.CDLL(lib_name)
#             else:
#                 return ctypes.CDLL(base_name)
#         except OSError:
#             pass
#     raise OSError('Unable to load any of : {}'.format(alternates))
#
#
# load_library()
import ctypes
libc = ctypes.CDLL('msvcrt')
libc.atof.argtypes = [ctypes.c_char_p]
libc.atof.restype = ctypes.c_double

integer = ctypes.c_int()
decimal = ctypes.c_float()
libc.scanf(b'%i %f', ctypes.byref(integer), ctypes.byref(decimal))