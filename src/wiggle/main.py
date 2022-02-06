from typing import Tuple
import os

from colour import Color


def rgb_255(rgb_floats: Tuple[float, float, float]) -> Tuple[int, int, int]:
    return tuple(map(lambda v: int(v * 255), rgb_floats))  # type: ignore


def color_tuple(rep: str) -> Tuple[int, int, int]:
    color = Color(rep)
    rgb_floats = color.rgb
    rgb_ints = rgb_255(rgb_floats)
    return rgb_ints


class Game:
    import pygame as pg

    def __init__(self, x: int, y: int, caption: str):
        os.environ["SDL_VIDEO_WINDOW_POS"] = f"{x},{y}"  # window location
        self.pg.init()
        self.screen = self.pg.display.set_mode((600, 500), self.pg.RESIZABLE)
        self.pg.display.set_caption(caption)

    def draw(self) -> None:
        self.pg.draw.circle(
            surface=self.screen,
            color=color_tuple("red"),
            center=(250, 250),
            radius=80,
        )
        self.pg.draw.rect(
            surface=self.screen,
            color=color_tuple("blue"),
            rect=(60, 60, 100, 100),
        )

    def run(self) -> None:
        done = False
        while not done:
            for event in self.pg.event.get():
                if event.type == self.pg.QUIT:
                    done = True
            self.draw()
            self.pg.display.flip()


def main() -> None:
    game = Game(100, 100, "Wiggle Game!")
    game.run()


if __name__ == "__main__":
    main()
