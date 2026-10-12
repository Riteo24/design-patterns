"""Фасад: один метод координує три підсистеми домашнього кінотеатру."""


class Projector:
    def turn_on(self):
        return "Проєктор увімкнено"


class SoundSystem:
    def set_volume(self, level):
        return f"Гучність: {level}"


class VideoPlayer:
    def play(self, movie):
        return f"Відтворення: {movie}"


class HomeTheaterFacade:
    def __init__(self, projector, sound, player):
        self._projector = projector
        self._sound = sound
        self._player = player

    def watch_movie(self, movie):
        return [
            self._projector.turn_on(),
            self._sound.set_volume(50),
            self._player.play(movie),
        ]


def main():
    theater = HomeTheaterFacade(Projector(), SoundSystem(), VideoPlayer())
    for message in theater.watch_movie("Інтерстеллар"):
        print(message)


if __name__ == "__main__":
    main()
