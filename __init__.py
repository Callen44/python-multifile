import os
def next(file_path, printout = False):
    global stringex
    stringex = '''global stream 
stream = os.popen('python3 ''' + file_path + ''' &')'''
    try:
        exec(stringex)
    except:
        output = 'failed to activate next file'
    if printout == True:
            output = stream.readlines()
    return(output)

def deamon(file_path, printout = False):
    stringex2 = '''stream2 = os.popen('python3 ''' + file_path + ''' &')'''
    try:
        exec(stringex2)
    except:
        output = 'failed to activate next file'
    if printout == True:
            output = stream2.readlines()
    return(output)