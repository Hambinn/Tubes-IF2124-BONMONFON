# test case: class, def, return, for, in, pass

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

def add(x, y):
    sum = x + y
    return sum

# -----------------------------------------
s = "geeks"
  
# Empty loop
for i in s:
    # No error will be raised
    pass
  
# Empty function
def fun():
    pass
  
# No error will be raised
fun()
  
# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)