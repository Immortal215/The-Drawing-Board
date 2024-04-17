import os
import sys
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import customtkinter as ctk
import pickle
import pprint
import time

 
def pickleData(data):
 with open('data.pickle', 'wb') as file:
    my_data = data
    pickle.dump(my_data, file)
 
 # Shows data.pickle in readable text
 obj = pickle.load(open("data.pickle", "rb"))
 
 with open("data.pickle", "a") as f:
     f.write("\n\n||          ||\nvv Readable vv\n~~~~~~~~~~~~~~~\n")
     pprint.pprint(obj, stream=f)
 
def unPickleName():
 
 with open('data.pickle', 'rb') as f:
     try : 
      loaded_data = pickle.load(f)
      return loaded_data["name"]
     except : 
       print("\n\n~ Error Loading Data ~\n\n")    


ctk.set_default_color_theme("appThemes.json")


class TabView1(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # add widgets on tabs
        self.label = ctk.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)
        
        self.label = ctk.CTkLabel(master=self.tab('tab 1'), text=f"Hello {unPickleName()}!")
        self.label.grid(padx=20,pady=20)


class App(ctk.CTk):
    
    def __init__(self):
        self.data = {"name":"123",}
        pickleData(self.data)

        super().__init__()


        def icon_change():

             current_path = os.getcwd()
             print(current_path)
             path_n_file = ""
             
             try :
                path_n_file = current_path + "\\assets\\icon.ico"

             except:
                 raise Exception("Unknown system")
                 exit(1)
                 
             return path_n_file
        
        screenW = (self.winfo_screenwidth())
        screenH = (self.winfo_screenheight())
        
        
        self.geometry('%dx%d+%d+%d' %((screenW/1.5), (screenH/1.5), ((screenW/2)-(screenW/3)),((screenH/2)-(screenH/3))))
        
        self.title("The Drawing Board")
        self.iconbitmap(icon_change())

 
        
        # self.button = ctk.CTkButton(self, text="Click", command=self.button_callbck)
        # self.button.grid(row=3,padx=20,pady=20)
        

        
        self.tab_view = TabView1(master=self, border_width=3)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        
    # def button_callbck(self):
    #     self.label.configure(text=unPickleName())

        
   

app = App()
app.mainloop()




