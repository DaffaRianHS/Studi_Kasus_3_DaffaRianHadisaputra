batas_nilai = (65, 100)
nilai_masuk = []
list_lulus = []
list_remedi = []

while True:
    nilai = input("Masukkan Nilai (Ketik 'hapus' jika ingin menghapus nilai, 'selesai' jika selesai):")
    
    if nilai == "hapus":
        print(nilai_masuk)
        hapus = int(input("Pilih nilai yang mau dihapus (sesuai urutan indeks):"))
        dihapus = nilai_masuk.pop(hapus)
        print(f"Nilai {dihapus} telah dihapus")
    elif nilai == "selesai":
        break
    else:
        nilai_masuk.append(int(nilai))

for i in nilai_masuk:
    if i >= batas_nilai[0]:
        list_lulus.append(i)
    else:
        list_remedi.append(i)

print("Nilai yang masuk:", nilai_masuk)
print("Nilai yang lulus:", list_lulus)
print("Nilai yang remedi:", list_remedi)