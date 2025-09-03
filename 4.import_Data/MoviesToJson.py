import csv
import re
 
csvfile = open('ml-latest-small/movies.csv', 'r')
 
reader = csv.DictReader( csvfile )
for movie in reader:
        print ("{ \"create\" : { \"_index\": \"movies\", \"_id\" : \"" , movie['movieId'], "\" } }", sep='')
        title = re.sub(r" \(.*\)$", "", re.sub('"','', movie['title']))
        year = movie['title'][-5:-1]
        if (not year.isdigit()):
            year = "2016"
        genres = movie['genres'].split('|')
        print ("{ \"id\": \"", movie['movieId'], "\", \"title\": \"", title, "\", \"year\":", year, ", \"genre\":[", end='', sep='')
        for genre in genres[:-1]:
            print("\"", genre, "\",", end='', sep='')
        print("\"", genres[-1], "\"", end = '', sep='')
        print ("] }")


movieId,title,genres
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy

{ "id": "1", "title": "Toy Story", "year":1995, "genre": [