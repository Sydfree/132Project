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

        for F in (StartPage, Category, NetflixOptions, MovieOptions, ShowOptions, MusicOptions, GamingOptions, CookingOptions,
                  Breakfast, Lunch, Dinner, Snack, ProductivityOptions, Homework, Chores, Puzzle, WorkoutOptions, Arms, Leg, Core):

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

        Return21 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return21.pack()
        

    
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


gui = MyGUI()
