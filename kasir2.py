
from itertools import product
# fungsi
def garis ():     
     print(73*"=")

def Listproduk ():
     print("============================== LIST PRODUK ============================== ")

def metode ():
     print("============================== METODE PEMBAYARAN ============================== ")

def konfirmasi ():
     konfirmasi = input("Apakah Sudah Yakin? Y/N : ")
     if konfirmasi == "y" or konfirmasi == "Y":
               print("Anda Sudah Berhasil Melakukan Pembayaran:)")
               garis()
     else:
               print("Id Metode Pembayaran Tidak Tersedia")
               garis()

# variabel
data_produk = {
     1:"Komputer",
     2:"Mouse  ",
     3:"Laptop Acer",
     4:"Mouse Pad",
     5:"Charger Laptop",

     }

data_harga={
     1: 5000000,
     2: 50000,
     3: 7000000,
     4: 18000,
     5: 90000,
     }

dict_trx = {}
Daftar_metode_pembayaran = {
     1:"Transfer Bank",
     2:"Virtual Account",
     3:"Kartu Kredit",
     }



Listproduk()
# perulangan
for i in data_produk:

     print("Id Produk : ",i,"\t Nama Produk : ",data_produk[i],"\t Harga Produk : ",data_harga[i])
garis()

pilih_id = int(input("Pilih Id Produk : "))
# pengkondisian
if pilih_id in data_produk :
     pilih_beli = input("Yakin Ingin Membeli? (Y/N) : ")
     if pilih_beli == "y" or pilih_beli =="Y":
          nama_penerima       = input("Nama Penerima   : ")
          alamat_penerima     = input("Alamat Penerima : ")
          NoHp                = input("No Hp           : ")
          dict_trx = {
               "nama_penerima"     : nama_penerima,
               "Alamat Penerima"   : alamat_penerima,
               "No Hp"             : NoHp,
               "Produk Id"         : data_produk,
          }
     else :
          pass
     if len (dict_trx) > 0 :
          metode()
     for i in Daftar_metode_pembayaran:
          print("Id : ",i,"\t Metode Pembayaran : ",Daftar_metode_pembayaran[i],)
     pilih_metode = int(input("Pilih Id Metode Pembayaran : "))
     if pilih_metode in Daftar_metode_pembayaran :
          garis()
          print ("Nama Penerima    : ", dict_trx["nama_penerima"])
          print ("Alamat Penerima  : ", dict_trx["Alamat Penerima"])
          print ("No Hp            : ", dict_trx["No Hp"])
          print ("Produk           : ",data_produk [pilih_id])
          print ("Harga            : ",data_harga [pilih_id])
          print("Metode Pembayaran :", Daftar_metode_pembayaran[pilih_metode])
          konfirmasi()