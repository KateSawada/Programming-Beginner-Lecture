#!/usr/bin/env python3
import copy

class OthelloGame():
    def __init__(self):
        #行と列の見出しの文字を作成
        #変更不可にするためにtupleを使う
        self.col_idx = ("a", "b", "c", "d", "e", "f", "g", "h")
        self.row_idx = ("1", "2", "3", "4", "5", "6", "7", "8")
        
        #8x8の盤面情報を保存するlistを作成
        #重複アリ&変更アリ
        self.board = []
        for i in range(8):
            self.board.append([0])
            for _ in range(8 - 1):
                self.board[i].append(0)
            

        #指手の入力は文字列strで受け取るため, listのインデックスにあわせてintに変換する必要あり
        self.row_idx2int ={
            "1": 0,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "7": 6,
            "8": 7
        }
        self.col_idx2int = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7
        }

        self.stone2str = {
            #先手=>緑
            1: '\033[32m'+'X'+'\033[0m',
            #後手=>赤
            -1: '\033[31m'+'X'+'\033[0m',
            0: ' '
        }

        self.opponent = {
            1: -1,
            -1: 1
        }

        #最初の石の配置
        self.board[3][3] = 1
        self.board[3][4] = -1
        self.board[4][3] = -1
        self.board[4][4] = 1

        print("initialize done! othello game is ready!")
            
    def draw_board(self):
        """
        盤面を表示する関数
        """
        #列見出しの表示
        for i in range(len(self.board[0])):
            print(" " + self.col_idx[i], end="")
        print("")
        #ボードの表示   
        print("--" * len(self.board[0]) + "-")
        #1~7行目
        for i in range(len(self.board) - 1):
            print("|", end="")
            for j in range(len(self.board[0])):
                print(self.stone2str[self.board[i][j]] + "|", end="")
            print(self.row_idx[i])
            print("|-" + "+-" * 7 + "|")
        #8行目
        print("|", end="")
        for i in range(len(self.board[0])):
            print(self.stone2str[self.board[-1][i]] + "|", end="")
        print(self.row_idx[-1])
        print("--" * len(self.board[0]) + "-")

        
    
    def can_put_stone(self, player):
        """
        まだ石を置けるか確認する関数
        """
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                check_board = copy.deepcopy(self.board)
                if self.board[y][x] == 0 and self.put_stone(check_board, x, y, player):
                    return True
        return False
   


    def put_stone(self, board, row, col, player):
        turned = False

        if row + 1 < len(board) and board[row + 1][col] == self.opponent[player]:
            for i in range(1, len(board) - row):
                if board[row + i][col] == self.opponent[player]:
                    pass
                elif board[row + i][col] == 0:
                    break
                elif board[row + i][col] == player:
                    for j in range(0, i):
                        board[row + j][col] = player
                    turned = True
                    break
        
        if row - 1 > 0 and board[row - 1][col] == self.opponent[player]:
            for i in range(1, row + 1):
                if board[row - i][col] == self.opponent[player]:
                    pass
                elif board[row - i][col] == 0:
                    break
                elif board[row - i][col] == player:
                    for j in range(0, i):
                        board[row - j][col] = player
                    turned = True
                    break
        
        if col + 1 < len(board[0]) and board[row][col + 1] == self.opponent[player]:
            for i in range(1, len(board[0]) - col):
                if board[row][col + i] == self.opponent[player]:
                    pass
                elif board[row][col + i] == 0:
                    break
                elif board[row][col + i] == player:
                    for j in range(0, i):
                        board[row][col + j] = player
                    turned = True
                    break

        if col - 1 > 0 and board[row][col - 1] == self.opponent[player]:
            for i in range(1, col + 1):
                if board[row][col - i] == self.opponent[player]:
                    pass
                elif board[row][col - i] == 0:
                    break
                elif board[row][col - i] == player:
                    for j in range(0, i):
                        board[row][col - j] = player
                    turned = True
                    break

        if row + 1 < len(board) and col + 1 < len(board[0]) and board[row + 1][col + 1] == self.opponent[player]:
            for i in range(1, min(len(board) - row, len(board[0]) - col)):
                if board[row + i][col + i] == self.opponent[player]:
                    pass
                elif board[row + i][col + i] == 0:
                    break
                elif board[row + i][col + i] == player:
                    for j in range(0, i):
                        board[row + j][col + j] = player
                    turned = True
                    break

        if row + 1 < len(board) and col - 1 > 0 and board[row + 1][col - 1] == self.opponent[player]:
            for i in range(1, min(len(board) - row, col + 1)):
                if board[row + i][col - i] == self.opponent[player]:
                    pass
                elif board[row + i][col - i] == 0:
                    break
                elif board[row + i][col - i] == player:
                    for j in range(0, i):
                        board[row + j][col - j] = player
                    turned = True
                    break

        if row - 1 > 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] == self.opponent[player]:
            for i in range(1, min(row + 1, len(board[0]) - col)):
                if board[row - i][col + i] == self.opponent[player]:
                    pass
                elif board[row - i][col + i] == 0:
                    break
                elif board[row - i][col + i] == player:
                    for j in range(0, i):
                        board[row - j][col + j] = player
                    turned = True
                    break

        if row - 1 > 0 and col - 1 > 0 and board[row - 1][col - 1] == self.opponent[player]:
            for i in range(1, min(row + 1, col + 1)):
                if board[row - i][col - i] == self.opponent[player]:
                    pass
                elif board[row - i][col - i] == 0:
                    break
                elif board[row - i][col - i] == player:
                    for j in range(0, i):
                        board[row - j][col - j] = player
                    turned = True
                    break
        
        if not turned and id(board) == id(self.board):
            print("you can not put stone there")

        return turned
    
    def count_stone(self, player):
        return sum(self.board, []).count(player)

    def play(self):
        """
        ゲーム本体
        """

        player = 1
        self.playing = True
        while self.playing:
            #まだ石を置けるか判定
            #現在のplayerが置けないなら，パス
            if not self.can_put_stone(player):
                player = self.opponent[player]
                #パスしても置けないなら終了
                if not self.can_put_stone(player):
                    break
            self.draw_board()
            stoneP1 = self.count_stone(1)
            stoneP2 = self.count_stone(-1)
            print('\033[32m'+'Player1: {}'.format(stoneP1)+'\033[0m')
            print('\033[31m'+'Player2: {}'.format(stoneP2)+'\033[0m')
            #石を置く座標の入力
            if player == 1:
                print('\033[32m'+'Player1, '+'\033[0m', end="")
            elif player == -1:
                print('\033[31m'+'Player2, '+'\033[0m', end="")
            print("where would you like to put stone?: ", end="")
            coordinate = input()
            if len(coordinate) != 2 or coordinate[0] not in self.col_idx2int or coordinate[1] not in self.row_idx2int:
                print("your input is wrong! please retry")
                continue
            can_switch = False
            can_switch = self.put_stone(self.board, self.row_idx2int[coordinate[1]], self.col_idx2int[coordinate[0]],  player)
            if can_switch:
                player = self.opponent[player]
        
        #石を数えて勝敗を決める
        print("-" * 8 + "result" + "-" * 8)
        print('\033[32m'+'Player1: {}'.format(stoneP1)+'\033[0m')
        print('\033[31m'+'Player2: {}'.format(stoneP2)+'\033[0m')
        if stoneP1 > stoneP2:
            print("Player1 win!")
        elif stoneP1 < stoneP2:
            print("Player2 win!")
        else:
            print("draw")
         

if __name__ == "__main__":
    game = OthelloGame()
    game.play()
    