# KELOMPOK 5
# Program Mesin ATM

# ======================
# KAMUS (Daftar Variabel)
# ======================
# daftar_pin           : array of string       # menyimpan daftar PIN nasabah
# daftar_no_telpon     : array of string       # menyimpan daftar nomor telepon yang terdaftar
# daftar_otp           : array of string       # menyimpan kode OTP untuk tiap nasabah
# daftar_saldo         : array of integer      # menyimpan saldo masing-masing nasabah
# percobaan            : array of integer      # menyimpan jumlah percobaan salah memasukkan PIN
# kartu_terblokir      : array of boolean      # menandakan apakah kartu nasabah terblokir atau tidak

# login_berhasil       : boolean               # penanda apakah login berhasil dilakukan
# index_nasabah        : integer               # menyimpan indeks nasabah yang sedang login (0 atau 1)
# metode_kartu         : boolean               # penanda metode login: True = kartu, False = tanpa kartu
# menarik_tunai        : boolean               # penanda bahwa pengguna sedang melakukan tarik tunai
# menyetor_tunai       : boolean               # penanda bahwa pengguna sedang melakukan setor tunai

# metode               : string                # input pilihan metode login (1=kartu, 2=tanpa kartu, 3=keluar)
# pin                  : string                # input PIN nasabah pada login dengan kartu
# index_temp           : integer               # indeks sementara kartu saat validasi PIN
# sisa_percobaan       : integer               # jumlah kesempatan tersisa sebelum kartu terblokir
# no_telpon            : string                # input nomor telepon nasabah pada login tanpa kartu
# otp                  : string                # input kode OTP saat verifikasi login tanpa kartu

# pilihan_kartu        : string                # input pilihan menu utama saat login dengan kartu
# pilihan_tariktunai   : string                # input pilihan nominal saat tarik tunai
# pilihan_tarik        : array of string       # daftar nominal pilihan penarikan tunai
# nominal_tarik        : integer               # nominal uang yang ditarik oleh nasabah
# perlihatkan_saldo    : string                # pilihan untuk menampilkan saldo setelah transaksi

# lima_puluh           : integer               # jumlah lembar uang Rp50.000 yang disetor
# total_setor          : integer               # total nominal uang yang disetor nasabah
# konfirmasi           : string                # konfirmasi kebenaran nominal setoran (1=sudah, 2=belum)

# pin_baru             : string                # input PIN baru saat nasabah mengganti PIN
# konfirmasi_pin       : string                # konfirmasi ulang PIN baru agar sesuai dengan input pertama
# pilihan_nonkartu     : string                # input pilihan menu utama saat login tanpa kartu


# ======================
# ALGORITMA
# ======================

# Inisialisasi data nasabah
daftar_pin = ["5678", "1234"]
daftar_no_telpon = ["081234567891", "081987654321"]
daftar_otp = ["0000", "1111"]
daftar_saldo = [1000000000, 2000000000]
percobaan = [0, 0]
kartu_terblokir = [False, False]

# Inisialisasi variabel logika utama
login_berhasil = False
index_nasabah = -1
metode_kartu = False
menarik_tunai = False
menyetor_tunai = False

# Menampilkan menu awal pilihan metode login
print("Pilih metode:")
print("1. Login dengan kartu")
print("2. Login tanpa kartu")
print("3. Keluar")
metode = input("Masukkan metode pilihan: ")

# Jika pengguna memilih keluar
if metode == "3":
    print("Terima kasih telah menggunakan layanan kami.")
    exit()

