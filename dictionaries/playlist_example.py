# make a spotifyesque playlist using nested dicts and lists

#my approach: playlist will be a dict, song list will be a list, each song will be a dict

example1 = {"song_name": "cool boys", "song_artist/s": ["the boiz"], "duration": 2.3}
example2 = {"song_name": "chilly billy", "song_artist/s": ["bill","chill"], "duration": 3.7}
example3 = {"song_name": "popular peeps", "song_artist/s": ["Jeff"], "duration": 5.2}
list_of_cool_songs = [example1, example2, example3]

playlist = { 
	"playlist_title": "cool songs 3",
	"playlist_creator": "Tim",
	"song_list": list_of_cool_songs,
}

print(playlist)

total_length = 0
for song in playlist["song_list"]:
	total_length += song["duration"]
print(total_length)
