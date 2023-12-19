import random
from game import Game, Move, Player
from tqdm import tqdm
from myplayer import MyPlayer1


class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: "Game") -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move


# class MyPlayer(Player):
#     def __init__(self) -> None:
#         super().__init__()

#     def make_move(self, game: "Game") -> tuple[tuple[int, int], Move]:
#         from_pos = (random.randint(0, 4), random.randint(0, 4))
#         move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
#         return from_pos, move


if __name__ == "__main__":
    player1 = MyPlayer1(0, preload=True)
    player2 = RandomPlayer()

    g = Game()
    winner = g.play(player1, player2)
    print(winner)

    wins = 0
    for _ in tqdm(range(100)):
        g = Game()
        winner = g.play(player1, player2)
        wins += 1 if winner == 0 else 0
    print("Win rate:", wins / 100)
