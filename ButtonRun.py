import webbrowser
from tkinter import *
import tkinter as tkinter
import random

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.fullScreenState = False 
        self.main_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()
        self.main_window.geometry("%dx%d" % (self.w, self.h))        

        self.button1 = tkinter.Button(self.main_window,text='Click Here To Start Your Quarantine Adventure!',command=self.Category, height = 15)
        self.button1.pack()
        tkinter.mainloop()


    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    
    def Category(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))

        self.avg_mess = tkinter.Label(self.mini_window,text='What Are You Interested In Doing Today?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button2 = tkinter.Button(self.mini_window,text='Netflix?',command=self.NetflixOptions, height = 5, width = 15)
        self.button2.pack()
        self.button3 = tkinter.Button(self.mini_window,text='Music?',command=self.MusicOptions, height = 5, width = 15)
        self.button3.pack()
        self.button4 = tkinter.Button(self.mini_window,text='Gaming?',command=self.GamingOptions, height = 5, width = 15)
        self.button4.pack()
        self.button5 = tkinter.Button(self.mini_window,text='Cooking?',command=self.CookingOptions, height = 5, width = 15)
        self.button5.pack()
        self.button6 = tkinter.Button(self.mini_window,text='Productivity?',command=self.ProductivityOptions, height = 5, width = 15)
        self.button6.pack()
        self.button7 = tkinter.Button(self.mini_window,text='Workout?',command=self.WorkoutOptions, height = 5, width = 15)
        self.button7.pack()

        
    def NetflixOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Show or Movie?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button8 = tkinter.Button(self.mini_window,text='Show',command=self.ShowOptions, height = 5, width = 15)
        self.button8.pack()
        self.button9 = tkinter.Button(self.mini_window,text='Movie',command=self.MovieOptions, height = 5, width = 15)
        self.button9.pack()

    def MovieOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='What Genre Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button10 = tkinter.Button(self.mini_window,text='Action',command=self.ActionMovieOptions, height = 5, width = 15)
        self.button10.pack()
        self.button11 = tkinter.Button(self.mini_window,text='Romance',command=self.RomanceMovieOptions, height = 5, width = 15)
        self.button11.pack()
        self.button12 = tkinter.Button(self.mini_window,text='Horror',command=self.HorrorMovieOptions, height = 5, width = 15)
        self.button12.pack()
        self.button13 = tkinter.Button(self.mini_window,text='Comedy',command=self.ComedyMovieOptions, height = 5, width = 15)
        self.button13.pack()
        self.button14 = tkinter.Button(self.mini_window,text='Documentary',command=self.DocumentaryMovieOptions, height = 5, width = 15)
        self.button14.pack()
        
    def ActionMovieOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_action = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/1365?bc=34399'), height = 5, width = 15)
        self.button_action.pack()

    def RomanceMovieOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_romance = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/8883?bc=34399'), height = 5, width = 15)
        self.button_romance.pack()

    def HorrorMovieOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_horror = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/8711?bc=34399'), height = 5, width = 15)
        self.button_horror.pack()

    def ComedyMovieOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_comedy = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/6548?bc=34399'), height = 5, width = 15)
        self.button_comedy.pack()

    def DocumentaryMovieOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_documentary = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/2243108?bc=34399'), height = 5, width = 15)
        self.button_documentary.pack()


    def ShowOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='What Genre Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button15 = tkinter.Button(self.mini_window,text='Reality',command=self.RealityShowOptions, height = 5, width = 15)
        self.button15.pack()
        self.button16 = tkinter.Button(self.mini_window,text='Action',command=self.ActionShowOptions, height = 5, width = 15)
        self.button16.pack()
        self.button17 = tkinter.Button(self.mini_window,text='Romance',command=self.RomanceShowOptions, height = 5, width = 15)
        self.button17.pack()
        self.button18 = tkinter.Button(self.mini_window,text='Horror',command=self.HorrorShowOptions, height = 5, width = 15)
        self.button18.pack()
        self.button19 = tkinter.Button(self.mini_window,text='Comedy',command=self.ComedyShowOptions, height = 5, width = 15)
        self.button19.pack()
        self.button20 = tkinter.Button(self.mini_window,text='Documentary',command=self.DocumentaryShowOptions, height = 5, width = 15)
        self.button20.pack()

    def RealityShowOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_reality_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/9833?bc=83'), height = 5, width = 15)
        self.button_reality_show.pack()

    def ActionShowOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_action_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/10673?bc=83'), height = 5, width = 15)
        self.button_action_show.pack()

    def RomanceShowOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_romance_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/26156?bc=83'), height = 5, width = 15)
        self.button_romance_show.pack()

    def HorrorShowOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_horror_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/83059?bc=83'), height = 5, width = 15)
        self.button_horror_show.pack()

    def ComedyShowOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_comedy_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/10375?bc=83'), height = 5, width = 15)
        self.button_comedy_show.pack()

    def DocumentaryShowOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_documentary_show = tkinter.Button(self.mini_window, text='You Should Watch...', command= lambda:
        webbrowser.open('https://www.netflix.com/browse/genre/10105?bc=83'), height = 5, width = 15)
        self.button_documentary_show.pack()

    def MusicOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='What Genre Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button21 = tkinter.Button(self.mini_window,text='Country',command=self.CountryOptions, height = 5, width = 15)
        self.button21.pack()
        self.button22 = tkinter.Button(self.mini_window,text='Rock',command=self.RockOptions, height = 5, width = 15)
        self.button22.pack()
        self.button23 = tkinter.Button(self.mini_window,text='Rap',command=self.RapOptions, height = 5, width = 15)
        self.button23.pack()
        self.button24 = tkinter.Button(self.mini_window,text='R&B',command=self.RandBOptions, height = 5, width = 15)
        self.button24.pack()
        self.button25 = tkinter.Button(self.mini_window,text='Lo-Fi',command=self.LoFiOptions, height = 5, width = 15)
        self.button25.pack()

    def CountryOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_country = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        webbrowser.open('https://www.youtube.com/results?search_query=Luke+Combs'), height = 5, width = 15)
        self.button_country.pack()
        

    def RockOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_rock = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        webbrowser.open('https://www.youtube.com/results?search_query=Paramore'), height = 5, width = 15)
        self.button_rock.pack()
    

    def RapOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_rap = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        webbrowser.open('https://www.youtube.com/results?search_query=Tyler+the+Creator'), height = 5, width = 15)
        self.button_rap.pack()

    def RandBOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
    
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_randb = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        webbrowser.open('https://www.youtube.com/results?search_query=Michael+Jackson'), height = 5, width = 15)
        self.button_randb.pack()
        

    def LoFiOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_lofi = tkinter.Button(self.mini_window, text='You Should Listen To...', command= lambda:
        webbrowser.open('https://www.youtube.com/results?search_query=slipfunc'), height = 5, width = 15)
        self.button_lofi.pack()
    

    def GamingOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='What Kind of Games Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button26 = tkinter.Button(self.mini_window,text='Preloaded PyGames?',command=self.PyGamesOptions, height = 5, width = 15)
        self.button26.pack
        self.button27 = tkinter.Button(self.mini_window,text='Something Homemade',command=self.HomemadeOptions, height = 5, width = 15)
        self.button27.pack()

    def PyGamesOptions(self):
        tkinter.messagebox.showinfo("We need to figure out how to load PyGames to pop up here.")

    def HomemadeOptions(self):
        tkinter.messagebox.showinfo("We need to figure out how to load Anassass' Game to pop up here.")

    
    def CookingOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='What Are You Interested In Cooking Today?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button28 = tkinter.Button(self.mini_window,text='Breakfast?',command=self.BreakfastOptions, height = 5, width = 15)
        self.button28.pack()
        self.button29 = tkinter.Button(self.mini_window,text='Lunch?',command=self.LunchOptions, height = 5, width = 15)
        self.button29.pack()
        self.button30 = tkinter.Button(self.mini_window,text='Dinner?',command=self.DinnerOptions, height = 5, width = 15)
        self.button30.pack()
        self.button31 = tkinter.Button(self.mini_window,text='Snack?',command=self.SnackOptions, height = 5, width = 15)
        self.button31.pack()

    def BreakfastOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_breakfast = tkinter.Button(self.mini_window, text='You Should Cook...', command= lambda:
        webbrowser.open('https://www.scoopwhoop.com/food/16-healthy-3-ingredient-breakfast-recipes-to-try-out-while-in-quarantine/'), height = 5, width = 15)
        self.button_breakfast.pack()

    def LunchOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_lunch = tkinter.Button(self.mini_window, text='You Should Cook...', command= lambda:
        webbrowser.open('https://www.tasteofhome.com/collection/creative-quarantine-meals/'), height = 5, width = 15)
        self.button_lunch.pack()

    def DinnerOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_dinner = tkinter.Button(self.mini_window, text='You Should Cook...', command= lambda:
        webbrowser.open('https://www.eatthis.com/quarantine-recipes/'), height = 5, width = 15)
        self.button_dinner.pack()
        

    def SnackOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_snack = tkinter.Button(self.mini_window, text='You Should Cook...', command= lambda:
        webbrowser.open('https://health.ucdavis.edu/good-food/recipes/healthy-snacks-covid-19.html'), height = 5, width = 15)
        self.button_snack.pack()

    def ProductivityOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='What Are You Interested In Doing Today?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button32 = tkinter.Button(self.mini_window,text='Homework?',command=self.Homework, height = 5, width = 15)
        self.button32.pack()
        self.button33 = tkinter.Button(self.mini_window,text='Chores?',command=self.Chores, height = 5, width = 15)
        self.button33.pack()
        self.button34 = tkinter.Button(self.mini_window,text='Puzzle?',command=self.Puzzle, height = 5, width = 15)
        self.button34.pack()

    def Homework(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Yeah, go do that....')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_homework = tkinter.Button(self.mini_window, text='You Should Work On...', command= lambda:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'), height = 5, width = 15)
        self.button_homework.pack()
    
    def Chores(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='You Do Not Want Everyone Yelling At You. Go, But Come Back When You Finish!')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_chores = tkinter.Button(self.mini_window, text='You Should Clean...', command= lambda:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'), height = 5, width = 15)
        self.button_chores.pack()

    def Puzzle(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Go Do Some Brain Exercises!!')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button_puzzle = tkinter.Button(self.mini_window, text='You Should Try...', command= lambda:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ'), height = 5, width = 15)
        self.button_puzzle.pack()

    def WorkoutOptions(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='What Are You Interested In Working Today?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

        self.button35 = tkinter.Button(self.mini_window,text='Arms?',command=self.ArmsWorkouts, height = 5, width = 15)
        self.button35.pack()
        self.button36 = tkinter.Button(self.mini_window,text='Legs?',command=self.LegWorkouts, height = 5, width = 15)
        self.button36.pack()
        self.button37 = tkinter.Button(self.mini_window,text='Core?',command=self.CoreWorkouts, height = 5, width = 15)
        self.button37.pack()        


    def ArmsWorkouts(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button_arms = tkinter.Button(self.mini_window, text='You Should Do This Workout...', command= lambda:
        webbrowser.open('https://www.workout-generator.com/arm-workout.html'), height = 5, width = 15)
        self.button_arms.pack()

    def LegWorkouts(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button_legs = tkinter.Button(self.mini_window, text='You Should Do This Workout...', command= lambda:
        webbrowser.open('https://www.workout-generator.com/leg-workout.html'), height = 5, width = 15)
        self.button_legs.pack()

    def CoreWorkouts(self):
        self.mini_window = tkinter.Toplevel()

        self.fullScreenState = False 
        self.mini_window.attributes('-fullscreen', self.fullScreenState)
        self.w, self.h = self.mini_window.winfo_screenwidth(), self.mini_window.winfo_screenheight()
        self.mini_window.geometry("%dx%d" % (self.w, self.h))
        
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button_core = tkinter.Button(self.mini_window, text='You Should Do This Workout...', command= lambda:
        webbrowser.open('https://www.workout-generator.com/ab-workout.html'), height = 5, width = 15)
        self.button_core.pack()


gui = MyGUI()
