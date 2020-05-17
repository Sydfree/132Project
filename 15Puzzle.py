import tkinter as tk
import enum
import random


class MoveDirection(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Board:
    EMPTY_CELL = "#"

    def __init__(self, board_size):
        self._board_size = board_size
        self._cell_count = self._board_size * self._board_size
        self._init_board()

    def _init_board(self):
        values = self._iter_cell_values()
        self._board = [[Cell(next(values)) for i in range(
            self._board_size)] for j in range(self._board_size)]

    def _check_if_valid_position(self, x, y):
        x_is_valid = True if 0 <= x < self._board_size else False
        y_is_valid = True if 0 <= y < self._board_size else False

        if x_is_valid and y_is_valid:
            return True
        else:
            return False

    def _get_empty_cell_position(self):
        for i in range(self._board_size):
            for j in range(self._board_size):
                if self.get_cell_value(i, j) == self.EMPTY_CELL:
                    return i, j

    def _get_next_position(self, x, y, direction):
        if direction == MoveDirection.UP:
            return x - 1, y
        elif direction == MoveDirection.RIGHT:
            return x, y + 1
        elif direction == MoveDirection.DOWN:
            return x + 1, y
        elif direction == MoveDirection.LEFT:
            return x, y - 1

    def _is_cell_value_equal_to(self, x, y, value):
        if self.get_cell_value(x, y) == value:
            return True
        else:
            return False

    def _iter_cell_values(self):
        values = [i for i in range(1, self._cell_count)]
        values.append(self.EMPTY_CELL)
        return iter(values)

    def _swap_cells(self, x1, y1, x2, y2):
        self._board[x1][y1], self._board[x2][y2] = self._board[x2][y2], self._board[x1][y1]

    def _yield_random_directions(self, amount_of_moves):
        possible_directions = list(MoveDirection)
        for _ in range(amount_of_moves):
            yield random.choice(possible_directions)

    def DEBUG_PRINT_BOARD(self):
        for i in range(self._board_size):
            row = ""
            for j in range(self._board_size):
                number = str(self.get_cell_value(i, j))
                row += number + " "
                if len(number) == 1:
                    row += " "
            print(row)

    def _distance_to_empty_cell(self, x, y):
        x_empty, y_empty = self._get_empty_cell_position()
        return x - x_empty, y - y_empty

    def _on_the_same_row_or_column_as_empty_cell(self, x, y):
        x_empty, y_empty = self._get_empty_cell_position()
        if x == x_empty or y == y_empty:
            return True
        else:
            return False

    def _move_cell_to_direction(self, x, y, direction):
        new_x, new_y = self._get_next_position(x, y, direction)
        if self._check_if_valid_position(new_x, new_y):
            self._swap_cells(x, y, new_x, new_y)

    def _move_empty_cell_to_direction(self, direction):
        x, y = self._get_empty_cell_position()
        self._move_cell_to_direction(x, y, direction)

    def _get_direction_from_distance(self, x, y):
        if x < 0:
            return MoveDirection.UP
        elif x > 0:
            return MoveDirection.DOWN
        elif y < 0:
            return MoveDirection.LEFT
        elif y > 0:
            return MoveDirection.RIGHT

    def _get_moves_for_empty_cell(self, x, y):
        moves = []
        if self._on_the_same_row_or_column_as_empty_cell(x, y):
            x_dist, y_dist = self._distance_to_empty_cell(x, y)
            direction = self._get_direction_from_distance(x_dist, y_dist)
            for _ in range(abs(x_dist + y_dist)):
                moves.append(direction)
        return moves

    def move(self, x, y):
        """Try to move the slot with the given coordinates.
        
        Movement is "aggressive" and multiple slots can move, given it does
        not break any rules of the game.
        """
        directions = self._get_moves_for_empty_cell(x, y)
        for d in directions:
            self._move_empty_cell_to_direction(d)

    def get_cell_value(self, x, y):
        """Get cell value in the coordinates (x,y)."""
        return self._board[x][y].value

    def set_cell_value(self, x, y, value):
        """Set cell with the coordinates (x,y) to a given value."""
        self._board[x][y].value = value

    def is_solved(self):
        """Return true/false based on if the board is solved or not."""
        max_index = self._board_size - 1
        if self.get_cell_value(max_index, max_index) == self.EMPTY_CELL:
            values = self._iter_cell_values()
            for i in range(self._board_size):
                for j in range(self._board_size):
                    if self._is_cell_value_equal_to(i, j, next(values)) == False:
                        return False
            return True
        else:
            return False

    def shuffle(self):
        """Randomize the board. Randomized board is guaranteed to be solvable."""
        self._init_board()
        amount_of_moves = 1000
        directions = self._yield_random_directions(amount_of_moves)

        for _ in range(amount_of_moves):
            self._move_empty_cell_to_direction(next(directions))


class Cell:
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Application(tk.Frame):
    def __init__(self, master=None):
        self._board_size = 4
        self._board = Board(self._board_size)
        self._board_cells = [[None for i in range(
            self._board_size)] for j in range(self._board_size)]

        tk.Frame.__init__(self, master)

        self.grid(padx=70, pady=70)
        self.create_cells()
        self.create_elements()
        self._board.shuffle()
        self.update_view()

    def click_handler(self, x, y):
        self._board.move(x, y)
        self.update_view()

    def create_elements(self):
        self.game_solved_text = tk.Message(self, text="", aspect=250)
        self.game_solved_text.grid(row=self._board_size + 2, column=0, columnspan=4)

        self.new_game_button = tk.Button(self, text="New game", cursor="hand2")
        self.new_game_button.config(command=self.start_new_game)
        self.new_game_button.grid(columnspan=4, sticky=tk.W)

    def check_if_solved(self):
        if self._board.is_solved():
            self.game_solved_text.config(text="Yay! You did it!")

    def start_new_game(self):
        self.game_solved_text.config(text="")
        self._board.shuffle()
        self.update_view()

    def update_view(self):
        for i in range(self._board_size):
            for j in range(self._board_size):
                cell_value = str(self._board.get_cell_value(i, j))
                if cell_value == self._board.EMPTY_CELL:
                    cell_value = "    "
                elif len(cell_value) == 1:
                    cell_value = " " + cell_value + " "
                self._board_cells[i][j].config(text=cell_value)
        self.check_if_solved()

    def create_cells(self):
        for i in range(self._board_size):
            for j in range(self._board_size):
                cell = tk.Button(self, cursor="hand2")
                cell.config(command=lambda x=i, y=j: self.click_handler(x, y))
                cell.grid(row=i, column=j, ipadx=8, ipady=3)
                self._board_cells[i][j] = cell

app = Application()

app.master.title("15 Puzzle")
app.mainloop()
