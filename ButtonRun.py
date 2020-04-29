##import tkinter as tk
##import tkinter.messagebox
##
##top = tk.Tk()
##
##def helloCallBack():
##    tkinter.messagebox.showinfo("Hello Python", "Hello World")
##    
##
##B = tkinter.Button(top, text = "Hello", command = helloCallBack)
##C = tkinter.Button(top, text = "Test", command = helloCallBack)
##
##B.pack()
##C.pack()
##top.mainloop()

import tkinter as tkinter
import random
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.button1 = tkinter.Button(self.main_window,text='Click Here To Start Your Quarantine Adventure!',command=self.Category)
        self.button1.pack()
        tkinter.mainloop()
        
    def Category(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Are You Interested In Doing Today?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button2 = tkinter.Button(self.mini_window,text='Netflix?',command=self.NetflixOptions)
        self.button2.pack()
        self.button3 = tkinter.Button(self.mini_window,text='Music?',command=self.MusicOptions)
        self.button3.pack()
        self.button4 = tkinter.Button(self.mini_window,text='Gaming?',command=self.GamingOptions)
        self.button4.pack()
        self.button5 = tkinter.Button(self.mini_window,text='Cooking?',command=self.CookingOptions)
        self.button5.pack()
        self.button6 = tkinter.Button(self.mini_window,text='Productivity?',command=self.ProductivityOptions)
        self.button6.pack()
        self.button7 = tkinter.Button(self.mini_window,text='Workout?',command=self.WorkoutOptions)
        self.button7.pack()

        
    def NetflixOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Show or Movie?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button8 = tkinter.Button(self.mini_window,text='Show',command=self.ShowOptions)
        self.button8.pack()
        self.button9 = tkinter.Button(self.mini_window,text='Movie',command=self.MovieOptions)
        self.button9.pack()

    def MovieOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Genre Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button10 = tkinter.Button(self.mini_window,text='Reality',command=self.RealityMovieOptions)
        self.button10.pack()
        self.button11 = tkinter.Button(self.mini_window,text='Action',command=self.ActionMovieOptions)
        self.button11.pack()
        self.button12 = tkinter.Button(self.mini_window,text='Romance',command=self.RomanceMovieOptions)
        self.button12.pack()
        self.button13 = tkinter.Button(self.mini_window,text='Horror',command=self.HorrorMovieOptions)
        self.button13.pack()
        self.button14 = tkinter.Button(self.mini_window,text='Comedy',command=self.ComedyMovieOptions)
        self.button14.pack
        self.button15 = tkinter.Button(self.mini_window,text='Documentary',command=self.DocumentaryMovieOptions)
        self.button15.pack()
        
    

     

    def RealityMovieOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def ActionMovieOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def RomanceMovieOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def HorrorMovieOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def ComedyMovieOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def DocumentaryMovieOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()


    def ShowOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Genre Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button16 = tkinter.Button(self.mini_window,text='Reality',command=self.RealityShowOptions)
        self.button16.pack()
        self.button17 = tkinter.Button(self.mini_window,text='Action',command=self.ActionShowOptions)
        self.button17.pack()
        self.button18 = tkinter.Button(self.mini_window,text='Romance',command=self.RomanceShowOptions)
        self.button18.pack()
        self.button19 = tkinter.Button(self.mini_window,text='Horror',command=self.HorrorShowOptions)
        self.button19.pack()
        self.button20 = tkinter.Button(self.mini_window,text='Comedy',command=self.ComedyShowOptions)
        self.button20.pack
        self.button21 = tkinter.Button(self.mini_window,text='Documentary',command=self.DocumentaryShowOptions)
        self.button21.pack()

    def RealityShowOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def ActionShowOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def RomanceShowOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def HorrorShowOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def ComedyShowOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def DocumentaryShowOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Watch...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def MusicOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Genre Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button22 = tkinter.Button(self.mini_window,text='Country',command=self.CountryOptions)
        self.button22.pack()
        self.button23 = tkinter.Button(self.mini_window,text='Rock',command=self.RockOptions)
        self.button23.pack()
        self.button24 = tkinter.Button(self.mini_window,text='Rap',command=self.RapOptions)
        self.button24.pack()
        self.button25 = tkinter.Button(self.mini_window,text='R&B',command=self.RandBOptions)
        self.button25.pack()

    def CountryOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def RockOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Kind of Rock Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button26 = tkinter.Button(self.mini_window,text='Classic',command=self.ClassicOptions)
        self.button26.pack
        self.button27 = tkinter.Button(self.mini_window,text='Alternative',command=self.AlternativeOptions)
        self.button27.pack()

    def ClassicOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def AlternativeOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def RapOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def RandBOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def GamingOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Kind of Games Are We Talking?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button28 = tkinter.Button(self.mini_window,text='Preloaded PyGames?',command=self.PyGamesOptions)
        self.button28.pack
        self.button29 = tkinter.Button(self.mini_window,text='Something Homemade',command=self.HomemadeOptions)
        self.button29.pack()

    def PyGamesOptions(self):
        tkinter.messagebox.showinfo("We need to figure out how to load PyGames to pop up here.")

    def HomemadeOptions(self):
        tkinter.messagebox.showinfo("We need to figure out how to load Anassass' Game to pop up here.")

    
    def CookingOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Are You Interested In Cooking Today?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button30 = tkinter.Button(self.mini_window,text='Breakfast?',command=self.BreakfastOptions)
        self.button30.pack()
        self.button31 = tkinter.Button(self.mini_window,text='Lunch?',command=self.LunchOptions)
        self.button31.pack()
        self.button32 = tkinter.Button(self.mini_window,text='Dinner?',command=self.DinnerOptions)
        self.button32.pack()
        self.button33 = tkinter.Button(self.mini_window,text='Snack?',command=self.SnackOptions)
        self.button33.pack()

    def BreakfastOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def LunchOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def DinnerOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def SnackOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def ProductivityOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Are You Interested In Doing Today?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button34 = tkinter.Button(self.mini_window,text='Homework?',command=self.Homework)
        self.button34.pack()
        self.button35 = tkinter.Button(self.mini_window,text='Chores?',command=self.Chores)
        self.button35.pack()
        self.button36 = tkinter.Button(self.mini_window,text='Puzzle?',command=self.Puzzle)
        self.button36.pack()

    def Homework(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Yeah, go do that....')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
    
    def Chores(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='You Do Not Want Everyone Yelling At You. Go, But Come Back When You Finish!')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def Puzzle(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Go Do Some Brain Exercises!!')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def WorkoutOptions(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='What Are You Interested In Working Today?')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button37 = tkinter.Button(self.mini_window,text='Arms?',command=self.ArmsWorkouts)
        self.button37.pack()
        self.button38 = tkinter.Button(self.mini_window,text='Legs?',command=self.LegWorkouts)
        self.button38.pack()
        self.button39 = tkinter.Button(self.mini_window,text='Core?',command=self.CoreWorkouts)
        self.button39.pack()        


    def ArmsWorkouts(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def LegWorkouts(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()

    def CoreWorkouts(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Good Choice! You Should Check Out...')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()


        
gui = MyGUI()
