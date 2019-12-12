class NxNBoard:

    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column
        self.board = [[0 for i in range(self.column)] for j in range(self.row)]
        self.filled_cells = []

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def get_cell_value(self, row, col):
        return self.board[row][col]

    def set_cell_value(self, row, col, value):
        self.board[row][col] = value
        if value == 1:
            self.filled_cells.append((row, col))
        elif value == 0:
            self.filled_cells.remove((row, col))

    def get_filled_cells(self):
        return self.filled_cells


def main():
    board = NxNBoard(4, 4)
    board.get_board()
    board.print_board()
    board.set_cell_value(2, 1, 20)
    print('')
    board.print_board()
    pass


if __name__ == "__main__":
    main()
