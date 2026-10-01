def konversi_suhu(suhu, satuan):
    if satuan == 'C':
        return (suhu * 9/5) + 32
    elif satuan == 'F':
        return (suhu - 32) * 5/9
    else:
        return "Satuan tidak valid"


value = int(input("Masukkan nilai suhu: "))
unit = input("Masukkan satuan suhu (C/F): ")

result = konversi_suhu(value, unit)

print(f"Hasil konversi: {result}")