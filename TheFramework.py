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

        for F in (StartPage, Category, NetflixOptions, MovieOptions, ActionMovie, RomanceMovie, HorrorMovie, ComedyMovie, DocumentaryMovie, ShowOptions, RealityShow,
                  ActionShow, RomanceShow, HorrorShow, ComedyShow, DocumentaryShow, MusicOptions, Country, Rock, Rap, RandB, LoFi, GamingOptions, CookingOptions,
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

        Netflix = tkinter.Button(self, text="Netflix", command=lambda: controller.show_frame(NetflixOptions))
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
        label = tkinter.Label(self, text="What Genre Are We Talking", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        ActionMovie = tkinter.Button(self, text='Action?',command=lambda: controller.show_frame(ActionMovie))
        ActionMovie.pack()
        RomanceMovie = tkinter.Button(self, text='Romance?',command=lambda: controller.show_frame(RomanceMovie))
        RomanceMovie.pack()
        HorrorMovie = tkinter.Button(self, text='Horror?',command=lambda: controller.show_frame(HorrorMovie))
        HorrorMovie.pack()
        ComedyMovie = tkinter.Button(self, text='Comedy?',command=lambda: controller.show_frame(ComedyMovie))
        ComedyMovie.pack()
        DocumentaryMovie = tkinter.Button(self, text='Documentary?',command=lambda: controller.show_frame(DocumentaryMovie))
        DocumentaryMovie.pack()
        Return2 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(NetflixOptions))
        Return2.pack()
        
class ActionMovie(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_action = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/1365?bc=34399'), height = 5, width = 15)
        #self.button_action.pack()
        Return3 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MovieOptions))
        Return3.pack() 

class RomanceMovie(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_romance = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/8883?bc=34399'), height = 5, width = 15)
        #self.button_romance.pack()
        Return4 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MovieOptions))
        Return4.pack() 

class HorrorMovie(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #self.button_horror = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/8711?bc=34399'), height = 5, width = 15)
        #self.button_horror.pack()
        Return5 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MovieOptions))
        Return5.pack() 

class ComedyMovie(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

       # self.button_comedy = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/6548?bc=34399'), height = 5, width = 15)
       # self.button_comedy.pack()
        Return6 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MovieOptions))
        Return6.pack() 

class DocumentaryMovie(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_documentary = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/2243108?bc=34399'), height = 5, width = 15)
        #self.button_documentary.pack()
        Return7 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MovieOptions))
        Return7.pack() 


class ShowOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        RealityShow = tkinter.Button(self, text='Reality?',command=lambda: controller.show_frame(RealityShow))
        RealityShow.pack()
        ActionShow = tkinter.Button(self, text='Action?',command=lambda: controller.show_frame(ActionShow))
        ActionShow.pack()
        RomanceShow = tkinter.Button(self, text='Romance?',command=lambda: controller.show_frame(RomanceShow))
        RomanceShow.pack()
        HorrorShow = tkinter.Button(self, text='Horror?',command=lambda: controller.show_frame(HorrorShow))
        HorrorShow.pack()
        ComedyShow = tkinter.Button(self, text='Comedy?',command=lambda: controller.show_frame(ComedyShow))
        ComedyShow.pack()
        DocumentaryMovie = tkinter.Button(self, text='Documentary?',command=lambda: controller.show_frame(DocumentaryShow))
        DocumentaryMovie.pack()
        Return8 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(NetflixOptions))
        Return8.pack()        

class RealityShow(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_reality_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/9833?bc=83'), height = 5, width = 15)
        #self.button_reality_show.pack()
        Return9 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ShowOptions))
        Return9.pack()

class ActionShow(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_action_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/10673?bc=83'), height = 5, width = 15)
        #self.button_action_show.pack()
        Return10 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ShowOptions))
        Return10.pack()

class RomanceShow(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_romance_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/26156?bc=83'), height = 5, width = 15)
        #self.button_romance_show.pack()
        Return11 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ShowOptions))
        Return11.pack()

class HorrorShow(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_horror_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/83059?bc=83'), height = 5, width = 15)
        #self.button_horror_show.pack()
        Return12 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ShowOptions))
        Return12.pack()

