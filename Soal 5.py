lanjut = "Y"
stok = 0
pendapatan_bersih = 0
while lanjut == "Y":
    tambah_stok = input("Apakah anda mau menambah stok semen sebanyak 100 bungkus ? (Y / N) : ")
    if tambah_stok == "Y":
        stok += 100
        pendapatan_bersih += (5000 * 70) + (25000 * 30)
    print("Stok Semen Anda saat ini = ", stok)
    print("Pendapatan Bersih Anda = ", pendapatan_bersih)
    lanjut = input("Apakah anda ingin menambah stok lagi ? (Y / N) :")

