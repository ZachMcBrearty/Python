# Weather App, using the bbc rss feed
#
import feedparser # https://github.com/kurtmckee/feedparser
import tkinter as tk # inbuilt

#~6 digit code for each area
#found by first going to website and copying from url
num = 000000 
url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/{num}"

def parseData(feed): # feed will be the parsed weather url
    _3DayData = feed["entries"] # the days are stored in entries
    _3DayDataFull = [] # final data set
    for x in _3DayData:
        dayName = x["title"].split()[0] # the day, eg "Friday:"
        daySummary = x["summary"].split(", ") # weather information for the day
        Day = [dayName, daySummary]
        _3DayDataFull.append(Day)
    return _3DayDataFull

def printDisplay(data): # basic display in idle or terminal
    for x in data: # eg _3DayDataFull:
        print(x[0]) # dayName
        for y in x[1]:
            print("-", y) # all the data in daySummary
        print() # separates each day 

def showTkinter(data, root=None): # tkinter to display the data, days in blue
    if root == None:
        root = tk.Tk()
    # required by terms of use>
    # THINK: highlight in red?
    tk.Label(root, text="BBC Weather Unofficial").pack(anchor="n")
    for x in data:
        #dayName, highlighted in blue
        tk.Label(root, text=x[0], bg="skyblue").pack(anchor="w", expand=1)
        for y in x[1]:
            # the daySummary, indented slightly 
            tk.Label(root, text="- "+y).pack(anchor="w")
        # spacer after each day 
        tk.Label(root, text="").pack(anchor="w")
    root.mainloop()

def update(root, TESTING=False):
    feed = feedparser.parse(url)
    if not TESTING:
        showTkinter(parseData(feed),root)
    else:
        printDisplay(parseData(feed))

if __name__=="__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title("Weather")
    root.geometry(newGeometry="300x800+150+150")
    update(root)
        
    
