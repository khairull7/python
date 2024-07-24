def garis ():
     print(50*"=")

def perhitungan ():
     if hitung==1:
          print("program menghitung luas ")
          a=float(input("masukan nilai a:"))
          b=float(input("masukan nilai b:"))
          hasil=a+b
          print("hasil adalah:",hasil)
     elif hitung==2:
          print("program kurang")
          a=float(input("masukan nilai a:"))
          b=float(input("masukan nilai b:"))
          hasil=a-b
          print("hasil adalah:",hasil)   
     elif hitung==3:
          print("program perkalian")
          a=float(input("masukan nilai a:"))
          b=float(input("masukan nilai b:"))
          hasil=a*b
          print("hasil adalah:",hasil)
     elif hitung==4:
          print("program pembagian")
          a=float(input("masukan nilai a:"))
          b=float(input("masukan nilai b:"))
          hasil=a/b
          print("hasil adalah:",hasil)

garis()
print("program Kolkulator sederhana")
garis()
print("Pilihan Perhitungan")
print("1.tambah")
print("2.kurang")
print("3.kali")
print("4.bagi")
garis()
hitung = float(input("masukan pilihan perhitungan(1/2/3/4)="))
perhitungan()