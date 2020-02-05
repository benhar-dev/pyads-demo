import pyads
import os

# clear the screen
os.system('cls') 

# title 
print("PYADS Quick Demo")
print("-------------------")

# connection
plc = pyads.Connection('127.0.0.1.1.1', 851)
plc.open()

# read test
readResult = plc.read_by_name('global.bool_value', pyads.PLCTYPE_BOOL)
print('global.bool_value = ' + str(readResult))

# read and write true test
plc.write_by_name('global.bool_value', True, pyads.PLCTYPE_BOOL)
readResult = plc.read_by_name('global.bool_value', pyads.PLCTYPE_BOOL)
print('global.bool_value = ' + str(readResult))

plc.close()