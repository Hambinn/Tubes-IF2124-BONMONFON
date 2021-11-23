# test case: class, def, return, for, in

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

l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
      
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
      
# Iterating over a String
print("\nString Iteration")   
s = "Geeks"
for i in s :
    print(i)