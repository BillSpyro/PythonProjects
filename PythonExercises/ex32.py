# Exercise 32

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right here"
])

bulls_on_parade = Song([
    "They rally around the family",
    "With pockets full of shells"
])

new_song = Song([
    "This is a new test song",
    "This is the second line",
    "This is the third line"
])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
new_song.sing_me_a_song()
