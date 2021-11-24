# test case: def, False, True, None, return, not, with, as, class

def indexOf(list, val):
    i = 0
    p = FIRST(l)
    found = False

    while(p != None and not found):
        if(val == INFO(p)):
            found = True
        else:
            i = i + 1
            p = NEXT(P)

    if(found):
        return i
    else:
        return 99999

#-----------------------------------------------------------
# a simple file writer object
  
class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name
  
    def __exit__(self):
        self.file.close()
  
# using with statement with MessageWriter
  
with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')