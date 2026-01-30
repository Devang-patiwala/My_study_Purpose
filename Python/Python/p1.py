import os
fname=input('Enter file name:')
if os.path.isfile(fname):
    print(fname)
