import random
from tkinter import *

all_character = ''
generate = ''

def is_l_letter()	:
    global all_character
    all_character += 'abcdefghijklmnopqrstuvwxyz'

def is_u_letter()	:
    global all_character
    all_character += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def is_digits()	:
    global all_character
    all_character += '0123456789'

def is_special()	:
    global all_character
    all_character += "'`-=[]\\;',./~!@#$%^&*()_+{}|:\"<>?'"

def generate_password()	:
    global all_character, generate
    if not all_character:
        result_label.config(text="⚠️ Please select at least one character set")
        return
    try:
        num = int(num_entry.get().strip())
        generate = ''.join(random.choices(all_character, k=num))
        result_label.config(text="Generated Password: " + generate)
        all_character = ''
    except:
        result_label.config(text="⚠️ Enter a valid number")

gui = Tk()
gui.state("zoomed")
gui.title("Strong Password Generator")
gui.config(bg = "lightblue")

Label(gui, text = "Strong Password Generator", font = ("Arial, 14"), bg = "lightblue").grid(row = 0, column = 0, padx = 50, pady = 30)

Label(gui, text = "Enter the number of character you want to generate:", font = ("Arial, 12"), bg = "lightblue").grid(row = 1, column = 0, padx = 50, pady = 10)
num_entry = Entry(gui, font = ("Arial, 12"))
num_entry.grid(row = 1, column = 1, pady = 10)

Button(gui, text = "Upper-Case", command = is_u_letter, bg = "red", width = 20).grid(row = 2, column = 0, padx = 50, pady = 10)

Button(gui, text = "Lower-Case", command = is_l_letter, bg = "olive", width = 20).grid(row = 2, column = 1, padx = 50, pady = 10)

Button(gui, text = "Digits", command = is_digits, bg = "green", width = 20).grid(row = 3, column = 0, padx = 50, pady = 10)

Button(gui, text = "Special Character", command = is_special, bg = "yellow", width = 20).grid(row = 3, column = 1, padx = 50, pady = 10)

Button(gui, text = "Generate Password", command = generate_password, bg = "orange", width = 20).grid(row = 4, column = 1, padx = 50, pady = 10)

result_label = Label(gui, text="Generated Password: ", font=("Comic Sans MS", 12), bg="lightblue")
result_label.grid(row=5, column=0, columnspan=2, padx=50, pady=20)

gui.mainloop()
