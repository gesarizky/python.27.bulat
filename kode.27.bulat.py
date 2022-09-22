# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
puluh = float(input("Tuliskan Angka Puluhan: "))
ratus = float(input("Tuliskan Angka Ratusan: "))
ribu = float(input("Tuliskan Angka Ribuan: "))


# Mengkonversi
hasilp = round(puluh, -1)
hasilr = round(ratus, -2)
hasilrb = round(ribu, -3)

 
# Menampilkan Hasil 
print('Maka Pembulatan terdekat dari %d adalah %d' %(puluh,hasilp))
print('Maka Pembulatan terdekat dari %d adalah %d' %(ratus,hasilr))
print('Maka Pembulatan terdekat dari %d adalah %d' %(ribu,hasilrb))
