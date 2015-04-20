__author__ = 'Katherine'

import tkinter as tk
import copy

class Chess_Game:

    pieces = {"Q": ["white queen", 8, [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]], [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]],
          "R": ["white rook", 8, [[0, 1], [1, 0], [0, -1], [-1, 0]], [[0, 1], [1, 0], [0, -1], [-1, 0]]],
          "B": ["white bishop", 8, [[1, 1], [-1, -1], [-1, 1], [1, -1]], [[1, 1], [-1, -1], [-1, 1], [1, -1]]],
          "N": ["white knight", 1, [[1, 2], [-1, 2], [-1, -2], [1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]], [[1, 2], [-1, 2], [-1, -2], [1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]],
          "P": ["white pawn", 1, [[0, -1]], [[1, -1], [-1, -1]]],
          "K": ["white king", 1, [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]], [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]],
          "q": ["black queen", 8, [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]], [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]],
          "r": ["black rook", 8, [[0, 1], [1, 0], [0, -1], [-1, 0]], [[0, 1], [1, 0], [0, -1], [-1, 0]]],
          "b": ["black bishop", 8, [[1, 1], [-1, -1], [-1, 1], [1, -1]], [[1, 1], [-1, -1], [-1, 1], [1, -1]]],
          "n": ["black knight", 1, [[1, 2], [-1, 2], [-1, -2], [1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]], [[1, 2], [-1, 2], [-1, -2], [1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]],
          "p": ["black pawn", 1, [[0, 1]], [[1, 1], [-1, 1]]],
          "k": ["black king", 1, [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]], [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]]}

    board = [[["r", "r1"], ["n", "n1"], ["b", "b1"], ["q", "q"], ["k", "k"], ["b", "b2"], ["n", "n2"], ["r", "r2"]], [["p", "p1"], ["p", "p2"], ["p", "p3"], ["p", "p4"], ["p", "p5"], ["p", "p6"], ["p", "p7"], ["p", "p8"]], [[" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "]], [[" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "]], [[" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "]], [[" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "], [" ", " "]], [["P", "P1"], ["P", "P2"], ["P", "P3"], ["P", "P4"], ["P", "P5"], ["P", "P6"], ["P", "P7"], ["P", "P8"]], [["R", "R1"], ["N", "N1"], ["B", "B1"], ["Q", "Q"], ["K", "K"], ["B", "B2"], ["N", "N2"], ["R", "R2"]]]

    def __init__(self, root):

        self.taken = []
        self.GUI = root

        self.canvas = tk.Canvas(root, height=900, width=900, bg="floral white")
        self.canvas.grid(row=1, column=0)

        self.turn = "w"
        self.num_clicks = 0

        self.temp = tk.StringVar()
        tk.Label(root, textvariable=self.temp).grid(row=0, column=0)
        self.canvas.bind("<Button-1>", self.clicking)

        self.possible_moves = []

        for row in range(8):
            for column in range(8):
                tag = str(row)+","+str(column)
                if (row + column) % 2 == 0:
                    self.canvas.create_rectangle(row*100 + 50, column*100 + 50, row*100 + 150, column*100 + 150, tags=tag, fill="LightSteelBlue2")
                else:
                    self.canvas.create_rectangle(row*100 + 50, column*100 + 50, row*100 + 150, column*100 + 150, tags=tag, fill="SlateBlue2")
        for i in range(8):
            for j in range(8):
                self.canvas.create_text(j*100 + 100, i*100 + 100, text=self.board[i][j][0], tags=self.board[i][j][1], fill="black")


    def refresh_GUI(self):
        for row in range(8):
            for column in range(8):
                tag = str(row)+","+str(column)
                if (row + column) % 2 == 0:
                    self.canvas.create_rectangle(row*100 + 50, column*100 + 50, row*100 + 150, column*100 + 150, tags=tag, fill="LightSteelBlue2")
                else:
                    self.canvas.create_rectangle(row*100 + 50, column*100 + 50, row*100 + 150, column*100 + 150, tags=tag, fill="SlateBlue2")
        for i in range(8):
            for j in range(8):
                self.canvas.create_text(j*100 + 100, i*100 + 100, text=self.board[i][j][0], tags=self.board[i][j][1], fill="black")

    def reset_clicks(self):
        self.num_clicks = 0
        self.refresh_GUI()
        self.possible_moves = []

    def clicking(self, event):
        row = (event.x-50)//100
        col = (event.y-50)//100
        piece = self.board[col][row][0]
        self.temp.set(str(row)+","+str(col))

        if self.num_clicks == 0:

            if piece != " ":
                old_click = [row, col]
                self.possible_moves = self.poss_moves([row, col])
                if self.turn == "w" and piece.upper() == piece:
                    self.canvas.itemconfig(str(row)+","+str(col), fill="DarkOrchid2")

                    for move in self.possible_moves:
                        row = move[0]
                        col = move[1]
                        self.canvas.itemconfig(str(row)+","+str(col), fill="yellow")
                    self.num_clicks = 1

                elif self.turn == "b" and piece.lower() == piece:
                    self.canvas.itemconfig(str(row)+","+str(col), fill="DarkOrchid2")

                    for move in self.possible_moves:
                        row = move[0]
                        col = move[1]
                        self.canvas.itemconfig(str(row)+","+str(col), fill="green")
                    self.num_clicks = 1

                self.possible_moves.append(old_click)
                print("possible_moves: ", self.possible_moves)

        elif self.num_clicks == 1:
            old_click = self.possible_moves.pop()
            if [row, col] in self.possible_moves:
                self.move(old_click, [row, col])
                self.reset_clicks()
                if self.turn == "w":
                    self.turn = "b"
                else:
                    self.turn = "w"
            else:
                self.reset_clicks()


    def color(self, piece):
        if piece.upper() == piece:
            return "White"
        else:
            return "Black"


    def color_check(self, piece1, piece2):
        if piece1 == " ":
            return False
        if piece2 == " ":
            return True
        if (piece1 and piece2) in self.pieces:
            if self.color(piece1) == self.color(piece2):
                return False
            else:
                return True
        else:
            return False


    def normalize(self, x, y):
        n = min(abs(x), abs(y))
        if n != 0:
            num_moves = n
            normalized = [x/n, y/n]
        else:
            if abs(x) > abs(y):
                num_moves = abs(x)
                normalized = [int(x/(abs(x))), 0]
            elif abs(x) < abs(y):
                num_moves = abs(y)
                normalized = [0, int(y/(abs(y)))]
            else:
                num_moves = 0
                normalized = [0, 0]
        return num_moves, normalized



    def check_move_piece(self, board, current_pos, new_pos):
        if min(current_pos) < 0 or max(current_pos) > 7:
            return False

        newx, newy = new_pos[0], new_pos[1]
        currentx, currenty = current_pos[0], current_pos[1]
        piece = board[currenty][currentx][0]
        move_piece = board[newy][newx][0]

        vecx, vecy = newx - currentx, newy - currenty
        num_moves, normalized = self.normalize(vecx, vecy)[0], self.normalize(vecx, vecy)[1]
        #print("THE", "|", [currentx, currenty], ":", piece, "|", " IS MOVING TO ", "|", [newx, newy], ":", move_piece, "|")


        if not self.color_check(piece, move_piece):
            return False


        if piece.upper() == "P":
            if abs(num_moves) > 2:
                return False
            elif num_moves == 2:
                if (currenty == 1 and self.color(piece) == "Black") and (normalized in self.pieces[piece][2]):
                    for i in range(1, num_moves+1):
                        if board[currenty + i*normalized[1]][currentx + i*normalized[0]][0] != " ":
                            print("pawn is here")
                            return False
                    return True
                elif (currenty == 6 and self.color(piece) == "White") and (normalized in self.pieces[piece][2]):
                    for i in range(1, num_moves+1):
                        if board[currenty + i*normalized[1]][currentx + i*normalized[0]][0] != " ":
                            return False
                    return True

                else:
                    return False
            elif num_moves == 1:
                if normalized in self.pieces[piece][3] and move_piece != " ":
                    print('about to take')
                    return True
                elif normalized in self.pieces[piece][2] and self.color_check(piece, move_piece) and move_piece == " ":
                    return True
                else:
                    return False
            else:
                return False

        if piece.upper() != "N" and (normalized in self.pieces[piece][2]) and num_moves <= self.pieces[piece][1]:
            for i in range(1, num_moves):
                if board[currenty + i*int(normalized[1])][currentx + i*int(normalized[0])][0] != " ":
                    print("piece in the way at: ", "[", currenty + i*int(normalized[1]), ",", currentx + i*int(normalized[0]), "]", board[currenty + i*int(normalized[1])][currentx + i*int(normalized[0])][1])
                    return False
            if not self.color_check(piece, move_piece):
                    return False
            else:
                return True

        else:
            if piece.upper() == "N" and (normalized in self.pieces[piece][2]) and (num_moves == 1):
                if self.color_check(piece, move_piece):
                    return True


    def check_move_king(self, board, current_pos, new_pos):
        newx, newy = new_pos[0], new_pos[1]
        currentx, currenty = current_pos[0], current_pos[1]
        piece = board[currenty][currentx][0]

        new_board = copy.deepcopy(board)
        new_board[newy][newx] = new_board[currenty][currentx]
        new_board[currenty][currentx] = [" ", " "]

        for x in range(8):
            for y in range(8):
                search = new_board[y][x][0]
                if search.upper() == "K" and not self.color_check(piece, search):
                    #print("FOUND our king", search, "at (", x, ",", y, ")")
                    king_pos = [x, y]
        for x in range(8):
            for y in range(8):
                search = new_board[y][x][0]
                tag_search = new_board[y][x][1]
                if self.color_check(search, piece) and self.check_move_piece(new_board, [x, y], king_pos):
                        #print("checking", "[", x, ",", y, "]...", search, tag_search, " is going to kill your king")
                        return False

        return True



    def move_check(self, board, current_pos, new_pos):
        return self.check_move_piece(board, current_pos, new_pos) and self.check_move_king(board, current_pos, new_pos)

    def poss_moves(self, current_pos):
        currentx, currenty = current_pos[0], current_pos[1]
        num_moves, normalized = self.normalize(currentx, currenty)[0], self.normalize(currentx, currenty)[1]
        possibles = []
        if self.board[current_pos[1]][current_pos[0]][0] != " ":
            for i in range(8):
                for j in range(8):
                    if self.move_check(self.board, current_pos, [i, j]):
                        possibles.append([i, j])
        return possibles

    def move(self, current_pos, new_pos):
        newx, newy = new_pos[0], new_pos[1]
        currentx, currenty = current_pos[0], current_pos[1]
        piece = self.board[currenty][currentx][0]
        tag_piece = self.board[currenty][currentx][1]
        if self.move_check(self.board, current_pos, new_pos):
            self.board[currenty][currentx] = [" ", " "]
            self.board[newy][newx] = [piece, tag_piece]

root = tk.Tk()
Chess_Game(root)
chessie = Chess_Game(root)
root.mainloop()