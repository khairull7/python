import string


# 4A
print("program Belanja")
kodebelanja=input("masukan kode belanja:")
if kodebelanja=="VC":
     print("Voucer")
elif kodebelanja=="C":
     print("Cash")

# 4B
print("program Penjualan ")
total=float(input("Masukan Total Belanja:"))
if total>=500000:
     print ("diskon 15%")
elif total>=250000:
     print("diskon 10%")
elif total>=150000:
     print("diskon 5%")
else:
     print("Cash")