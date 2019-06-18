"""
file_open.py
"""
try:
 fd=open('test','r')
except FileNotFoundError as e:
    print(e)

fd.close()