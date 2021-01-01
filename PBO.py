import sqlite3

class Inkep:
    
    def BuatAkun(Username, Password, Nama_Pegawai):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'INSERT INTO [Data Akun] (Username, Password, [Nama Pegawai]) \
            VALUES (\'%s\', \'%s\', \'%s\')' 
        query = query % (Username, Password, Nama_Pegawai)
        cursor.execute(query)
        con.commit()
        con.close()
        print("Akun Telah Sukses Dibuat")
        Akun.masuk_akun()
    
    def Login(Username, Password):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT Username, Password FROM [Data Akun] \
        where Username=\'%s\' and Password=\'%s\' '
        query = query % (Username, Password)
        cursor.execute(query)
        con.commit()
        row = cursor.fetchall()
        if (len(row)) == 0:
            print("Maaf Login Gagal, Mohon cek username & password anda")
        elif Username == row[0][0] and Password == row[0][1]:
            print("Login Sukses")
            Akun.program(Username)      
        con.close()

    def Administrasi(Nama, Jenis_Kelamin, Usia, Alamat, Status_Kewarganegaraan, Tempat_tanggal_lahir, Agama, No_telepon):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'INSERT INTO [Data Pegawai "Inkep"] (Nama, [Jenis Kelamin], Usia, Alamat, [Status Kewarganegaraan], [Tempat tanggal lahir], Agama, [No telepon]) \
            VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
        query = query % (Nama, Jenis_Kelamin, Usia, Alamat, Status_Kewarganegaraan, Tempat_tanggal_lahir, Agama, No_telepon)
        cursor.execute(query)
        con.commit()
        con.close()
        print("Data pegawai berhasil diunggah")
        obat.kurangi(Jenis_Obat)

    def dataPegawai():
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT * FROM [Data Pegawai "Inkep"]'
        cursor.execute(query)
        hasil = cursor.fetchall()
        con.commit()
        for i in hasil:
            print('-------------------------------------------')
            print('No.Id pegawai :',i[0])
            print('Nama pegawai :',i[1])
            print('Jenis kelamin pegawai :',i[2])
            print('Usia pegawai :',i[3])
            print('Alamat pegawai :',i[4])
            print('Status Kewarganegaraan pegawai :',i[5])
            print('Tempat, tanggal lahir pegawai :',i[6])
            print('Agama pasien :',i[7])
            print('No.Telepon pasien :',i[8])
        con.close()
        Akun.program_pegawai()

class Akun:

    def masuk_akun():
        print('selamat datang di program Inkep')
        print("""silahkan pilih angka sesuai fitur di bawah
        1. Buat akun baru
        2. Login
        3. batal / keluar""")
        a=input('mohon input fitur sesuai angka :')
        if a=='1':
            print('Anda akan membuat akun baru, silahkan isi datadiri anda')
            Username = input('input username anda :')
            Password = input('input password anda :')
            Nama_Pegawai = input('input nama anda :')
            Inkep.BuatAkun(Username, Password, Nama_Pegawai)
        elif a=='2':
            print('silahkan login menggunakan username & password anda')
            Username = input('input username anda :')
            Password = input('input password anda :')
            Inkep.Login(Username,Password)
        elif a=='3':
            print('terimakasih telah memakai program ini :)')
        else:print('inputan anda salah, mohon mulai ulang program')

    def program(Username):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT [Nama Pegawai] FROM [Data Akun] where Username=\'%s\' ' 
        query = query % (Username)
        cursor.execute(query)
        con.commit()
        row = cursor.fetchall()
        print('selamat datang',row[0][0])
        con.close()
        Akun.program_pegawai()

    def program_pegawai():
        print("""silahkan pilih angka sesuai fitur di bawah
        1. Administrasi Pegawai
        2. Data Pegawai
        3. Menu Data Pegawai
        4. kembali ke menu akun
        5. keluar""")
        a=input('mohon input fitur sesuai angka :')
        if a=='1':
            print('Silahkan isi data data pasien dibawah ini')
            Nama = input('nama pasien :')
            Jenis_Kelamin = input('jenis kelamin :')
            Usia = input('usia :')
            Alamat = input('alamat :')
            Status_Kewarganegaraan = input('status kewarganegaraan :')
            Tempat_tanggal_lahir = input('tempat, tanggal lahir :')
            Agama = input('agama :')
            No_telepon = input('no.telepon :')
            Inkep.Administrasi(Nama, Jenis_Kelamin, Usia, Alamat, Status_Kewarganegaraan, Tempat_tanggal_lahir, Agama, No_telepon)
        elif a=="2":
            Inkep.dataPegawai()
        elif a=='3':
            Akun.manajer()
        elif a=='4':
            Akun.masuk_akun()
        elif a=='5':
            print('terimakasih telah memakai program ini :)')
        else:print('inputan anda salah, mohon mulai ulang program')

    def manajer():
        print("""silahkan pilih angka sesuai fitur di bawah
        1. Lihat data manajer
        2. Tambah data manajer
        3. Edit data manajer
        4. kembali ke menu pegawai
        5. keluar""")
        a=input('mohon input fitur sesuai angka :')
        if a=='1':
            print('Data Manajer')
            Manajer.lihat()
        elif a=='2':
            print('input nama & jumlah data manajer')
            Nama_Manajer = input('Nama Manajer :')
            Jumlah_dataManajer = input('data Manajer :')
            Manajer.tambah(Nama_Manajer, Jumlah_dataManajer)
        elif a=='3':
            print('input nama manajer yang mau diedit datanya')
            Nama_Manajer = input('Nama manajer :')
            Manajer.edit(Nama_Manajer)
        elif a=='4':
            Akun.program_pegawai()
        elif a=='5':
            print('terimakasih telah memakai program ini :)')
        else:print('inputan anda salah, mohon mulai ulang program')

