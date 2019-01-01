import sqlite3 as sq
#print(sq.version)
baglanti = sq.connect('veriler.db')
if baglanti:
    print("Başarılı")
else:
    print("Başarısız")
cur = baglanti.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS `USERS` (
	`USER_ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`USER_NAME`	TEXT NOT NULL,
	`USER_PASSWORD`	TEXT NOT NULL,
	`USER_AP`	INTEGER NOT NULL DEFAULT 1
);""")


cur.execute("""INSERT INTO USERS
(USER_NAME,USER_PASSWORD) VALUES ('{}','{}')""".
            format(input("Kullanıcı"),input("Şifre")))
baglanti.commit()
baglanti.close()
