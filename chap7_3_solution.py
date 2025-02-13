# Define a class `Playlist`
class Playlist:
    
    # Define the constructor method (__init__)
    # This method initializes the playlist with a list of songs
    def __init__(self, songs):
        
        # Assign the `songs` parameter to the instance variable `self.songs`
        self.songs = songs  

    # Define a special method `__getitem__`
    # This method allows indexing access to the playlist
    def __getitem__(self, index):
        return self.songs[index]  # Return the song at the given index

# Create an instance of the `Playlist` class with a list of songs
my_playlist = Playlist(["Song 1", "Song 2", "Song 3"])

# Access a song using index notation
print(my_playlist[1])  # Output: Song 2
