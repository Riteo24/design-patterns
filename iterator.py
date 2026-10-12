"""Ітератор: незалежний обхід плейлиста без доступу до його списку."""
from collections.abc import Iterator, Iterable


class PlaylistIterator(Iterator):
    def __init__(self, songs):
        self._songs = tuple(songs)  # Незалежний знімок послідовності.
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._position >= len(self._songs):
            raise StopIteration
        song = self._songs[self._position]
        self._position += 1
        return song


class Playlist(Iterable):
    def __init__(self):
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __iter__(self):
        return PlaylistIterator(self._songs)


def main():
    playlist = Playlist()
    playlist.add("Пісня 1")
    playlist.add("Пісня 2")
    playlist.add("Пісня 3")
    for song in playlist:
        print(song)


if __name__ == "__main__":
    main()
