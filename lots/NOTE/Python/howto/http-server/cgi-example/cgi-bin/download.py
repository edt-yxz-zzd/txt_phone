

'''
for upload see:
    show_env.py
below code see:
    http://www.tutorialspoint.com/python/python_cgi_programming.htm

'''



# HTTP Header
print('Content-Disposition: attachment; filename = "YYY_FileName.xxx"')
    # forcing downloads

print('Content-Type:application/octet-stream')
    # any Content-Type
#print('Content-Length: ???')
    # optional
print() # NOTE!!!
    # require empty line as seperator

# Actual File Content will go here.
import sys
sys.stdout.buffer.write(b'\0\0abc\n')
#https://stackoverflow.com/questions/31917595/how-to-write-a-raw-hex-byte-to-stdout-in-python-3

