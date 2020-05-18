import webbrowser
from tkinter import *
import tkinter as tkinter
import random
from PIL import Image, ImageTk

LARGE_FONT= ("Verdana", 12)

class MyGUI(tkinter.Tk):
    
    def __init__(self, *args, **kwargs):

        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Category, NetflixOptions, MovieOptions, ShowOptions, MusicOptions, GamingOptions, CookingOptions, ProductivityOptions,
                  WorkoutOptions, Puzzles):

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
       
        label = tkinter.Label(self, text="Click Here To Start Your Quarantine Adventure!", font=LARGE_FONT, bg="blue")
        label.pack(pady=100,padx=100)

        Categories = tkinter.Button(self, text="Quarantine Adventure!", command=lambda: controller.show_frame(Category))
        Categories.config(height = 10, width = 30)
        Categories.pack()

        self.fullScreenState = False
        controller.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = controller.winfo_screenwidth(), controller.winfo_screenheight()
        controller.geometry("%dx%d" % (self.w, self.h))

        self.config(bg='blue')

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
       
class Category(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Doing Today?", font=LARGE_FONT, bg="red")
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='red')

        Netflix = tkinter.Button(self, text="Netflix?", command=lambda: controller.show_frame(NetflixOptions))
        Netflix.config(height = 5, width = 30)
        Netflix.place(relx=.4, rely = .2, anchor= "c")

        Music = tkinter.Button(self, text="Music?", command=lambda: controller.show_frame(MusicOptions))
        Music.config(height = 5, width = 30)
        Music.place(relx=.6, rely = .2, anchor= "c")

        Gaming = tkinter.Button(self, text='Gaming?',command=lambda: controller.show_frame(GamingOptions))
        Gaming.config(height = 5, width = 30)
        Gaming.place(relx=.4, rely = .4, anchor= "c")

        Cooking = tkinter.Button(self, text='Cooking?',command=lambda: controller.show_frame(CookingOptions))
        Cooking.config(height = 5, width = 30)
        Cooking.place(relx=.6, rely = .4, anchor= "c")

        Productivity = tkinter.Button(self, text='Productivity?',command=lambda: controller.show_frame(ProductivityOptions))
        Productivity.config(height = 5, width = 30)
        Productivity.place(relx=.4, rely = .6, anchor= "c")

        Workout = tkinter.Button(self, text='Workout?',command=lambda: controller.show_frame(WorkoutOptions))
        Workout.config(height = 5, width = 30)
        Workout.place(relx=.6, rely = .6, anchor= "c")

        Quit1 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit1.config(height = 5, width = 30)
        Quit1.place(relx=.5, rely = .85, anchor= "c")
        


        
class NetflixOptions(tkinter.Frame):

    def __init__(self, parent, controller):
        
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Are You Feeling A Movie or Some Shows?", font=LARGE_FONT, bg='#E50914')
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='#E50914')

        Movie = tkinter.Button(self, text='Movies?',command=lambda: controller.show_frame(MovieOptions))
        Movie.config(height = 10, width = 30)
        Movie.place(relx=.4, rely = .4, anchor= "c")

        Show = tkinter.Button(self, text='Show?',command=lambda: controller.show_frame(ShowOptions))
        Show.config(height = 10, width = 30)
        Show.place(relx=.6, rely = .4, anchor= "c")

        Return1 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return1.config(height = 5, width = 30)
        Return1.place(relx=.5, rely = .65, anchor= "c")

        Quit2 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit2.config(height = 5, width = 30)
        Quit2.place(relx=.5, rely = .85, anchor= "c")

