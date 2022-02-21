from lib2to3.pgen2.token import RPAR


data_nama = "Akbar Hossam Delmiro"
data_umur = 18
data_tinggi = 168
data_nomor_sepatu = 42

# string standard
print(f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Ukuran sepatu = {data_nomor_sepatu}")


# String multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Akbar Hossam Delmiro"
data_tinggi = 168
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string) 

data1 = 15
data2 =f"maka angka ini akan menjadi bulat -> {data1}"
print(data2)
#cara memberi koma pada angka
uang = 3000000
print(f"jutaan = {uang:,}")
uang3 = 2004.3466
print(f"desimal = {uang3:.2f} ")
# menampilkan angka 0 di depan angka
print(f"desimal = {uang3:010.2f} ")
# cara menampilkan + dan -
angka4 = -20
angka5 = 20
print(f"minus (-) = {angka4:+d}")
print(f"plus (+) = {angka5:+d}")
# memformat persen
angka6 = 0.045
print(f"maka persen -> {angka6:.4%}")
# Melakukan operasi aritmatika dalam format string
angka7 = 100
angka8 = 50
operasi = f"perkalian {angka7} * {angka8} -> Rp.{angka7*angka8:,}"
print(operasi)
# Menampilkan Bilangan Binary, Octal, dan Hexadecimal
angka9 = 200
format_binary =f" Binary -> {bin(angka9)}"
format_octal =f" Octal -> {oct(angka9)}"
format_hex = f"Hexadecimal -> {hex(angka9)}"
print(format_binary)
print(format_octal)
print(format_hex)



