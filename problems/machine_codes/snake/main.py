import random

class Board:

    def __init__(self):
        print('board is instantiated')
        self.state = [0]*100

    # move player on board
    def move(self, pos, target):
        print(f'moving')

    def update(self, pos, val):
        self.state[pos] = val
        print(self.state)

    def add_snake(self, head, tail):
        self.state[head] = ['S','H',tail]
        self.state[tail] = ['S','T',head]

    def add_ladder(self, top, bottom):
        self.state[top] = ['L', 'T', bottom]
        self.state[bottom] = ['L', 'B', top]

    def __str__(self):
        return str(self.state)

    # def player_pos(self):


class Player:
    def __init__(self, name):
        print('player initialised')

    def s(self):
        return 'player mf'


class SpecialPlayer(Player):
    def s(self):
        return 'special player mf'

if __name__ == '__main__':

    # board = Board()
    # print(board.state)
    # print(board)

    p = Player('me')
    k = SpecialPlayer('me')
    print(p.s())
    print(k.s())

    # for _ in range(3):
    #     for i in range(int(input())):
    #         pass



