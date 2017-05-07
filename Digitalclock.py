# Zach McBrearty
# First made: 17/03/2017
# Simple Digital Clock
# Tk and Datetime used together to make a digital clock
import tkinter as tk
import datetime as dt
##import sys
##sys.setrecursionlimit(20) 
# tested to see if the update function was recursive
# it wasnt, but testing this appeared to crash the IDLE
# basic Clock / tk.Frame class
class Clock(tk.Frame):
    def __init__(self, master=None, TwentyFourHour=True):
        '''basic init for the tk Clock
        TwentyFourHour - Controls whether the hour is 24 hour or 12 hour ''' 
        if TwentyFourHour:
            self.HourDiv = 24
        else:
            self.HourDiv = 12
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.update()
        
    def update(self):
        '''Updates the Day/Month/Year and Hour:Minute:Second so the time is correct'''
        now = dt.datetime.now()
        temp = str(now.day)+" / "+str(now.month)+" / "+str(now.year)
        self.DMY.configure(text=temp)
        temp2 = str(now.hour%self.HourDiv)+" : "+str(now.minute)+" : "+str(now.second)
        self.HMS.configure(text=temp2)
        temp3 = self.getAge()
        if type(temp3) == str:
            print(end="")
        else:
            temp3 = "-".join(temp3)
        self.age.configure(text=temp3)
        self.after(1000,self.update)
        
    def create_widgets(self):
        '''Creates the widgets in the order:(Text Label at top) > (year month day) > (hour minute second) > age'''
        tk.Label(text="Day / Month / Year    Hour : Minute : Second").pack(side=tk.TOP)
        now = dt.datetime.now()

        temp = str(now.day)+" / "+str(now.month)+" / "+str(now.year)
        self.DMY = tk.Label(text=temp)
        self.DMY.pack(side=tk.LEFT, expand=1)
        temp2 = str(now.hour%self.HourDiv)+" : "+str(now.minute)+" : "+str(now.second)
        self.HMS = tk.Label(text=temp2)
        self.HMS.pack(side=tk.LEFT, expand=1)
        temp3 = self.getAge()
        if type(temp3) == str:
            print(end="")
        else:
            temp3 = "-".join(temp3)
        self.age = tk.Label(text=temp3)
        self.age.pack(side=tk.BOTTOM)

    def getAge(self,year=2001, month=11, day=6):
        '''Gets the the age of the person
        args: year, month, day (of birth)'''
        now = dt.datetime.now()
        nowLst = [now.year, now.month, now.day]
        birthLst = [year, month, day]
        ans = []
        for x, y in zip(nowLst, birthLst):
            ans.append(x-y)
        if not ans[1] and not ans[2]: # not 0 is True # it would be 0 months and days on birthday
            return "Happy Birthday"
        if ans[2] < 0:
            ans[1] -= -1
            ans[2] += 30
        if ans[1] < 0:
            ans[0] -= 1
            ans[1] += 12
            
        for i, x in enumerate(ans):
            ans[i] = str(x)
        return ans
        
#base root for the tkinter obj
root = tk.Tk()
root.resizable(width=False, height=False)
root.title("Simple Clock")
root.geometry(newGeometry="250x75+150+150")
root.config(bg="firebrick")
root.attributes("-topmost", True)
#the clock
clock = Clock(root)
clock.mainloop()
