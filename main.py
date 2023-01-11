#Task_1
import sqlite3
conn=sqlite3.connect('my_db.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS my_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Aksana')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Yana')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Alina')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Marina')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Anna')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Irina')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Ekaterina')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Elena')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Svetlana')''')
cursor.execute('''INSERT INTO my_tab (name) VALUES ('Tatiana')''')
conn.commit()
cursor.execute('''SELECT id FROM my_tab''')
for i in list(cursor):
    for j in i:
        if type(j) is int:
            if j%2==0:
                cursor.execute('''DELETE FROM my_tab WHERE id=?''', i)
                conn.commit()
            else:
                cursor.execute('''UPDATE my_tab SET name='default' WHERE id=?''', i)
                conn.commit()
cursor.execute('''SELECT * FROM my_tab''')

#Task_2
cursor.execute('''CREATE TABLE IF NOT EXISTS text_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, col1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS nums_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, col1 INTEGER)''')
my_sp=[1,2,3,4,10,100,1000,'one','potato','carrot']
for i in my_sp:
    if type(i) is int:
        cursor.execute('''INSERT INTO nums_tab (col1) VALUES (?)''', (i,))
        conn.commit()
    if type(i) is str:
        cursor.execute('''INSERT INTO text_tab (col1) VALUES (?)''', (i,))
        conn.commit()
cursor.execute('''DELETE FROM nums_tab  WHERE col1>10''')
conn.commit()
cursor.execute('''UPDATE text_tab SET col1='Overone' WHERE LENGTH(col1)>4''')
conn.commit()
#Task_3
from random import randint
cursor.execute('''CREATE TABLE IF NOT EXISTS playlist(id INTEGER PRIMARY KEY AUTOINCREMENT,
                song TEXT, time INTEGER)''')
for i in range(10):
    cursor.execute('INSERT INTO playlist (song,time) VALUES (?,?)', ('song'+str(i+1),randint(10, 100)))
conn.commit()
cursor.execute('''SELECT * FROM playlist WHERE time>60''')
new_sp=list(cursor.fetchall())
my_file=open('my_playlist.txt','w')
for i in new_sp:
    my_file.write(str(i)+'\n')
my_file.close()