class ComedyShow(tkinter.Frame):
     def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)   

        #self.button_comedy_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/10375?bc=83'), height = 5, width = 15)
        #self.button_comedy_show.pack()
        Return13 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ShowOptions))
        Return13.pack()

class DocumentaryShow(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)   

        #self.button_documentary_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        #webbrowser.open('https://www.netflix.com/browse/genre/10105?bc=83'), height = 5, width = 15)
        #self.button_documentary_show.pack()
        Return14 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(ShowOptions))
        Return14.pack()

class MusicOptions(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Genre Are We Talking", font=LARGE_FONT)
        label.pack(pady=10,padx=10)  


        Country = tkinter.Button(self, text='Country?',command=lambda: controller.show_frame(Country))
        Country.pack()
        Rock = tkinter.Button(self, text='Rock?',command=lambda: controller.show_frame(Rock))
        Rock.pack()
        Rap = tkinter.Button(self, text='Rap?',command=lambda: controller.show_frame(Rap))
        Rap.pack()
        RandB = tkinter.Button(self, text='R&B?',command=lambda: controller.show_frame(RandB))
        RandB.pack()
        LoFi = tkinter.Button(self, text='Lo-Fi?',command=lambda: controller.show_frame(LoFi))
        LoFi.pack()
        Return15 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return15.pack()

class Country(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_country = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        #webbrowser.open('https://www.youtube.com/results?search_query=Luke+Combs'), height = 5, width = 25)
        #self.button_country.pack()
        Return16 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MusicOptions))
        Return16.pack()
        

class Rock(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #self.button_rock = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        #webbrowser.open('https://www.youtube.com/results?search_query=Paramore'), height = 5, width = 25)
        #self.button_rock.pack()
        Return17 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MusicOptions))
        Return17.pack()
    

class Rap(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_rap = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        #webbrowser.open('https://www.youtube.com/results?search_query=Tyler+the+Creator'), height = 5, width = 25)
        #self.button_rap.pack()
        Return18 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MusicOptions))
        Return18.pack()

class RandB(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_randb = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        #webbrowser.open('https://www.youtube.com/results?search_query=Michael+Jackson'), height = 5, width = 25)
        #self.button_randb.pack()
        Return19 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MusicOptions))
        Return19.pack()
        

class LoFi(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Good Choice!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #self.button_lofi = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        #webbrowser.open('https://www.youtube.com/results?search_query=slipfunc'), height = 5, width = 25)
        #self.button_lofi.pack()
        Return20 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(MusicOptions))
        Return20.pack()
    

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
        
        Breakfast = tkinter.Button(self, text='Breakfast?',command=lambda: controller.show_frame(Breakfast))
        Breakfast.pack()
        Lunch = tkinter.Button(self, text='Lunch?',command=lambda: controller.show_frame(Lunch))
        Lunch.pack()
        Dinner = tkinter.Button(self, text='Dinner?',command=lambda: controller.show_frame(Dinner))
        Dinner.pack()
        Snack = tkinter.Button(self, text='Snack?',command=lambda: controller.show_frame(Snack))
        Snack.pack()
        Return22 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return22.pack() 

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

class ProductivityOptions(tkinter.Frame):
   def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Accomplishing Today", font=LARGE_FONT)
        label.pack(pady=10,padx=10)  

        Homework = tkinter.Button(self, text='Homework?',command=lambda: controller.show_frame(Homework))
        Homework.pack()
        Chores = tkinter.Button(self, text='Chores?',command=lambda: controller.show_frame(Chores))
        Chores.pack()
        Puzzles = tkinter.Button(self, text='Puzzle?',command=lambda: controller.show_frame(Puzzles))
        Puzzles.pack()
        Return26 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return26.pack()

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

class WorkoutOptions(tkinter.Frame):
  def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="What Are You Interested In Working Today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10) 

        Arms = tkinter.Button(self, text='Arms?',command=lambda: controller.show_frame(Arms))
        Arms.pack()
        Legs = tkinter.Button(self, text='Legs?',command=lambda: controller.show_frame(Leg))
        Legs.pack()
        Core = tkinter.Button(self, text='Core?',command=lambda: controller.show_frame(Core))
        Core.pack()
        Return30 = tkinter.Button(self, text="Go Back", command=lambda: controller.show_frame(Category))
        Return30.pack()       


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


gui = MyGUI()
