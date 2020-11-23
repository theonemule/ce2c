import sqlite3
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

artist = input ("New artist name: ")

artists = conn.execute("UPDATE artist SET name = '%s' WHERE artistid = 1" % artist)

conn.commit()
conn.close()