class MovieOptions(tkinter.Frame):
        
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking?", font=LARGE_FONT, bg='#0E84C8')
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='#0E84C8')

        ActionMovie = tkinter.Button(self, text='Action?', command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/1365?bc=34399'),
                                                                            controller.destroy()])
        ActionMovie.config(height = 5, width = 30)
        ActionMovie.place(relx=.4, rely = .2, anchor= "c")

        RomanceMovie = tkinter.Button(self, text='Romance?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/8883?bc=34399'),
                                                                             controller.destroy()])
        RomanceMovie.config(height = 5, width = 30)
        RomanceMovie.place(relx=.6, rely = .2, anchor= "c")

        HorrorMovie = tkinter.Button(self, text='Horror?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/8711?bc=34399'),
                                                                           controller.destroy()])
        HorrorMovie.config(height = 5, width = 30)
        HorrorMovie.place(relx=.4, rely = .35, anchor= "c")

        ComedyMovie = tkinter.Button(self, text='Comedy?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/6548?bc=34399'),
                                                                           controller.destroy()])
        ComedyMovie.config(height = 5, width = 30)
        ComedyMovie.place(relx=.6, rely = .35, anchor= "c")

        DocumentaryMovie = tkinter.Button(self, text='Documentary?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/2243108?bc=34399'),
                                                                                    controller.destroy()])
        DocumentaryMovie.config(height = 5, width = 30)
        DocumentaryMovie.place(relx=.5, rely = .5, anchor= "c")

        Return2 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(NetflixOptions))
        Return2.config(height = 5, width = 30)
        Return2.place(relx=.5, rely = .7, anchor= "c")

        Quit3 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit3.config(height = 5, width = 30)
        Quit3.place(relx=.5, rely = .85, anchor= "c")

class ShowOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking?", font=LARGE_FONT, bg='#FAFA01' )
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='#FAFA01')

        RealityShow = tkinter.Button(self, text='Reality?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/9833?bc=83'),
                                                                           controller.destroy()])
        RealityShow.config(height = 4, width = 30)
        RealityShow.place(relx=.4, rely = .2, anchor= "c")

        ActionShow = tkinter.Button(self, text='Action?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/10673?bc=83'),
                                                                         controller.destroy()])
        ActionShow.config(height = 4, width = 30)
        ActionShow.place(relx=.6, rely = .2, anchor= "c")

        RomanceShow = tkinter.Button(self, text='Romance?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/26156?bc=83'),
                                                                           controller.destroy()])
        RomanceShow.config(height = 4, width = 30)
        RomanceShow.place(relx=.4, rely = .35, anchor= "c")

        HorrorShow = tkinter.Button(self, text='Horror?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/83059?bc=83'),
                                                                         controller.destroy()])
        HorrorShow.config(height = 4, width = 30)
        HorrorShow.place(relx=.6, rely = .35, anchor= "c")

        ComedyShow = tkinter.Button(self, text='Comedy?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/10375?bc=83'),
                                                                         controller.destroy()])
        ComedyShow.config(height = 4, width = 30)
        ComedyShow.place(relx=.4, rely = .5, anchor= "c")

        DocumentaryShow = tkinter.Button(self, text='Documentary?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/10105?bc=83'),
                                                                                    controller.destroy()])
        DocumentaryShow.config(height = 4, width = 30)
        DocumentaryShow.place(relx=.6, rely = .5, anchor= "c")

        Return4 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(NetflixOptions))
        Return4.config(height = 3, width = 30)
        Return4.place(relx=.5, rely = .7, anchor= "c")

        Quit5 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit5.config(height = 3, width = 30)
        Quit5.place(relx=.5, rely = .85, anchor= "c")


class MusicOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking?", font=LARGE_FONT, bg='green')
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='green')


        Country = tkinter.Button(self, text='Country?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX1lVhptIYRda'),
                                                                       controller.destroy()])
        Country.config(height = 4, width = 30)
        Country.place(relx=.4, rely = .2, anchor= "c")

        Rock = tkinter.Button(self, text='Rock?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U'),
                                                                 controller.destroy()])
        Rock.config(height = 4, width = 30)
        Rock.place(relx=.6, rely = .2, anchor= "c")

        Rap = tkinter.Button(self, text='Rap?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd'),
                                                               controller.destroy()])
        Rap.config(height = 4, width = 30)
        Rap.place(relx=.4, rely = .35, anchor= "c")

        RandB = tkinter.Button(self, text='R&B?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX4SBhb3fqCJd'),
                                                                 controller.destroy()])
        RandB.config(height = 4, width = 30)
        RandB.place(relx=.6, rely = .35, anchor= "c")

        LoFi = tkinter.Button(self, text='Lo-Fi?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/0TCxLrp0tEZrkGkaWhnFrE'),
                                                                  controller.destroy()])
        LoFi.config(height = 4, width = 30)
        LoFi.place(relx=.5, rely = .5, anchor= "c")

        Return5 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return5.config(height = 5, width = 30)
        Return5.place(relx=.5, rely = .7, anchor= "c")

        Quit6 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit6.config(height = 5, width = 30)
        Quit6.place(relx=.5, rely = .85, anchor= "c")


class GamingOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Broswer Games or Suggest a Console Game?", font=LARGE_FONT, bg='purple')
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='purple')

        BrowserGames = tkinter.Button(self, text='Browser Games?',command=lambda:[webbrowser.open('https://www.miniclip.com/games/en/'),
                                                                  controller.destroy()])
        BrowserGames.config(height = 10, width = 30)
        BrowserGames.place(relx=.4, rely = .4, anchor= "c")
        
        ConsoleGames = tkinter.Button(self, text='Game Suggestion?',command=lambda:[webbrowser.open('https://apps.quanticfoundry.com/recommendations/gamerprofile/videogame/'),
                                                                  controller.destroy()])
        ConsoleGames.config(height = 10, width = 30)
        ConsoleGames.place(relx=.6, rely = .4, anchor= "c")

        Return6 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return6.config(height = 5, width = 30)
        Return6.place(relx=.5, rely = .7, anchor= "c")

        Quit7 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit7.config(height = 5, width = 30)
        Quit7.place(relx=.5, rely = .85, anchor= "c")       
        

    
class CookingOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What're You Wanting To Cook?", font=LARGE_FONT, bg='#4901FA')
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='#4901FA')
        
        Breakfast = tkinter.Button(self, text='Breakfast?',command=lambda:[webbrowser.open('https://www.foodnetwork.com/recipes/photos/our-best-breakfast-recipes'),
                                                                           controller.destroy()])
        Breakfast.config(height = 5, width = 30)
        Breakfast.place(relx=.4, rely = .25, anchor= "c")

        Lunch = tkinter.Button(self, text='Lunch?',command=lambda:[webbrowser.open('https://www.foodnetwork.com/search/lunch-/COURSE_DFACET:0/tag%23meal-type:lunch'),
                                                                   controller.destroy()])
        Lunch.config(height = 5, width = 30)
        Lunch.place(relx=.6, rely = .25, anchor= "c")

        Dinner = tkinter.Button(self, text='Dinner?',command=lambda:[webbrowser.open('https://www.foodnetwork.com/healthy/packages/healthy-every-week/healthy-mains/healthy-weeknight-dinners'),
                                                                     controller.destroy()])
        Dinner.config(height = 5, width = 30)
        Dinner.place(relx=.4, rely = .45, anchor= "c")

        Snack = tkinter.Button(self, text='Snack?',command=lambda:[webbrowser.open('https://www.foodnetwork.com/search/snack-/COURSE_DFACET:0/tag%23meal-type:snack'),
                                                                   controller.destroy()])
        Snack.config(height = 5, width = 30)
        Snack.place(relx=.6, rely = .45, anchor= "c")

        Return7 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return7.config(height = 5, width = 30)
        Return7.place(relx=.5, rely = .7, anchor= "c")

        Quit8 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit8.config(height = 5, width = 30)
        Quit8.place(relx=.5, rely = .85, anchor= "c")

