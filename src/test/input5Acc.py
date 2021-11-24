#test case: if, elif, else, and, or, is

x = 90
if x > 0 and x < 100:
    print("x lebih dari 0 dan kurang dari 100")
elif x < 0:
    print("x kurang dari 0")
elif x > 100:
    print("x lebih dari 100")

nilaiUTS = 70
nilaiUAS = 100
if nilaiUTS == 100 or nilaiUAS == 100:
    print("Kamu dapat indeks A karena nilai UTS atau nilai UASmu 100")
else:
    print("Kamu dapat indeks B, karena baik nilai UTS maupun UAS tidak ada yang dapat 100")

x = []
y = []
print(x is y)       # print false

w = []
v = w
print(w is v)       # print true