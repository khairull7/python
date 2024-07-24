import mysql.connector

koneksi = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="db_crudpython"
)

mycursor = koneksi.cursor()

lanjut = True
while lanjut:
    print("")
    print("")
    print("")
    print("CRUD User")
    print("1.LIHAT USER")
    print("2.TAMBAH USER")
    print("3.UBAH USER")
    print("4.HAPUS USER")
    print("5.KELUAR")
    print("")

    p = int(input("PILIH MENU :"))
    print("")
    print("")
    if p == 1:
        mycursor.execute("SELECT *FROM user")
        myresult = mycursor.fetchall()
        print("=====================")
        print("(id,nama,email,no hp)")
        for x in myresult:
            print(x)
    elif p == 2:
        nama = input("NAMA :")
        email = input("EMAIL :")
        no_hp = input("NO HP :")
        sql = "INSERT INTO user (nama, email, no_hp) VALUES (%s, %s,%s)"
        val = (nama, email, no_hp,)
        mycursor.execute(sql,val)
        koneksi.commit() 
        print(mycursor.rowcount, "data user berhasil di tambah")
    elif p == 3:
        id = input("ID USER :")
        mycursor.execute("SELECT * FROM user where id ="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            nama = input("NAMA ("+user[1]+") :") or user [1]
            email = input("EMAIL ("+user[2]+") :") or user [2]
            no_hp= input("NO HP ("+user[3]+") :") or user [3]
            sql = "UPDATE user SET nama=%s,email=%s,no_hp=%s WHERE id=%s"
            val = (nama, email, no_hp,id)
            mycursor.execute(sql, val)
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di simpan")
        else:
            print("data tidak ditemukan")
    elif p == 4:
        id = input("ID USER :")
        mycursor.execute("SELECT * FROM user where id =%s LIMIT 1",(id,))
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if user is not None:
            print("MENGHAPUS DATA :",user)
            sql = "DELETE FROM user WHERE id=%s"
            mycursor.execute(sql,(id,))
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di hapus")
        else:
            print("data tidak ditemukan")
    elif(p == 5):
        lanjut = False
