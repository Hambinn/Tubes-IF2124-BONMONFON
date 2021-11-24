# Tubes-IF2124-BONMONFON
## Interpreter Python
Program akan menerima suatu teks file atau string yang merupakan kode dari sebuah program, lalu program akan memanfaatkan CFG untuk mengevaluasi kebenaran syntax dari kode yang dijadikan input tadi. Program juga menggunakan FA untuk mengecek tiap expression (contoh :, FA akan menolak ‘123dasda’ sebagai nama variabel, karena dalam python nama variabel tidak diperbolehkan didahului angka, contoh lain : ekspresi ‘55+’ salah karena penempatan operand + harus dijepit di antara 2 expression valid lain ).Program menggunakan Antarmuka berbasis CLI (Command Line Interface).    
## Pembagian Tugas
| NIM     | Pembagian Code | Pembagian Laporan |  
| :---:       |    :----:   |          :---: |  
| 13520074   | main.py, lexer.py, processInput.py, rulesDictionary.py       |Implementasi dan Pengujian|  
| 13520096   | cykParser.py, grammar.txt     | Hasil FA dan CFG, Implementasi dan Pengujian     |
| 13520102   | grammarConverter.py, converterUtility.py, rulesDictionary.py | Teori Dasar, Implementasi dan Pengujian |

# Cara Menjalankan Program  
1. Buka folder
2. Masuk ke file src
3. jalankan command `py main.py` pada terminal
4. lalu masukkan nama file
5. program akan mengeluarkan accepted bisa file benar, jika salah maka akan ditunjukkan error di bagian mana.









