import tkinter as tk
from tkinter import ttk
import os, json

def convert():
    print(entryInt.get())
    mile_input = entryInt.get()
    km_output = mile_input * 1.61
    outputString.set(km_output)

window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

title_label = ttk.Label(master=window, text='Miles to kilometers', font='monospace 10')
title_label.pack()

input_frame = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryInt)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

outputString = tk.StringVar()
output_label = ttk.Label(master=window, text='output', font='monospace 13', textvariable=outputString)
output_label.pack(pady=5)

""""""

tk.Text(master=window).pack()

main_folder_name = 'data'
has_folder = os.path.isdir(main_folder_name)
if not has_folder:
   os.mkdir('data')
   folder_path = os.path.abspath(main_folder_name)
   print(f'created folder {folder_path}')
else:
    print('folder checked')

with open('data.json', 'r') as file:
    loaded_data = json.load(file)

""""""


window.mainloop()