# ============================================
# LOGIN DENGAN KARTU
# ============================================
elif metode == "1": 
    metode_kartu = True
    login_berhasil = False
    index_nasabah = -1

    # Loop login menggunakan PIN sampai benar atau terblokir
    while not login_berhasil and metode_kartu:
        pin = input("Masukkan PIN Anda: ")

        # Verifikasi PIN nasabah pertama
        if pin == daftar_pin[0] and not kartu_terblokir[0]:
            login_berhasil = True 
            index_nasabah = 0
            percobaan[0] = 0

        # Verifikasi PIN nasabah kedua
        elif pin == daftar_pin[1] and not kartu_terblokir[1]:
            login_berhasil = True 
            index_nasabah = 1
            percobaan[1] = 0

        # Jika PIN salah
        else:
            index_temp = 0 if not kartu_terblokir[0] else 1
            percobaan[index_temp] += 1
            sisa_percobaan = 3 - percobaan[index_temp]

            # Jika 3 kali salah, kartu diblokir
            if percobaan[index_temp] >= 3:
                print("Kartu Anda terblokir karena terlalu banyak percobaan salah.")
                kartu_terblokir[index_temp] = True
                metode_kartu = False
                index_nasabah = -1
            else:
                print(f"PIN salah. Percobaan tersisa {sisa_percobaan} kali.\n")

# ============================================
# LOGIN TANPA KARTU (MENGGUNAKAN NOMOR DAN OTP)
# ============================================
elif metode == "2":
    metode_kartu = False
    login_berhasil = False

    # Proses login tanpa kartu
    while not login_berhasil and not metode_kartu:
        no_telpon = input("Masukkan nomor telepon Anda: ")

        # Jika nomor terdaftar untuk akun 1
        if no_telpon == daftar_no_telpon[0]:
            print("OTP Anda adalah: ", daftar_otp[0])
            index_nasabah = 0

            # Loop verifikasi OTP hingga benar
            while not login_berhasil:
                otp = input("Masukkan OTP yang dikirim ke nomor telepon Anda: ")
                if otp == daftar_otp[0]:
                    login_berhasil = True
                else:
                    print("OTP salah. Silakan masukkan ulang OTP Anda.\n")

        # Jika nomor terdaftar untuk akun 2
        elif no_telpon == daftar_no_telpon[1]:
            print("OTP Anda adalah: ", daftar_otp[1])
            index_nasabah = 1
            while not login_berhasil:
                otp = input("Masukkan OTP yang dikirim ke nomor telepon Anda: ")
                if otp == daftar_otp[1]:
                    login_berhasil = True
                else:
                    print("OTP salah. Silakan masukkan ulang OTP Anda.\n")

        # Jika nomor tidak terdaftar
        else:
            print("Nomor telepon tidak terdaftar.\n")


