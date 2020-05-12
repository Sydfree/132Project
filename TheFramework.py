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

        StartPhoto = Image.open('Images/maxresdefault.gif')
        tk_image = ImageTk.PhotoImage(StartPhoto)

        label = tkinter.Label(self, text="Click Here To Start Your Quarantine Adventure!", image=tk_image,
                              compound='center', font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Categories = tkinter.Button(self, text="Quarantine Adventure!", command=lambda: controller.show_frame(Category))
        Categories.pack()

        self.fullScreenState = False
        controller.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = controller.winfo_screenwidth(), controller.winfo_screenheight()
        controller.geometry("%dx%d" % (self.w, self.h))

        #self.config(bg='blue')

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
       
class Category(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Doing Today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='red')

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

        Quit1 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit1.pack()
        


        
class NetflixOptions(tkinter.Frame):

    def __init__(self, parent, controller):
        
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Are You Feeling A Movie or Some Shows?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='#E50914')

        Movie = tkinter.Button(self, text='Movies?',command=lambda: controller.show_frame(MovieOptions))
        Movie.pack()

        Show = tkinter.Button(self, text='Show?',command=lambda: controller.show_frame(ShowOptions))
        Show.pack()

        Return1 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return1.pack()

        Quit2 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit2.pack()

class MovieOptions(tkinter.Frame):
        
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='black')

        ActionMovie = tkinter.Button(self, text='Action?', command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/1365?bc=34399'),
                                                                            controller.destroy()])
        ActionMovie.pack()

        RomanceMovie = tkinter.Button(self, text='Romance?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/8883?bc=34399'),
                                                                             controller.destroy()])
        RomanceMovie.pack()

        HorrorMovie = tkinter.Button(self, text='Horror?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/8711?bc=34399'),
                                                                           controller.destroy()])
        HorrorMovie.pack()

        ComedyMovie = tkinter.Button(self, text='Comedy?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/6548?bc=34399'),
                                                                           controller.destroy()])
        ComedyMovie.pack()

        DocumentaryMovie = tkinter.Button(self, text='Documentary?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/2243108?bc=34399'),
                                                                                    controller.destroy()])
        DocumentaryMovie.pack()

        Return2 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(NetflixOptions))
        Return2.pack()

        Quit3 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit3.pack()

class ShowOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='gold')

        RealityShow = tkinter.Button(self, text='Reality?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/9833?bc=83'),
                                                                           controller.destroy()])
        RealityShow.pack()

        ActionShow = tkinter.Button(self, text='Action?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/10673?bc=83'),
                                                                         controller.destroy()])
        ActionShow.pack()

        RomanceShow = tkinter.Button(self, text='Romance?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/26156?bc=83'),
                                                                           controller.destroy()])
        RomanceShow.pack()

        HorrorShow = tkinter.Button(self, text='Horror?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/83059?bc=83'),
                                                                         controller.destroy()])
        HorrorShow.pack()

        ComedyShow = tkinter.Button(self, text='Comedy?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/10375?bc=83'),
                                                                         controller.destroy()])
        ComedyShow.pack()

        DocumentaryMovie = tkinter.Button(self, text='Documentary?',command=lambda:[webbrowser.open('https://www.netflix.com/browse/genre/10105?bc=83'),
                                                                                    controller.destroy()])
        DocumentaryMovie.pack()

        Return4 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(NetflixOptions))
        Return4.pack()

        Quit5 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit5.pack()


class MusicOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='green')


        Country = tkinter.Button(self, text='Country?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX1lVhptIYRda'),
                                                                       controller.destroy()])
        Country.pack()

        Rock = tkinter.Button(self, text='Rock?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U'),
                                                                 controller.destroy()])
        Rock.pack()

        Rap = tkinter.Button(self, text='Rap?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd'),
                                                               controller.destroy()])
        Rap.pack()

        RandB = tkinter.Button(self, text='R&B?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DX4SBhb3fqCJd'),
                                                                 controller.destroy()])
        RandB.pack()

        LoFi = tkinter.Button(self, text='Lo-Fi?',command=lambda:[webbrowser.open('https://open.spotify.com/playlist/0TCxLrp0tEZrkGkaWhnFrE'),
                                                                  controller.destroy()])
        LoFi.pack()

        Return5 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return5.pack()

        Quit6 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit6.pack()


class GamingOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Broswer Games or Suggest a Console Game?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='purple')

        BrowserGames = tkinter.Button(self, text='Browser Games?',command=lambda:[webbrowser.open('https://www.miniclip.com/games/en/'),
                                                                  controller.destroy()])
        BrowserGames.pack()
        
        ConsoleGames = tkinter.Button(self, text='Game Suggestion?',command=lambda:[webbrowser.open('https://apps.quanticfoundry.com/recommendations/gamerprofile/videogame/'),
                                                                  controller.destroy()])
        ConsoleGames.pack()

        Return6 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return6.pack()

        Quit7 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit7.pack()        
        

    
class CookingOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What're You Wanting To Cook?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='yellow')
        
        Breakfast = tkinter.Button(self, text='Breakfast?',command=lambda:[webbrowser.open('https://www.foodnetwork.com/recipes/photos/our-best-breakfast-recipes'),
                                                                           controller.destroy()])
        Breakfast.pack()

        Lunch = tkinter.Button(self, text='Lunch?',command=lambda:[webbrowser.open('https://www.foodnetwork.com/search/lunch-/COURSE_DFACET:0/tag%23meal-type:lunch'),
                                                                   controller.destroy()])
        Lunch.pack()

        Dinner = tkinter.Button(self, text='Dinner?',command=lambda:[webbrowser.open('https://www.foodnetwork.com/healthy/packages/healthy-every-week/healthy-mains/healthy-weeknight-dinners'),
                                                                     controller.destroy()])
        Dinner.pack()

        Snack = tkinter.Button(self, text='Snack?',command=lambda:[webbrowser.open('https://www.foodnetwork.com/search/snack-/COURSE_DFACET:0/tag%23meal-type:snack'),
                                                                   controller.destroy()])
        Snack.pack()

        Return22 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return22.pack()

        Quit6 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit6.pack()

class ProductivityOptions(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Accomplishing Today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='silver')

        Homework = tkinter.Button(self, text='School? Stay Organized!',command=lambda:[webbrowser.open('https://www.amazon.com/slp/planners-for-college-students/k6f77xpfpfohtp9'),
                                                                                       controller.destroy()])
        Homework.pack()

        Chores = tkinter.Button(self, text='Chores?',command=lambda:[webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
                                                                     controller.destroy()])
        Chores.pack()

        Puzzle = tkinter.Button(self, text='Puzzles?',command=lambda: controller.show_frame(Puzzles))
        Puzzle.pack()

        Return7 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return7.pack()

        Quit8 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit8.pack()

class Puzzles(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Accomplishing Today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='green')

        Sudoku = tkinter.Button(self, text='Sudoku?',command=lambda:[webbrowser.open('https://sudoku.com/'),
                                                                                       controller.destroy()])
        Sudoku.pack()

        Jigsaw = tkinter.Button(self, text='Jigsaw Puzzle?',command=lambda:[webbrowser.open('https://thejigsawpuzzles.com/'),
                                                                     controller.destroy()])
        Jigsaw.pack()

        Nonograms = tkinter.Button(self, text='Nonograms',command=lambda:[webbrowser.open('https://www.puzzle-nonograms.com/'),
                                                                     controller.destroy()])
        Nonograms.pack()        

        Return7 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return7.pack()

        Quit8 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit8.pack()

class WorkoutOptions(tkinter.Frame):
  def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Working Today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.config(bg='orange')

        Arms = tkinter.Button(self, text='Arms?',command=lambda:[webbrowser.open('https://www.workout-generator.com/arm-workout.html'),
                                                                 controller.destroy()])
        Arms.pack()

        Legs = tkinter.Button(self, text='Legs?',command=lambda:[webbrowser.open('https://www.workout-generator.com/leg-workout.html'),
                                                                 controller.destroy()])
        Legs.pack()

        Core = tkinter.Button(self, text='Core?',command=lambda:[webbrowser.open('https://www.workout-generator.com/ab-workout.html'),
                                                                 controller.destroy()])
        Core.pack()

        Return8 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return8.pack()

        Quit9 = tkinter.Button(self, text="Click to Quit", command = controller.destroy)
        Quit9.pack()

gui = MyGUI()
