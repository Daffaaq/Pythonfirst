import os

print("+-----------------------------------------------+")
print("|    Selamat Datang di Aplikasi Sistem Pakar\t|")
print("|\t    pengujian Kualitas Garam\t        |")
print("+-----------------------------------------------+")
n = input("Next ")

os.system('cls')

while n == "y":
    print("\nPilih Kriteria Garam")
    print("G01. Warna Putih Bening Kering")
    print("G02. Warna Putih Bening Basah")
    print("G03. Warna Putih Kapur kering")
    print("G04. Warna Putih Kapur Basah")
    warna = input("Pilih : ")
    print()
    print("G05. Rasa Asin Garam")
    print("G06. Rasa Asin Ringan")
    print("G07. Rasa Asin Pahit")
    print("G08. Rasa Pahit")
    rasa = input("Pilih : ")
    
    if warna.isupper() and rasa.isupper():
        if warna == "G01" and rasa == "G05": #1
            print("\nKualitas Bagus")
        if warna == "G01" and rasa ==  "G06": #2
            print("\nKualitas Kurang Baik")
        if warna == "G01" and rasa ==  "G07": #3
            print("\nKualitas Kurang Baik")
        if warna == "G01" and rasa ==  "G08": #4
            print("\nKualitas Kurang Baik")
        if warna == "G02" and rasa ==  "G05": #5
            print("\nKualitas Kurang Baik")
        if warna == "G02" and rasa ==  "G06": #6
            print("\nKualitas buruk")
        if warna == "G02" and rasa ==  "G07": #7
            print("\nKualitas buruk")
        if warna == "G02" and rasa ==  "G08": #8
            print("\nKualitas buruk")
        if warna == "G03" and rasa ==  "G05": #9
            print("\nKualitas Kurang Baik")
        if warna == "G03" and rasa ==  "G06": #10
            print("\nKualitas buruk")
        if warna == "G03" and rasa ==  "G07": #11
            print("\nKualitas buruk")
        if warna == "G03" and rasa ==  "G08": #12
            print("\nKualitas buruk")
        if warna == "G04" and rasa ==  "G05": #13
            print("\nKualitas Kurang Baik")
        if warna == "G04" and rasa ==  "G06": #14
            print("\nKualitas buruk")
        if warna == "G04" and rasa ==  "G07": #15
            print("\nKualitas buruk")
        if warna == "G04" and rasa == "G08": #16
            print("\nKualitas buruk")
    
    else:
        print("Mohon Maaf anda seharusnya menggunakan huruf Kapital")

    n = input("\nMenu ")
    if n == "y":
        print()
    elif n =="n":
        exit()
        print("Terimakasih")
    else:
        print("Salah Memasukkan")