class ProductivityOptions(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Accomplishing Today?", font=LARGE_FONT, bg='silver')
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='silver')

        Homework = tkinter.Button(self, text='School? Stay Organized!',command=lambda:[webbrowser.open('https://www.amazon.com/slp/planners-for-college-students/k6f77xpfpfohtp9'),
                                                                                       controller.destroy()])
        Homework.config(height = 8, width = 30)
        Homework.place(relx=.4, rely = .3, anchor= "c")

        Chores = tkinter.Button(self, text='Chores?',command=lambda:[webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
                                                                     controller.destroy()])
        Chores.config(height = 8, width = 30)
        Chores.place(relx=.6, rely = .3, anchor= "c")

        Puzzle = tkinter.Button(self, text='Puzzles?',command=lambda: controller.show_frame(Puzzles))
        Puzzle.config(height = 8, width = 30)
        Puzzle.place(relx=.5, rely = .5, anchor= "c")

        Return8 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return8.config(height = 5, width = 30)
        Return8.place(relx=.5, rely = .7, anchor= "c")

        Quit9 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit9.config(height = 5, width = 30)
        Quit9.place(relx=.5, rely = .85, anchor= "c")

class Puzzles(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Accomplishing Today?", font=LARGE_FONT, bg='SpringGreen2')
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='SpringGreen2')

        Sudoku = tkinter.Button(self, text='Sudoku?',command=lambda:[webbrowser.open('https://sudoku.com/'),
                                                                                       controller.destroy()])
        Sudoku.config(height = 8, width = 30)
        Sudoku.place(relx=.4, rely = .3, anchor= "c")

        Jigsaw = tkinter.Button(self, text='Jigsaw Puzzle?',command=lambda:[webbrowser.open('https://thejigsawpuzzles.com/'),
                                                                     controller.destroy()])
        Jigsaw.config(height = 8, width = 30)
        Jigsaw.place(relx=.6, rely = .3, anchor= "c")

        Nonograms = tkinter.Button(self, text='Nonograms?',command=lambda:[webbrowser.open('https://www.puzzle-nonograms.com/'),
                                                                     controller.destroy()])
        Nonograms.config(height = 8, width = 30)
        Nonograms.place(relx=.5, rely = .5, anchor= "c")

        Return9 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ProductivityOptions))
        Return9.config(height = 5, width = 30)
        Return9.place(relx=.5, rely = .7, anchor= "c")

        Quit10 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit10.config(height = 5, width = 30)
        Quit10.place(relx=.5, rely = .85, anchor= "c")

class WorkoutOptions(tkinter.Frame):
  def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Working Today?", font=LARGE_FONT, bg='orange')
        label.place(relx=.5, rely = .1,anchor ="c")

        self.config(bg='orange')

        Arms = tkinter.Button(self, text='Arms?',command=lambda:[webbrowser.open('https://www.workout-generator.com/arm-workout.html'),
                                                                 controller.destroy()])
        Arms.config(height = 8, width = 30)
        Arms.place(relx=.4, rely = .3, anchor= "c")

        Legs = tkinter.Button(self, text='Legs?',command=lambda:[webbrowser.open('https://www.workout-generator.com/leg-workout.html'),
                                                                 controller.destroy()])
        Legs.config(height = 8, width = 30)
        Legs.place(relx=.6, rely = .3, anchor= "c")

        Core = tkinter.Button(self, text='Core?',command=lambda:[webbrowser.open('https://www.workout-generator.com/ab-workout.html'),
                                                                 controller.destroy()])
        Core.config(height = 8, width = 30)
        Core.place(relx=.5, rely = .5, anchor= "c")

        Return10 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return10.config(height = 5, width = 30)
        Return10.place(relx=.5, rely = .7, anchor= "c")

        Quit11 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit11.config(height = 5, width = 30)
        Quit11.place(relx=.5, rely = .85, anchor= "c")

gui = MyGUI()
