from madlibs_games import game_1, game_2, game_3, game_4
import random

if __name__ == "__main__":
    m = random.choice([game_1.madlibs, game_2.madlibs, game_3.madlibs, game_4.madlibs])
    m()