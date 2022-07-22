#Import Json
import json

#Import requests
import requests

#Input artist name and song title
artist_name = input("Enter the artist name: ")
song_title = input("Enter the song title: ")


#Define function to search for lyrics
def search_lyrics(artist_name, song_title):
    #Search for lyrics
    url = "https://api.lyrics.ovh/v1/" + artist_name + "/" + song_title
    response = requests.get(url)
    #If no lyrics found, print error message
    if response.status_code != 200:
        print("No lyrics found for " + song_title + " by " + artist_name)
    #If lyrics found, print lyrics
    else:
        print(response.json()["lyrics"])

#Call search_lyrics function
search_lyrics(artist_name, song_title)


#End Program
print("Lyrics Found!")
