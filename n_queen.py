from n_by_n_board import NxNBoard


class NQueen:
    def __init__(self, board):
        self.board = board

    def place_queen_naive(self, n, start_row, start_col, solution):
        if solution == n:
            print('\nSolution - \n')
            self.board.print_board()
            print('')
            print(self.board.get_filled_cells())
            return -1
        for i in range(start_row, n):
            for j in range(start_col, n):
                if self.is_queen_safe((i, j), n):
                    self.board.set_cell_value(i, j, 1)
                    solution += 1
                    # self.board.print_board()
                    if self.place_queen_naive(n, start_row, start_col, solution) == 0:
                        self.board.set_cell_value(i, j, 0)
                        solution -= 1
                    else:
                        return -1
        return 0

    def is_queen_safe(self, position, n):
        return self.check_row(position, n) and self.check_column(position, n) and self.check_diagonal(position, n)

    def check_row(self, position, n):
        row = position[0]
        total = 0
        for i in range(0, n):
            total += self.board.get_cell_value(row, i)
        return total < 1

    def check_column(self, position, n):
        col = position[1]
        total = 0
        for i in range(0, n):
            total += self.board.get_cell_value(i, col)
        return total < 1

    def check_diagonal(self, position, n):
        row = position[0]
        col = position[1]
        total = 0
        for i in range(0, n):
            new_row = row - i
            new_col = col - i
            if new_row >= 0 and new_col >= 0:
                total += self.board.get_cell_value(new_row, new_col)

        for j in range(1, n):
            new_row = row + j
            new_col = col + j
            if new_row < n and new_col < n:
                total += self.board.get_cell_value(new_row, new_col)

        for k in range(1, n):
            new_row = row + k
            new_col = col - k
            if new_row < n and new_col >= 0:
                total += self.board.get_cell_value(new_row, new_col)

        for p in range(1, n):
            new_row = row - p
            new_col = col + p
            if new_row >= 0 and new_col < n:
                total += self.board.get_cell_value(new_row, new_col)
        return total < 1


def main():
    n = 8
    board = NxNBoard(n, n)
    nqueen = NQueen(board)
    nqueen.place_queen_naive(n, 0, 0, 0)
    pass


if __name__ == "__main__":
    main()