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

        Quit = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit.pack()
        


        
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

        Quit1 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit1.pack()

class MovieOptions(tkinter.Frame):
        
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

<<<<<<< HEAD
        ActionMovie = tkinter.Button(self, text='Action?', command=lambda: [webbrowser.open('https://www.netflix.com/browse/genre/1365?bc=34399'), \
                                                                            controller.destroy])
=======
        ActionMovie = tkinter.Button(self, text='Action?',command=lambda: webbrowser.open('https://www.netflix.com/browse/genre/1365?bc=34399'))
>>>>>>> 6ac0f9d61d31f66cc84f368bd3747a788c67a84c
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

        Quit2 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit2.pack()

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

        Quit3 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit3.pack()


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

        Quit4 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit4.pack()


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
<<<<<<< HEAD

        Quit5 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit5.pack()

class Breakfast(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_breakfast = tkinter.Button(self.mini_window, text='You Should Cook...', command= lambda:
        #webbrowser.open('https://www.scoopwhoop.com/food/16-healthy-3-ingredient-breakfast-recipes-to-try-out-while-in-quarantine/'), height = 5, width = 15)
        #self.button_breakfast.pack()
        Return22 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(CookingOptions))
        Return22.pack() 

class Lunch(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_lunch = tkinter.Button(self.mini_window, text='You Should Cook...', command= lambda:
        #webbrowser.open('https://www.tasteofhome.com/collection/creative-quarantine-meals/'), height = 5, width = 15)
        #self.button_lunch.pack()

        Return23 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(CookingOptions))
        Return23.pack()

        Quit6 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit6.pack()

class Dinner(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_dinner = tkinter.Button(self.mini_window, text='You Should Cook...', command= lambda:
        #webbrowser.open('https://www.eatthis.com/quarantine-recipes/'), height = 5, width = 15)
        #self.button_dinner.pack()

        Return24 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(CookingOptions))
        Return24.pack()

        Quit7 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit7.pack()        

class Snack(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        #self.button_snack = tkinter.Button(self.mini_window, text='You Should Cook...', command= lambda:
        #webbrowser.open('https://health.ucdavis.edu/good-food/recipes/healthy-snacks-covid-19.html'), height = 5, width = 15)
        #self.button_snack.pack()

        Return25 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(CookingOptions))
        Return25.pack()

        Quit8 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit8.pack()

=======

        
>>>>>>> 6ac0f9d61d31f66cc84f368bd3747a788c67a84c
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

<<<<<<< HEAD
        Quit9 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit9.pack()

class Homework(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_homework = tkinter.Button(self.mini_window, text='You Should Work On...', command= lambda:
        #webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'), height = 5, width = 25)
        #self.button_homework.pack()
        Return27 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ProductivityOptions))
        Return27.pack()
    
class Chores(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_chores = tkinter.Button(self.mini_window, text='You Should Clean...', command= lambda:
        #webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'), height = 5, width = 15)
        #self.button_chores.pack()

        Return28 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ProductivityOptions))
        Return28.pack()

        Quit10 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit10.pack()

class Puzzle(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_puzzle = tkinter.Button(self.mini_window, text='You Should Try...', command= lambda:
        #webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'), height = 5, width = 15)
        #self.button_puzzle.pack()

        Return29 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ProductivityOptions))
        Return29.pack()
=======
>>>>>>> 6ac0f9d61d31f66cc84f368bd3747a788c67a84c

        Quit11 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit11.pack()

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

        Quit12 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit12.pack()


<<<<<<< HEAD
class Arms(tkinter.Frame):
  def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #self.button_arms = tkinter.Button(self.mini_window, text='You Should Do This Workout...', command= lambda:
        #webbrowser.open('https://www.workout-generator.com/arm-workout.html'), height = 5, width = 25)
        #self.button_arms.pack()

        Return30 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(WorkoutOptions))
        Return30.pack()

        Quit13 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit13.pack()

class Leg(tkinter.Frame):
  def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #self.button_legs = tkinter.Button(self.mini_window, text='You Should Do This Workout...', command= lambda:
        #webbrowser.open('https://www.workout-generator.com/leg-workout.html'), height = 5, width = 25)
        #self.button_legs.pack()

        Return31 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(WorkoutOptions))
        Return31.pack()

        Quit14 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit14.pack()

class Core(tkinter.Frame):
  def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #self.button_core = tkinter.Button(self.mini_window, text='You Should Do This Workout...', command= lambda:
        #webbrowser.open('https://www.workout-generator.com/ab-workout.html'), height = 5, width = 25)
        #self.button_core.pack()

        Return32 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(WorkoutOptions))
        Return32.pack()

        Quit15 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit15.pack()
        

=======
>>>>>>> 6ac0f9d61d31f66cc84f368bd3747a788c67a84c
gui = MyGUI()
