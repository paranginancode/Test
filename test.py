a = int(input('Masukkan Angka : '))
b = int(input('Masukkan Angka : '))

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, 'Genap')
    else:
        print(i, 'Ganjil')
