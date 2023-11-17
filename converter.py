import tkinter as tk 
from tkinter import ttk 
import ttkbootstrap as ttk
#this function is to give the command to the button  
def convert ():
    mile_input = entry_Int.get()
    km_output = mile_input*1.61
    output_string.set(km_output)
    


#window of the app
window =  ttk.Window(themename='darkly')
window.title('conveter')
window.geometry('300x150')

# a big bold title for the app 
title_label = ttk.Label(master=window, text='Miles to Kilometers',font='Calibri 25 bold')
title_label.pack()

#input fields which contains a button and an entry widget 
# the input frame is to house two widgets , so they become slaves of the input frame 
# for the button to function we add the comman function 
# to get the values from the entry field we use the get() method 
input_frame =  ttk.Frame(master=window )
#create an  entry int with tk.intvar, then plug it to the entry frame 
entry_Int = tk.IntVar()
entry = ttk.Entry(master=input_frame,textvariable=entry_Int)
button = ttk.Button(master=input_frame,text='Convert', command = convert)
entry.pack(side='left', padx=10)
button.pack()
input_frame.pack(pady=10)

#the output
# # create out put varaile 
output_string = tk.StringVar() 
output_label = ttk.Label(master= window,font='Calibri 25 bold',textvariable=output_string)
output_label.pack(pady=5)


window.mainloop()












