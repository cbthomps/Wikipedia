#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created on: Mon Jul 12 15:17:05 2021
@author: Chris Thompson
@pythonVersion: 3.8
    
@description: This is a script to pick out a random Wikipedia page.
"""
#####################################
#IMPORT MODULES
#####################################
import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
#####################################
#GLOBAL VARIABLES
#####################################


#####################################
#CLASSES
#####################################
#The main menu for the program
class MainMenu(tk.Tk):
    #Sets up the frame and label and buttons for the main menu
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg ='LightCyan2', width = 700, height = 700)
        self.foo = None
        self.label1 = tk.Label(self.frame, text = 'Press for a random Wikipedia article:' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label1.place(x=50, y=50)
        self.button1 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Random Article'  ,padx =5,bg ='LightCyan3' ,command = self.RandomArticle)
        self.button1.place(x=50, y=100)
        self.button2 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read'  ,padx =5,bg ='LightCyan3' ,command = self.ReadArticle)
        self.button2.place(x=50, y=450)
        self.button3 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Next'  ,padx =5,bg ='LightCyan3' ,command = self.RandomArticle)
        self.button3.place(x=125, y=450)
        
        self.label1 = tk.Label(self.frame, text = 'Title:' , font='arial 20 bold')
        self.label1.place(x=50, y=150)
        self.heading = tk.StringVar()
        self.entry1 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.heading, bg ='antiquewhite2',width = 75,)
        self.entry1.place(x=50, y = 200)
        self.label2 = tk.Label(self.frame, text = 'First Paragraph:' , font='arial 20 bold')
        self.label2.place(x=50, y=250)
        self.body1 = tk.StringVar()
        self.entry2 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.body1, bg ='antiquewhite2',width = 75,)
        self.entry2.place(x=50, y = 300)
        self.body2 = tk.StringVar()
        self.entry3 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.body2, bg ='antiquewhite2',width = 75,)
        self.entry3.place(x=50, y = 320)
        self.body3 = tk.StringVar()
        self.entry4 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.body3, bg ='antiquewhite2',width = 75,)
        self.entry4.place(x=50, y = 340)
        self.body4 = tk.StringVar()
        self.entry5 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.body4, bg ='antiquewhite2',width = 75,)
        self.entry5.place(x=50, y = 360)
        self.body5 = tk.StringVar()
        self.entry6 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.body5, bg ='antiquewhite2',width = 75,)
        self.entry6.place(x=50, y = 380)
        self.frame.pack()
    #Function that finds an article at random from Wikipedia
    def RandomArticle(self):
        self.page = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.title = self.soup.find(class_ = "firstHeading").text
        self.url = 'https://en.wikipedia.org/wiki/%s' %self.title
        #This is what will be displayed for the user from the webpage
        self.pageTitle = self.soup.select('h1')[0].text
        self.firstParagraph = self.soup.select('p')[0].text
        self.firstLines = self.firstParagraph[0:75]
        self.secondLines = self.firstParagraph[75:150]
        self.thirdLines = self.firstParagraph[150:225]
        self.fourthLines = self.firstParagraph[225:300]
        self.fifthLines = self.firstParagraph[300:375]
        self.heading.set(self.pageTitle)
        self.body1.set(self.firstLines)
        self.body2.set(self.secondLines)
        self.body3.set(self.thirdLines)
        self.body4.set(self.fourthLines)
        self.body5.set(self.fifthLines)
    #This function takes users to the webpage if they click the button    
    def ReadArticle(self):
        webbrowser.open(self.url)

#####################################
#USER-DEFINED FUNCTIONS
#####################################
#Establishes the graphical interface's size, title, and color
def main():
    root = tk.Tk()
    root.geometry('700x700')
    root.resizable(0,0)
    root.title("Random Wikipedia Article")
    root.config(bg ='LightCyan2')
    app = MainMenu(root)

#####################################
#RUN SCRIPT
#####################################
if __name__ == "__main__":
    main() 
