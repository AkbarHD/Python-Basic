# menyatukan string (concacenate)
from subprocess import list2cmdline
from urllib.parse import _NetlocResultMixinStr
from numpy import dtype

print(10*"=","Concatenate",10*"=")
nama_1 = "kucing"
nama_2 = "harimau"
nama_3 = "komodo"
nama_lengkap = nama_1 + " " + nama_2 + " " + nama_3
print("Maka : " +nama_lengkap )
# Menghitung jumlah string (Len)
print(10*"=","Len",10*"=")
data1 = len(nama_lengkap)
print("Maka Jumalah string nya ada : ",data1)
k = "k"
status = k in nama_lengkap
print("apakah huruf (K) ada di object Nama_lengkap ? ",status)
# Mencari indeks dalam sebuah object []
indeks = nama_lengkap[0:5]
print("maka indeksny adalah : ",indeks)
# Mencari item paling kecil (min) dan besar (max)
item = min(nama_lengkap)
item1 = max(nama_lengkap)
print("Maka item paling kecil adalah : "+str(item))
print("Maka item paling besar  adalah : "+str(item1))
# menghitung peringkat item di keyboard
ASCII_CODE = ord("o")
print("maka ascii code nya ada : "+str(ASCII_CODE))
# untuk mengetahui berapa item dalam 1 string (count)
count = nama_lengkap.count("o")
print("maka jumlah o pada 1 string ada :  "+str(count))
# Mengubah huruf menjadi huruf kapital, awal kapital dan huruf kecil
ubah_1 = nama_lengkap.upper()
ubah_2 = nama_lengkap.lower()
ubah_3 = nama_lengkap.title()
print("huruf kecil : " +ubah_2)
print("huruf besar : " +ubah_1)
print("awalan kata huruf besar : " +ubah_3)
# Contoh pengecekan lower case, upper case dan tittle case
lower_case = nama_lengkap.islower()
lower_case = nama_lengkap.isupper()
print(nama_lengkap,"apakah besar semua ? "+str(lower_case))
print(nama_lengkap,"apakah huruf kecil semua ? "+str(lower_case))
# Mengecek kata awal dan kata akhir startswith and endswith
cek_1 = nama_lengkap.startswith("kucing")
cek_2 = nama_lengkap.endswith("komodo")
print(nama_lengkap,"apakah kata akhiran komodo ? "+str(cek_2))
print(nama_lengkap,"apakah kata awalnya kucing ? "+str(cek_1))
# cara menggabungkan kata dalam sebuah list menggunakan join() and memisahkan split()
list = ["kamu","kaya ","monyet"]
list_2 =" ".join(list)
print("maka akan gabung : "+str(list_2))
list_3 = 'akuehmcintaehmkamu'
list_4 = (list_3.split("ehm"))
print(list_4)
#alokasi karakter rjust, ljust, center
rata_kanan = "data"
rata_kanan_1 = rata_kanan.rjust(20)
rata_kanan_2 = rata_kanan.ljust(20)
rata_kanan_3 = rata_kanan.center(20,"-")
print(" "+rata_kanan_2+" ")
print(" "+rata_kanan_3+" ")
print(' '+rata_kanan_1+" ")
print("=================== Program Selesai==================")





