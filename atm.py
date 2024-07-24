from click import option

def header ():
     print(50*"=")
     print("SELAMAT DATANG DI ATM")
     print(50*"=")
     print("Option:")
     print("1. Cek Uang")
     print("2. Tarik Uang")
     print("1. Tabung Uang")

def keyword ():
     print("keyword anda salah,mohon ulangi lagi")

def garis ():
     print(50*"=")  

header()
option=int(input("Silahkan pilih Option:"))
if option==1:
     print("Saldo berjumlah RP.1.000.000,00")
elif option==2:
     print("Saldo berjumlah RP.1.000.000,00 berapa nominal yang akan di tarik?")
     print("1. Rp.100.000,00")
     print("2. Rp.200.000,00")
     saldo_kamu=100000000
     option2=int(input("option :"))
     if option2==1:
          hasil1=saldo_kamu-10000000
          print("Saldo sekarang berjumlah :",hasil1)
     elif option2==2:
          hasil2=saldo_kamu-20000000
          print("Saldo sekarang berjumlah :",hasil2)
     else:
          keyword()
elif option==3:
     saldo_anda=100000000
     print("Saldo anda berjumlah Rp.1.000.000,00, Mau Nabung berapa?")
     option3=int(input("Masukan jumlah uang:"))
     hasil3=saldo_anda+option3
     print("Saldo anda sekarang",hasil3)
else:
          keyword()
garis()
print("TERIMAKASIH")
garis()