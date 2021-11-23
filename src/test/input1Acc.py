# KAMUS
# a1, a2 : int
# operator : string (operator yang diterima adalah + (tambah), - (kurang), * (kali), / (bagi, dibulatkan ke bawah), dan % (sisa bagi))

# ALGORITMA
a1 = int(input("Masukkan angka pertama: "))                                                                                                             # Memasukkan angka pertama
a2 = int(input("Masukkan angka kedua: "))                                                                                                               # Memasukkan angka kedua
operator = str(input("Masukkan operator: "))                                                                                                            # Memasukkan salah satu pilihan operator (operator yang diterima adalah + (tambah), - (kurang), * (kali), / (bagi, dibulatkan ke bawah), dan % (sisa bagi))
if (operator == "+"):                                                                                                                                   # Cek kondisi apakah operator yang dipilih adalah +
    print(str(a1) + " " + str(operator) + " " + str(a2) + " = " + str(a1 + a2))                                                                         # Jika operator yang dipilih adalah +, maka angka pertama akan ditambah angka kedua
elif (operator == "-"):                                                                                                                                 # Cek kondisi apakah operator yang dipilih adalah -
    print(str(a1) + " " + str(operator) + " " + str(a2) + " = " + str(a1 - a2))                                                                         # Jika operator yang dipilih adalah -, maka angka pertama akan dikurang angka kedua
elif (operator == "*"):                                                                                                                                 # Cek kondisi apakah operator yang dipilih adalah *
    print(str(a1) + " " + str(operator) + " " + str(a2) + " = " + str(a1 * a2))                                                                         # Jika operator yang dipilih adalah *, maka angka pertama akan dikali angka kedua
elif (operator == "/"):                                                                                                                                 # Cek kondisi apakah operator yang dipilih adalah /
    print(str(a1) + " " + str(operator) + " " + str(a2) + " = " + str(a1 // a2))                                                                        # Jika operator yang dipilih adalah /, maka angka pertama akan dibagi angka kedua lalu dibulatkan ke bawah
elif (operator == "%"):                                                                                                                                 # Cek kondisi apakah operator yang dipilih adalah %
    print(str(a1) + " " + str(operator) + " " + str(a2) + " = " + str(a1 % a2))                                                                         # Jika operator yang dipilih adalah %, maka angka pertama akan dibagi angka kedua lalu diambil sisa baginya
else:                                                                                                                                                   # Cek kondisi apakah operator yang dipilih selain +, -, *, /, dan %   
    print("Input tidak valid, operator yang diterima adalah + (tambah), - (kurang), * (kali), / (bagi, dibulatkan ke bawah), dan % (sisa bagi)")        # Jika operator yang dipilih selain +, -, *, /, dan %, maka akan muncul kalimat yang memberitahu bahwa input tidak valid  