class Song:
    count = 0
    genres = []
    artists =[]
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_artists(self)

    @classmethod
    def add_song_to_count(cls, song):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        if song.genre not in cls.genres:
            cls.genres.append(song.genre)

        if song.genre in cls.genre_count:
            cls.genre_count[song.genre] += 1
        else:
            cls.genre_count[song.genre] = 1

    @classmethod
    def add_to_artists(cls, song):
        if song.artist not in cls.artists:
            cls.artists.append(song.artist)

        if song.artist in cls.artist_count:
            cls.artist_count[song.artist] += 1
        else:
            cls.artist_count[song.artist] = 1
        

    

    

