#Adds a reference to my SQL library
import sqlite3

#Gets a connection to the database
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

artist = input ("Search for artist: ")

#Get records using SELECT
artists = conn.execute("SELECT * FROM artist WHERE name = '%s'" % artist)

#Displays each record
for row in artists:
    print(row)
