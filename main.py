import tkinter as tk
from tkinter import ttk
import os, json

window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value='a button with string var')
button = ttk.Button(window, text='simple button', command=button_func, textvariable=button_string)
button.pack()

check_var = tk.IntVar(value=10)
check1 = ttk.Checkbutton(
    window, text='checkbox 1', 
    command=lambda:print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5)
check1.pack()

check2 = ttk.Checkbutton(
    window, text='checkbox 2', 
    command=lambda:check_var.set(5))
check2.pack()

radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window, text='radiobutton 1', 
    value=1, command=lambda:print(radio_var.get()),
    variable=radio_var)
radio1.pack()
radio2 = ttk.Radiobutton(window, text='radiobutton 2', value=2, variable=radio_var)
radio2.pack()

def radio_func():
    print(check_bool.get())
    check_bool.set(False)

radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

exercise_radio1 = ttk.Radiobutton(window, text='radio a', value='A', command=radio_func, variable=radio_string)
exercise_radio2 = ttk.Radiobutton(window, text='radio b', value='B', command=radio_func, variable=radio_string)

exercise_check = ttk.Checkbutton(window, text='exercise check', variable=check_bool)

exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()

window.mainloop()

# PART 4
""" def button_func():
    print(string_var.get())
    string_var.set('button pressed')

window = tk.Tk()
window.title('Tkinter Variables')

string_var = tk.StringVar(value='start value')

label = tk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = tk.Entry(master=window, textvariable=string_var)
entry.pack()

button = tk.Button(master=window, text='button', command=button_func)
button.pack()

exercise_var = tk.StringVar(value='test')

entry2 = ttk.Entry(master=window, textvariable=exercise_var)
entry2.pack()
entry1 = ttk.Entry(master=window, textvariable=exercise_var)
entry1.pack()
exercise_label = ttk.Label(master=window, textvariable=exercise_var)
exercise_label.pack()

window.mainloop() """

# PART 3
""" def button_func():
    # print(entry.get())
    entry_text = entry.get()

    # label.config(text=f'{os.cpu_count()}:threads')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # print(label.configure())

window = tk.Tk()
window.title('Getting and setting widgets')

label = tk.Label(master=window, text='Some text')
label.pack()

entry = tk.Entry(master=window)
entry.pack()

button = tk.Button(master=window, text='The button', command=button_func)
button.pack()

def reset_func():
    label['text'] = 'Some text'
    entry['state'] = 'normal'

exercise_button = tk.Button(master=window, text='exercise button', command=reset_func)
exercise_button.pack()

window.mainloop() """

# PART 2
""" def button_func():
    print('a button was pressed')

def exercise_button_func():
    print('hello')

window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

label = tk.Label(master=window, text='This is test')
label.pack()

text = tk.Text(master=window)
text.pack()

entry = tk.Entry(master=window)
entry.pack()

button = tk.Button(master=window, text='A button', command=button_func)
button.pack()

# exercise_button = tk.Button(master=window, text='A button', command=exercise_button_func)
exercise_button = tk.Button(master=window, text='exercise button', command=lambda:print('hello'))
exercise_button.pack()

window.mainloop() """

# PART 1
""" def convert():
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


window.mainloop() """