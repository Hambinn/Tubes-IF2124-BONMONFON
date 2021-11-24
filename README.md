# Tubes-IF2124-BONMONFON
## Interpreter Python
Program akan menerima suatu teks file atau string yang merupakan kode dari sebuah program, lalu program akan memanfaatkan CFG untuk mengevaluasi kebenaran syntax dari kode yang dijadikan input tadi. Program juga menggunakan FA untuk mengecek tiap expression (contoh :, FA akan menolak ‘123dasda’ sebagai nama variabel, karena dalam python nama variabel tidak diperbolehkan didahului angka, contoh lain : ekspresi ‘55+’ salah karena penempatan operand + harus dijepit di antara 2 expression valid lain ).Program menggunakan Antarmuka berbasis CLI (Command Line Interface).    
## Pembagian Tugas
Eiffel Aqila Amarendra - 13520074  (Code: `main.py`, `lexer.py`, `processInput.py`, `rulesDictionary.py`| Laporan: Implementasi dan Pengujian)  
Monica Adelia - 13520096  (Code :`cykParser.py`, `grammar.txt` | Laporan: Hasil FA dan CFG, Implementasi dan Pengujian)  
Ilham Bintang Nurmansyah - 13520102  (Code: `grammarConverter.py`, `converterUtility.py`, `rulesDictionary.py` | Laporan: Teori Dasar, Implementasi dan Pengujian)

# Cara Menjalankan Program  
1. Buka folder
2. Masuk ke file src
3. jalankan command `py main.py` pada terminal
4. lalu masukkan nama file
5. program akan mengeluarkan accepted bisa file benar, jika salah maka akan ditunjukkan error di bagian mana.









