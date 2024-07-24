print("==================")
print(50*"=")
print("program percabangan")
print(50*"=")
print("Dibuat Oleh:")
print("Nama Anda")
print(50*"=")
print("Pilihan Perhitungan")
print("1.pembagian")
print("2.persegi")
print("3.persegi panjang")
print("4.segitiga")
print(50*"=")
hitung = float(input("masukan pilihan perhitungan(1/2/3/4)="))
if hitung==1:
     print("program pembagian")
     a=float(input("masukan nilai a:"))
     b=float(input("masukan nilai b:"))
     hasil=a/b
     print("hasil adalah:",hasil)
elif hitung==2:
     print("program persegi")
     s=float(input("masukan sisi:"))
     luas=s*s
     print("luas persegi adalah:",luas)
elif hitung==3:
     print("program persegi panjang")
     p=float(input("masukan luas panjang:"))
     l=float(input("masukan luas lebar:"))
     luas=p*l
     print("luas persegi panjang adalah::",luas)
elif hitung==4:
     print("program segitigas")
     a=float(input("masukan luas alas:"))
     t=float(input("masukan luas tinggi:"))
     luas=(a*t)/2
     print("luas segitiga adalah:",luas)