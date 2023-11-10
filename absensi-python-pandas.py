import pandas as pd
#================================================================================#
file_xlsx = "absen-ia23.xlsx"
file_csv = "absen-ia23.csv"
#================================================================================#
while True:
    try:
        df = pd.read_excel(file_xlsx)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nama", "NPM", "Kelas", "Keterangan"])
#================================================================================#
    print("Pilih opsi:")
    print("1. Baca file Excel")
    print("2. Input data ke file Excel")
    print("3. Baca file CSV")
    print("4. Tambahkan data ke file CSV")
    print("5. Cari mahasiswa berdasarkan NPM")
    print("6. Keluar")
    option = input("Masukkan pilihan (1/2/3/4/5/6): ")
#================================================================================#
    if option == "1":
        print("DataFrame setelah membaca file Excel:")
        print(df.to_string(index=False))
#================================================================================#
    elif option == "2":
        if df is None:
            df = pd.DataFrame(columns=["Nama", "NPM", "Kelas", "Keterangan"])
        nama = input("Masukkan Nama: ")
        while True:
            npm_input = input("Masukkan NPM (maksimal 8 digit): ")
            if npm_input.isdigit() and len(npm_input) == 8:
                npm = int(npm_input)
                if npm not in df["NPM"].values:
                    break
                else:
                    print("NPM sudah ada. Masukkan NPM yang unik.")
            else:
                print("Masukkan NPM yang valid (angka, maksimal 8 digit).")

        kelas = input("Masukkan Kelas: ")
        keterangan = input("Masukkan Keterangan (Contoh: S1-Informatika Pagi Depok): ")
        data_tambahan = pd.DataFrame({"Nama": [nama], "NPM": [npm], "Kelas": [kelas], "Keterangan": [keterangan]})
        df = pd.concat([df, data_tambahan], ignore_index=True)
        print("\nDataFrame setelah penambahan data:")
        print(df.to_string(index=False))
        df.to_excel(file_xlsx, index=False)
#================================================================================#
    elif option == "3":
        try:
            df_csv = pd.read_csv(file_csv)
            print("DataFrame setelah membaca file CSV:")
            print(df_csv.to_string(index=False))
        except FileNotFoundError:
            print("File CSV tidak ditemukan.")
#================================================================================#
    elif option == "4":
        nama = input("Masukkan Nama: ")
        while True:
            npm_input = input("Masukkan NPM (maksimal 8 digit): ")
            if npm_input.isdigit() and len(npm_input) == 8:
                npm = int(npm_input)
                if npm not in df_csv["NPM"].values:
                    break
                else:
                    print("NPM sudah ada. Masukkan NPM yang unik.")
            else:
                print("Masukkan NPM yang valid (angka, maksimal 8 digit).")

        kelas = input("Masukkan Kelas: ")
        keterangan = input("Masukkan Keterangan (Contoh: S1-Informatika Pagi Depok): ")
        data_tambahan = pd.DataFrame({"Nama": [nama], "NPM": [npm], "Kelas": [kelas], "Keterangan": [keterangan]})
        df_csv = pd.concat([df_csv, data_tambahan], ignore_index=True)
        df_csv.to_csv(file_csv, index=False)
        print("\nDataFrame setelah penambahan data ke file CSV:")
        print(df_csv)
#================================================================================#
    elif option == "5":
        while True:
            npm_cari_input = input("Masukkan NPM yang ingin dicari: ")
            if npm_cari_input.isdigit() and len(npm_cari_input) == 8:
                npm_cari = int(npm_cari_input)
                break
            else:
                print("Masukkan NPM yang valid (angka, maksimal 8 digit).")

        mahasiswa = df[df["NPM"] == npm_cari]
        if not mahasiswa.empty:
            print("Data mahasiswa dengan NPM", npm_cari)
            print(mahasiswa[["Nama", "NPM", "Kelas", "Keterangan"]])
        else:
            print("Mahasiswa dengan NPM", npm_cari, "tidak ditemukan.")
#================================================================================#
    elif option == "6":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, 5, atau 6.")
#================================================================================#
print("Program ditutup.")
