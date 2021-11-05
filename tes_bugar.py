umur = int(input("Masukkan umur anda: "))
gender = input("Masukkan jenis kelamin anda (pria/wanita): ")
if umur >= 20 and umur <= 30:
    if gender == "pria" :
        tes1 = int(input("Hasil Tes 1: "))
        if tes1 >= 38 and tes1 <= 40 : skor1 = 3
        elif tes1 > 35 and tes1 <= 37 : skor1 = 2
        elif tes1 <= 35 : skor1 = 1
        tes2 = int(input("Hasil Tes 2: "))
        if tes2 >= 14 and tes2 <= 16 : skor2 = 3
        elif tes2 > 11 and tes2 <= 12 : skor2 = 2
        elif tes2 <= 11 : skor2 = 1
    elif gender == "wanita":
        tes1 = int(input("Hasil Tes 1: "))
        if tes1 >= 34 and tes1 <= 36 : skor1 = 3
        elif tes1 >= 32 and tes1 < 34 : skor1 = 2
        elif tes1 <= 31 : skor1 = 1
        tes2 = int(input("Hasil Tes 2: "))
        if tes2 > 10 and tes2 <= 14 : skor2 = 3
        elif tes2 >= 8 and tes2 <= 10 : skor2 = 2
        elif tes2 < 8 : skor2 = 1
elif umur >= 31 and umur <= 40:
    if gender == "pria" :
        tes1 = int(input("Hasil Tes 1: "))
        if tes1 > 35 and tes1 <= 37 : skor1 = 3
        elif tes1 > 32 and tes1 <= 35 : skor1 = 2
        elif tes1 >= 30 and tes1 <= 32 : skor1 = 1
        tes2 = int(input("Hasil Tes 2: "))
        if tes2 >= 28 and tes2 <= 30 : skor2 = 3
        elif tes2 >25 and tes2 <= 27 : skor2 = 2
        elif tes2 < 25 : skor2 = 1
    elif gender == "wanita":
        tes1 = int(input("Hasil Tes 1: "))
        if tes1 > 30 and tes1 <= 32 : skor1 = 3
        elif tes1 >= 28 and tes1 <= 30 : skor1 = 2
        elif tes1 < 28 : skor1 = 1
        tes2 = int(input("Hasil Tes 2: "))
        if tes2 > 22 and tes2 <= 24 : skor2 = 3
        elif tes2 >= 20 and tes2 <= 22 : skor2 = 2
        elif tes2 < 20 : skor2 = 1
hasil = (skor1 + skor2) / 2
print("Umur anda adalah ", umur ," tahun")
print("Jenis kelamin anda ", gender)
if hasil >= 2.5 : 
    print("Tingkat kebugaran anda: ", hasil , "(Sangat bugar)")
elif hasil >= 2 and hasil < 2.5 : 
    print("Tingkat kebugaran anda: ", hasil , "(Cukup bugar)")
elif hasil >= 1 and hasil < 2 : 
    print("Tingkat kebugaran anda: ", hasil , "(Kurang bugar)")