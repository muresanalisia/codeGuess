from game.game import Game
from ui.ui import Ui

def main():
    game=Game()
    ui=Ui(game=game)
    ui.intro()
    ui.command()

if __name__ == '__main__':
    main()
