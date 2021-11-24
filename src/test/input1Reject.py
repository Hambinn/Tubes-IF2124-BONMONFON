#test case: if, elif, else

# KAMUS
# a1, a2 : int
# operator : string (operator yang diterima adalah + (tambah), - (kurang), * (kali), / (bagi, dibulatkan ke bawah), dan % (sisa bagi))

# ALGORITMA
a1 = int(input("Masukkan angka pertama: "))                                     
a2 = int(input("Masukkan angka kedua: "))                                       
operator = str(input("Masukkan operator: "))                                    
if (operator == "+"):                                                           
    print(a1 + a2) 
elif (operator == "-"):                                                         
    print(a1 - a2)
elif (operator == "*"):                                                         
    print(a1 * a2)
elif (operator == "/"):                                                         
    print(a1 / a2)
else (operator == "%"):                                                         
    print(a1 % a2)
else:                                                                              
    print("Input tidak valid, operator yang diterima adalah + (tambah), - (kurang), * (kali), / (bagi), dan % (sisa bagi)")