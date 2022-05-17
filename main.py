import ctypes   # import the necessary modules
# Load DLL into memory

spi_master = ctypes.WinDLL("MCP2210DLL-UMx64.dll", winmode=0)
spi_master.DllInit(0x04D8,0x00DE)

# Test connexion
isConnected = spi_master.GetConnectionStatus() # return 0 if not connected !

if isConnected:
    print("The device is connected.\n")
else:
    print("The device is NOT connected.\n")


spi_master.argtypes = [ctypes.c_char_p, ctypes.c_int]
spi_master.restype = ctypes.c_int
spi_master.SetSpiMode = 1
integer = ctypes.c_int()
word = ctypes.c_char_p
data_2 = spi_master.GetSpiMode(integer)
print(data_2)

libc = ctypes.cdll.LoadLibrary("MCP2210DLL-UMx64.dll")
print(libc.GetConnectionStatus())
s = spi_master.GetSerialNumber
c_s = ctypes.c_wchar_p(str(s))
print(c_s)
print(c_s.value)

x = getattr(libc, 'GetSerialNumber')
print(x)

spi_master.DllCleanUp()

