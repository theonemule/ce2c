import sqlite3
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

artist = input ("Delete artist: ")

artists = conn.execute("DELETE FROM artist WHERE name = '%s'" % artist)

conn.commit()
conn.close()