# variabel global
saldo = 2000000
lanjut_beli = "y"
user = {"username":"admin","password":"12345" }
logged = "gagal"

# def
def beli_pulsa(p):
     global saldo
     if saldo >= int (p):
          saldo -= int(p)
          print("anda berhasil melakukan isi ulang pulsa sebesar Rp.",p)
          print("sisa saldo anda sebesar",saldo)
     else:
          print ("maaf,saldo anda tidak cukup")

# while
while logged == "gagal":
     print("Mau beli pulsa? Silahkan login")
     username = input("masukan username anda : ")
     password = input("masukkan password anda : ")
     if username == user['username'] and password == user['password']:
          print("selamat datang"+user['username'])
          logged = "berhasil"
     else:
          print ("username salah")

while lanjut_beli == "y" and logged == "berhasil":
     print ("beli pulsa")
     print ("1.beli pulsa Rp.5000")
     print ("2.beli pulsa Rp.10000")
     print ("3.beli pulsa Rp.15000")
     print ("4.beli pulsa Rp.20000")
     print ("5.beli pulsa Rp.25000")
     print ("6.keluar aplikasi")
     a = int(input("silahkan pilih nominal pulsa yang ingin di beli : "))
     if a == 1:
          beli_pulsa(5000)
     if a == 2:
          beli_pulsa(10000)
     if a == 3:
          beli_pulsa(15000)
     if a == 4:
          beli_pulsa(20000)
     if a == 5:
          beli_pulsa(25000)
     if a == 5:
          lanjut_beli = "n"
     else :     
          lanjut_beli = input("mau isi pulsa lagi?(y/n)")