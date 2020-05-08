import webbrowser
from tkinter import *
import tkinter as tkinter
import random

LARGE_FONT= ("Verdana", 12)

class MyGUI(tkinter.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Category, NetflixOptions, MovieOptions, ShowOptions, MusicOptions, GamingOptions, CookingOptions, ProductivityOptions, WorkoutOptions):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self,parent)
        label = tkinter.Label(self, text="Click Here To Start Your Quarantine Adventure!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Categories = tkinter.Button(self, text="Quarantine Adventure!", command=lambda: controller.show_frame(Category))
        Categories.pack()
        

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
       

    
class Category(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Doing Today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Netflix = tkinter.Button(self, text="Netflix?", command=lambda: controller.show_frame(NetflixOptions))
        Netflix.pack()
        Music = tkinter.Button(self, text="Music?", command=lambda: controller.show_frame(MusicOptions))
        Music.pack()
        Gaming = tkinter.Button(self, text='Gaming?',command=lambda: controller.show_frame(GamingOptions))
        Gaming.pack()
        Cooking = tkinter.Button(self, text='Cooking?',command=lambda: controller.show_frame(CookingOptions))
        Cooking.pack()
        Productivity = tkinter.Button(self, text='Productivity?',command=lambda: controller.show_frame(ProductivityOptions))
        Productivity.pack()
        Workout = tkinter.Button(self, text='Workout?',command=lambda: controller.show_frame(WorkoutOptions))
        Workout.pack()
        


        
class NetflixOptions(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Are You Feeling A Movie or Some Shows?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        

        Movie = tkinter.Button(self, text='Movies?',command=lambda: controller.show_frame(MovieOptions))
        Movie.pack()

        Show = tkinter.Button(self, text='Show?',command=lambda: controller.show_frame(ShowOptions))
        Show.pack()

        Return1 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return1.pack()

class MovieOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        ActionMovie = tkinter.Button(self, text='Action?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/1365?bc=34399'))
        ActionMovie.pack()

        RomanceMovie = tkinter.Button(self, text='Romance?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/8883?bc=34399'))
        RomanceMovie.pack()

        HorrorMovie = tkinter.Button(self, text='Horror?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/8711?bc=34399'))
        HorrorMovie.pack()

        ComedyMovie = tkinter.Button(self, text='Comedy?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/6548?bc=34399'))
        ComedyMovie.pack()

        DocumentaryMovie = tkinter.Button(self, text='Documentary?',command=lambda:webbrowser.open('https://www.netflix.com/browse/genre/2243108?bc=34399'))
        DocumentaryMovie.pack()

        Return2 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(NetflixOptions))
        Return2.pack()


class ShowOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        RealityShow = tkinter.Button(self, text='Reality?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/9833?bc=83'))
        RealityShow.pack()
        ActionShow = tkinter.Button(self, text='Action?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/10673?bc=83'))
        ActionShow.pack()
        RomanceShow = tkinter.Button(self, text='Romance?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/26156?bc=83'))
        RomanceShow.pack()
        HorrorShow = tkinter.Button(self, text='Horror?',command=lambda:webbrowser.open('https://www.netflix.com/browse/genre/83059?bc=83'))
        HorrorShow.pack()
        ComedyShow = tkinter.Button(self, text='Comedy?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/10375?bc=83'))
        ComedyShow.pack()
        DocumentaryMovie = tkinter.Button(self, text='Documentary?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/10105?bc=83'))
        DocumentaryMovie.pack()
        Return8 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(NetflixOptions))
        Return8.pack()        


class MusicOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking", font=LARGE_FONT)
        label.pack(pady=10,padx=10)  


        Country = tkinter.Button(self, text='Country?',command=lambda: webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX1lVhptIYRda'))
        Country.pack()
        Rock = tkinter.Button(self, text='Rock?',command=lambda: webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U'))
        Rock.pack()
        Rap = tkinter.Button(self, text='Rap?',command=lambda: webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd'))
        Rap.pack()
        RandB = tkinter.Button(self, text='R&B?',command=lambda: webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX4SBhb3fqCJd'))
        RandB.pack()
        LoFi = tkinter.Button(self, text='Lo-Fi?',command=lambda: webbrowser.open('https://open.spotify.com/playlist/0TCxLrp0tEZrkGkaWhnFrE'))
        LoFi.pack()
        Return15 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return15.pack()


class GamingOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="I saw that we can load games using tkinter. reind me to talk about this. -Aidan ", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        NumPuzzle = tkinter.Button(self, text="Sliding Number Puzzle", command=lambda: controller.show_frame(NumPuzzle))
        NumPuzzle.pack()
        Sudoku = tkinter.Button(self, text="Sudoku", command=lambda: controller.show_frame(Sudoku))
        Sudoku.pack()
        Return21 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return21.pack()


class NumPuzzle(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

class Sudoku(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        
        

    
class CookingOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What're You Wanting To Cook?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        Breakfast = tkinter.Button(self, text='Breakfast?',command=lambda: webbrowser.open('https://www.foodnetwork.com/recipes/photos/our-best-breakfast-recipes'))
        Breakfast.pack()
        Lunch = tkinter.Button(self, text='Lunch?',command=lambda: webbrowser.open('https://www.foodnetwork.com/search/lunch-/COURSE_DFACET:0/tag%23meal-type:lunch'))
        Lunch.pack()
        Dinner = tkinter.Button(self, text='Dinner?',command=lambda: webbrowser.open('https://www.foodnetwork.com/healthy/packages/healthy-every-week/healthy-mains/healthy-weeknight-dinners'))
        Dinner.pack()
        Snack = tkinter.Button(self, text='Snack?',command=lambda: webbrowser.open('https://www.foodnetwork.com/search/snack-/COURSE_DFACET:0/tag%23meal-type:snack'))
        Snack.pack()
        Return22 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return22.pack()

        
class ProductivityOptions(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Accomplishing Today", font=LARGE_FONT)
        label.pack(pady=10,padx=10)  

        Homework = tkinter.Button(self, text='School? Stay Organized!',command=lambda: webbrowser.open('https://www.amazon.com/slp/planners-for-college-students/k6f77xpfpfohtp9'))
        Homework.pack()
        Chores = tkinter.Button(self, text='Chores?',command=lambda: webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        Chores.pack()
        Puzzles = tkinter.Button(self, text='Puzzle?',command=lambda: webbrowser.open('https://thejigsawpuzzles.com/'))
        Puzzles.pack()
        Return26 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return26.pack()


class WorkoutOptions(tkinter.Frame):
  def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Working Today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10) 

        Arms = tkinter.Button(self, text='Arms?',command=lambda: webbrowser.open('https://www.workout-generator.com/arm-workout.html'))
        Arms.pack()
        Legs = tkinter.Button(self, text='Legs?',command=lambda: webbrowser.open('https://www.workout-generator.com/leg-workout.html'))
        Legs.pack()
        Core = tkinter.Button(self, text='Core?',command=lambda: webbrowser.open('https://www.workout-generator.com/ab-workout.html'))
        Core.pack()
        Return30 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return30.pack()       




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


gui = MyGUI()
