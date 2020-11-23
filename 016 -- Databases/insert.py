import sqlite3
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

artist = input ("New artist: ")

artists = conn.execute("INSERT INTO artist (name) VALUES ('%s')" % artist)

conn.commit()
conn.close()