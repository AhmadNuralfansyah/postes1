nama = input("Masukan nama : ")
nim = input("masukan nim : ")
pas = input("masukan password : ")


def kalkulator():
    
    print("\nKalkulator konversi")
    print("======================")
    berat_awal = float(input("masukan berat KG : "))
    print("konversi ke:")
    print("1. Pound (lb)")
    print("2. Ounce (ons)")
    print("3. Gram (g)")
    
    pilih = input("Masukkan pilihan : ")
    if pilih == "1":
        berat_lb = berat_awal * 2.20462
        print(f"{berat_awal} kilogram = {berat_lb} pound")
    elif pilih == "2":
        berat_ons = berat_awal * 35.274
        print(f"{berat_awal} kilogram = {berat_ons} ounce")
    elif pilih == "3":
        berat_g = berat_awal * 1000
        print(f"{berat_awal} kilogram = {berat_g} gram")
    else:
        print("Invalid")



if nama == "alfan" and nim == "123" and pas == "123":
    kalkulator()
else:
    print("Invalid")
    
    
