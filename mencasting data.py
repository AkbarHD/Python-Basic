from lib2to3.pytree import type_repr
import string
from tkinter.tix import Tree

from numpy import integer

print("==================Data Integer========================")
data_integer = 8;
print("data : ",data_integer,"bertipe-",type(data_integer))
data_float = float(data_integer)
print("data : ",data_float,"bertipe-",type(data_float))
data_boolean = bool(data_integer)
print("data : ",data_boolean,"bertipe-",type(data_boolean))
data_string = str(data_integer)
print("data : ",data_string,"bertipe",type(data_string))
print("===================Data Float=========================")
data_float = 8.6;
print("data : ",data_float,"bertipe-",type(data_float))
data_integer = int(data_float)
print("data : ",data_integer,"bertipe-",type(data_integer))
data_string = str(data_float)
print("data : ",data_string,"bertipe-",type(data_string))
data_boolean = bool(data_float)
print("data : ",data_boolean,"bertipe-",type(data_boolean))
print("===================Data String========================")
data_boolean = True;
print("data : ",data_boolean,"bertipe-",type(data_boolean))
data_float = float(data_boolean)
print("data :",data_float,"bertipe-",type(data_float))
data_string = str(data_boolean)
print("data : ",data_string,"beetipe-",type(data_string))
data_integer = int(data_boolean)
print("data : ",data_integer,"bertipe-",type(data_integer))
print("========================Data String=====================")
data_string = 90;
print("data : ",data_string,"Bertipe-",type(data_string))
data_integer = int(data_string)
print("data : ",data_integer,"bertipe-",type(data_integer))
data_boolean = bool(data_string)
print("data : ",data_boolean,"bertipe",type(data_boolean))
data_float = float(data_string)
print("data : ",data_float,"bertipe",type(data_float))
print("=================FINISH===============================")

koma = 0
for i in range (2):
    koma +=4
    print(f"maka angka sekarang adalah ->{koma}")

suhu = 2
while suhu<10:
    print(f"maka angka sekarang adalah -> {suhu}")
    suhu +=1

    if suhu==8:
        print("nice")
        break
    print("whatsapp gaess")
print("selesaii!!!")












