from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

data_list = data.to_dict(orient="records")
curr_word = {}


def generate_word():
    global curr_word, flip_timer
    window.after_cancel(flip_timer)
    curr_word = random.choice(data_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=curr_word["French"], fill="black")
    canvas.itemconfig(present_image, image=front_img)
    flip_timer = window.after(3000, func=card_flip)


def card_flip():
    canvas.itemconfig(present_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=curr_word["English"], fill="white")


def remove_word():
    data_list.remove(curr_word)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


window = Tk()
window.title("FlashCard🎴")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
present_image = canvas.create_image(400, 263, image=front_img)
canvas.config(background=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
title_text = canvas.create_text(400, 150, font=("Ariel", 50, "italic"), text="")
word_text = canvas.create_text(400, 300, font=("Ariel", 50, "italic"), text="")

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.config(background=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.config(background=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

generate_word()

window.mainloop()