class Manajer():

    def lihat():
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT * FROM [Data Manajer]'
        cursor.execute(query)
        hasil = cursor.fetchall()
        con.commit()
        for i in hasil:
            print('-------------------------------------------')
            print('No.Id  :',i[0])
            print('Nama  :',i[1])
            print('Usia  :',i[2])
            print('Jenis Kelamin :',i[3])
            print('Alamat :',i[4])
            print('Tempat Tanggal Lahir :',i[5])
            print('Agama :',i[6])
            print('Jumlah Pegawai :',i[7])
            print('Nomor telepon :',i[8])
            print('Jadwal :',i[9])
        Akun.manajer()

    def tambah(Nama_Manajer, Jumlah_dataManajer):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'INSERT INTO [Data Manajer] ([Nama Manajer], [Jumlah Data Manajer]) VALUES (\'%s\', \'%s\')' 
        query = query % (Nama_Manajer, Jumlah_dataManajer)
        cursor.execute(query)
        con.commit()
        con.close()
        print("Data manajer telah berhasil ditambah")
        Akun.manajer()
    
    def edit(Nama_Manajer):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT [Jumlah Data Manajer] FROM [Data Manajer] where [Nama Manajer]=\'%s\' '
        query = query % (Nama_Manajer)
        cursor.execute(query)
        con.commit()
        row = cursor.fetchall()
        data = input('input jumlah data manajer yang baru :')
        baru = data[0][0]
        baru = data
        query = 'UPDATE [Data Manajer] SET [Jumlah Data Manajer] = \'%s\' Where [Nama Manajer] = \'%s\' ' 
        query = query % (baru, Nama_Manajer)
        cursor.execute(query)
        con.commit()
        con.close()
        print("Data manajer telah berhasil ditambah")
        Akun.manajer()

    def kurangi(Nama_Manajer):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT [Nama Manajer],[Jumlah Data Manajer] FROM [Data Manajer] where [Nama Manajer]=\'%s\' '
        query = query % (Nama_Manajer)
        cursor.execute(query)
        con.commit()
        row = cursor.fetchall()
        if (len(row)) == 0:
            print("Maaf jenis manajer yang anda inputkan tidak ada dalam data")
            Akun.program_pegawai()
        elif Nama_Manajer == row[0][0]:
            baru = row[0][1] - 1
            query = 'UPDATE [Data Manajer] SET [Jumlah Data Manajer] = \'%s\' Where [Nama Manajer] = \'%s\' ' 
            query = query % (baru, Nama_Manajer)
            cursor.execute(query)
            con.commit()
            Manajer.notif(Nama_Manajer)
            con.close()

    def notif(Nama_Manajer):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT [Jumlah Data Manajer] FROM [Data Manajer] where [Nama Manajer]=\'%s\' '
        query = query % (Nama_Manajer)
        cursor.execute(query)
        con.commit()
        row = cursor.fetchall()
        if row[0][0] <= 5:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!!!!! stock obat menipis, harap melakukan stock ulang !!!!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        con.close()
        Akun.program_pegawai()
