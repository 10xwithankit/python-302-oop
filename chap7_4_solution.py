# Define a class `Playlist`
class Playlist:
    
    # Define the constructor method (__init__)
    # This method initializes the playlist with a list of songs
    def __init__(self, songs):
        
        # Assign the `songs` parameter to the instance variable `self.songs`
        self.songs = songs  

    # Define a special method `__setitem__`
    # This method allows modifying a song at a specific index
    def __setitem__(self, index, song):
        self.songs[index] = song  # Update the song at the given index

# Create an instance of the `Playlist` class with a list of songs
my_playlist = Playlist(["Song 1", "Song 2", "Song 3"])

# Modify the second song in the playlist using index notation
my_playlist[1] = "New Song"

# Print the updated list of songs in the playlist
print(my_playlist.songs)  # Output: ['Song 1', 'New Song', 'Song 3']