# ============================================
# MENU UTAMA SETELAH LOGIN BERHASIL
# ============================================
while login_berhasil:
    menarik_tunai = False
    menyetor_tunai = False

    # ===============================
    # MENU LOGIN DENGAN KARTU
    # ===============================
    if metode_kartu == True:
        print("MENU UTAMA")
        print("1. Cek Saldo ")
        print("2. Tarik Tunai ")
        print("3. Setor Tunai ")
        print("4. Ubah PIN")
        print("Tekan 0 untuk keluar")

        pilihan_kartu = input("Masukkan pilihan Anda: ")

        # Keluar dari sistem
        if pilihan_kartu == "0":
            print("Silahkan ambil kartu Anda.")
            print("Terima kasih telah menggunakan layanan kami.")
            exit()

        # Menu cek saldo
        elif pilihan_kartu == "1":
            print(f"Saldo Anda saat ini: {daftar_saldo[index_nasabah]} rupiah\n")
            exit()

        # Menu tarik tunai
        elif pilihan_kartu == "2":
            menarik_tunai = True
            
            while menarik_tunai:
                print("Pilihan Nominal Tarik Tunai")
                pilihan_tarik = ["50000", "100000", "200000", "300000"]
                for i in range(4):
                    print(f"{i+1}. {pilihan_tarik[i]}")
                print("5. Tulis nominal sendiri (kelipatan 50000)")
                print("Ketik 0 untuk kembali ke menu utama")

                pilihan_tariktunai = input("Masukkan nominal yang ingin Anda tarik: ")

                # Jika kembali
                if pilihan_tariktunai == "0":
                    print("Terima kasih telah menggunakan layanan kami.\n")
                    exit()

                # Pilihan nominal tetap
                elif pilihan_tariktunai in ["1", "2", "3", "4"]:
                    nominal_tarik = int(pilihan_tarik[int(pilihan_tariktunai)-1])

                    # Cek saldo cukup
                    if nominal_tarik <= daftar_saldo[index_nasabah]:
                        daftar_saldo[index_nasabah] -= nominal_tarik
                        print("Transaksi berhasil.")
                        print("Apakah ingin memperlihatkan saldo sisa?")
                        print("1. Ya")
                        print("2. Tidak") 
                        perlihatkan_saldo = str(input("Pilihan Anda: "))

                        # Jika ingin lihat saldo
                        if perlihatkan_saldo == "1":
                            print(f"Saldo Anda sekarang: {daftar_saldo[index_nasabah]} rupiah\n")
                            exit()
                        else: 
                            print("Silahkan ambil uang dan kartu Anda.\n")
                            print("Terima kasih telah menggunakan layanan kami.\n")
                            menarik_tunai = False
                            exit()
                    else:
                        print("Saldo tidak mencukupi untuk melakukan penarikan.\n")

                # Input nominal sendiri
                elif pilihan_tariktunai == "5":
                    nominal_tarik = int(input("Masukkan nominal tarik tunai (kelipatan 50000): "))

                    # Validasi nominal
                    if nominal_tarik % 50000 == 0 and nominal_tarik <= 1000000:
                        if nominal_tarik <= daftar_saldo[index_nasabah]:
                            daftar_saldo[index_nasabah] -= nominal_tarik
                            print(f"Transaksi berhasil.")
                            print("Apakah ingin memperlihatkan saldo sisa?")
                            print("1. Ya")
                            print("2. Tidak") 
                            perlihatkan_saldo = str(input("Pilihan Anda: "))

                            if perlihatkan_saldo == "1":
                                print(f"Saldo Anda sekarang: {daftar_saldo[index_nasabah]} rupiah\n")
                                exit()
                            else: 
                                print("Silahkan ambil uang dan kartu Anda.\n")
                                print("Terima kasih telah menggunakan layanan kami.\n")
                                menarik_tunai = False
                                exit()

                        else:
                            print("Saldo tidak mencukupi.\n")
                    elif nominal_tarik > 1000000:
                        print("Nominal melebihi limit (Rp1.000.000).")
                    else:
                        print("Nominal harus kelipatan Rp50.000.\n")

        # Menu setor tunai
        elif pilihan_kartu == "3":
            menyetor_tunai = True

            while menyetor_tunai:
                print("Silakan masukkan uang ke mesin...")
                input("(Tekan Enter setelah uang dimasukkan)")
                print("\nMesin sedang menghitung uang Anda...")
        
                lima_puluh = int(input("Jumlah lembar Rp50.000 terdeteksi: "))
                total_setor = (lima_puluh * 50000)

                # Jika tidak ada uang
                if total_setor == 0:
                    print("\nTidak ada uang yang terdeteksi. Transaksi dibatalkan.\n")
                    menyetor_tunai = False
                else:
                    print(f"\nTotal uang terdeteksi: Rp{total_setor}")
                    print("Apakah nominal setoran sudah benar?")
                    print("1. Sudah")
                    print("2. Belum")
                    konfirmasi = input("")

                    if konfirmasi == "1":
                        print("\nMemproses setoran Anda...")
                        daftar_saldo[index_nasabah] += total_setor
                        print(f"Setoran sebesar Rp{total_setor} berhasil!")
                        print(f"Saldo Anda sekarang: Rp{daftar_saldo[index_nasabah]}\n")
                        exit()
                    else:
                        print("\nSetoran dibatalkan. Uang dikembalikan.\n")

        # Menu ubah PIN
        elif pilihan_kartu == "4":
            pin_baru = input("Masukkan PIN baru (4 digit): ")
            if len(pin_baru) != 4:
                print("PIN harus 4 digit.")
            else: 
                konfirmasi_pin = input("Konfirmasi PIN baru: ")
                if konfirmasi_pin == pin_baru and pin_baru != daftar_pin[index_nasabah]:
                    daftar_pin[index_nasabah] = pin_baru
                    print("PIN berhasil diubah.\n")
                    exit()
                else:
                    print("Konfirmasi PIN tidak sesuai atau PIN baru sama dengan PIN lama.\n")

    # ===============================
    # MENU LOGIN TANPA KARTU
    # ===============================
    else:
        print("MENU UTAMA (Non-Kartu)")
        print("1. Tarik Tunai")
        print("2. Setor Tunai")
        print("Tekan 0 untuk keluar")

        pilihan_nonkartu = input("Masukkan pilihan Anda: ")

        # Jika keluar
        if pilihan_nonkartu == "0":
            print("Terima kasih telah menggunakan layanan kami.")
            exit()

        # Tarik tunai tanpa kartu
        elif pilihan_nonkartu == "1":
            menarik_tunai = True

            while menarik_tunai:
                print("Pilihan Nominal Tarik Tunai")
                pilihan_tarik = ["50000", "100000", "200000", "300000"]
                for i in range(4):
                    print(f"{i+1}. {pilihan_tarik[i]}")
                print("5. Tulis nominal sendiri (kelipatan 50000)")
                print("Ketik 0 untuk kembali ke menu utama")

                pilihan_tariktunai = input("Masukkan nominal yang ingin Anda tarik: ")

                # Kembali ke menu
                if pilihan_tariktunai == "0":
                    print("Terima kasih telah menggunakan layanan kami.\n")
                    exit()

                # Pilihan tetap
                elif pilihan_tariktunai in ["1", "2", "3", "4"]:
                    nominal_tarik = int(pilihan_tarik[int(pilihan_tariktunai)-1])
                    if nominal_tarik <= daftar_saldo[index_nasabah]:
                        daftar_saldo[index_nasabah] -= nominal_tarik
                        print(f"Transaksi berhasil. Saldo Anda sekarang: {daftar_saldo[index_nasabah]} rupiah\n")
                        print("Silahkan ambil uang Anda.\n")
                        menarik_tunai = False
                        exit()
                    else:
                        print("Saldo tidak mencukupi.\n")

                # Input nominal sendiri
                elif pilihan_tariktunai == "5":
                    nominal_tarik = int(input("Masukkan nominal tarik tunai (kelipatan 50000): "))
                    if nominal_tarik % 50000 == 0 and nominal_tarik <= 1000000:
                        if nominal_tarik <= daftar_saldo[index_nasabah]:
                            daftar_saldo[index_nasabah] -= nominal_tarik
                            print(f"Transaksi berhasil. Saldo Anda sekarang: {daftar_saldo[index_nasabah]} rupiah\n")
                            print("Silahkan ambil uang Anda.\n")
                            exit()
                        else:
                            print("Saldo tidak mencukupi.\n")
                    elif nominal_tarik > 1000000:
                        print("Nominal melebihi limit (Rp1.000.000).")
                    else:
                        print("Nominal harus kelipatan Rp50.000.\n")

        # Setor tunai tanpa kartu
        elif pilihan_nonkartu == "2":
            menyetor_tunai = True

            while menyetor_tunai:
                print("Silakan masukkan uang ke mesin...")
                input("(Tekan Enter setelah uang dimasukkan)")
                print("\nMesin sedang menghitung uang Anda...")

                # Input jumlah lembar uang
                lima_puluh = int(input("Jumlah lembar Rp50.000 terdeteksi: "))

                # Hitung total setoran
                total_setor = (lima_puluh * 50000)

                # Validasi setoran
                if total_setor == 0:
                    print("\nTidak ada uang yang terdeteksi. Transaksi dibatalkan.\n")
                    exit()
                else:
                    print(f"\nTotal uang terdeteksi: Rp{total_setor}")
                    print("Apakah Nominal Setoran Sudah Benar?")
                    print("1. Sudah")
                    print("2. Belum")
                    konfirmasi = input("")

                    # Jika benar, proses setoran
                    if konfirmasi == "1":
                        print("\nMemproses setoran Anda...")
                        daftar_saldo[index_nasabah] += total_setor
                        print(f"Setoran sebesar Rp{total_setor} berhasil diproses!")
                        print(f"Saldo Anda sekarang: Rp{daftar_saldo[index_nasabah]}\n")
                        exit()
                    else:
                        print("\nSetoran dibatalkan. Uang dikembalikan.\n")
