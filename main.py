class Gameboard():

    def __init__(self):
        self.gameboard = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}

    def setPeice(self, user, position, gameboard):
        gameboard[position] = user
        return gameboard
    @property
    def gameBoard(self):
        '''
        need to learn more about properties. They seem to be used primarily as
        getters and setters. ??
        '''
        return self.gameboard

    def clearboard(self):
        self.gameboard = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}

    def is_place_taken(self, gameboard, index):
        if gameboard[index] != ' ' :
            return True

    def is_board_full(self, gameboard):
    return all(gameboard[index] != ' ' for index in range(1, 10))

    def is_game_won(self, gameboard):
        win_conds = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
        for win_cond in win_conds:
            if gameboard[win_cond[0]] == gameboard[win_cond[1]] and gameboard[win_cond[1]] == gameboard[win_cond[2]] and gameboard[win_cond[0]]!= ' ':
                return True


    def printBoard(self,gameboard):
        index = 0
        for row in range(1,4):
            for column in range(1,4):
                index += 1
                if column != 3:
                    print(gameboard[index], end='')
                    print('|', end='')
                else:
                    print(gameboard[index])


class Game():

    def on_start(self):
        '''
        Called on initial start and in subsequent restarts
        '''
        self.controlBoard = Gameboard()
        self.gameboard = self.controlBoard.gameBoard
        self.playerOne ='o'
        self.playerTwo = 'x'
        print('Welcome to tic-tac-toe')
        print("What is player one's name?")
        self.player_one = input(' : ')
        print("What is player two's name?")
        self.player_two = input(' : ')
        print('Here is your game board, each place is represented by 1-9, starting from left column each time and movng along the row')
        self.controlBoard.printBoard(self.gameboard)
        self.turn = 1

    def on_end(self):
        #check if a player wants to end the game
        if self.running == False:
            replay = input('Press 0 to quit or 1 to play again: ')
            try:
                if int(replay):
                    self.running = True
                    self.on_start()
            except:
                print("A number must be entered.")
                self.on_end()


    def takeTurn(self, user, peice):
        print(user + ' choose a place, 1-9')
        try:
            position = int(input(': '))
            if position > 9 or position < 1:
                raise Exception

        except:
            print('Pick a number between 1-9')
            return self.takeTurn(user, peice)

        if self.controlBoard.is_place_taken(self.gameboard, position):
            print("That place is taken")
            self.takeTurn(user,peice)
        else:
            self.controlBoard.setPeice(peice, position, self.gameboard)
            self.controlBoard.printBoard(self.gameboard)
            if self.controlBoard.is_game_won(self.gameboard):
                print(user +  " wins.")
                self.running = False


    def main(self,):
        self.running = True
        self.on_start()
        while self.running:
            if self.turn%2 != 0:
                self.takeTurn(self.player_one, 'o')
            else:
                self.takeTurn(self.player_two, 'x')

            if self.controlBoard.is_board_full(self.gameboard):
                print("Its a draw!! You both lose!")
                self.running = False
            self.turn += 1

            if not self.running:
                self.on_end()



if __name__ == '__main__':
    Game().main()