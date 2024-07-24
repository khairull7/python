# awal def
def detail_bayar ():
     print("========== Detail Pembayaran ==========")
     print("menu yang di pesan          : ",beli)
     print("jumlah yang di pesan        : ",jumlah)
     print("total biaya                 : ",bayar)
     print("total yang harus di bayar   : ",total)
     print("============= Terimakasih =============")

def garis ():
     print(33*"=")
# akhir def

menu = {
     "nasi ayam bakar":33000,
     "nasi ayam kecap":25000,
     "nasi ayam geprek":20000,
     "nasi gurame bakar":20000,

}
print("========== Daftar Menu ==========")
for i in menu:
     print("Daftar Menu:", i,"\t Harga : ",menu[i])
print("pembelian di atas Rp.50.000,- mendapatkan potongan harga 15%")
garis()
beli = input("Pilih menu : ")
jumlah = int(input("Jumlah Pesanan : "))
bayar =  jumlah * menu[beli]

if bayar > 50000:
     diskon = bayar*15/100
     total = bayar - diskon
else:
     total = bayar
detail_bayar()