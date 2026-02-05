def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error! Pembagian dengan nol tidak diperbolehkan."
    return x / y

print("--- Kalkulator Sederhana ---")
print("Pilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
    pilihan = input("\nMasukkan pilihan (1/2/3/4) atau 'exit' untuk keluar: ")

    if pilihan.lower() == 'exit':
        print("Terima kasih telah menggunakan kalkulator!")
        break

    if pilihan in ('1', '2', '3', '4'):
        try:
            num1 = int(input("Masukkan angka pertama: "))
            num2 = int(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input salah! Harap masukkan angka.")
            continue

        if pilihan == '1':
            print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid.")