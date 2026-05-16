from tkinter import *
from random import choice
import pandas as pd
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
def load_data():
    global to_learn
    try:
        data_to_learn = pd.read_csv("data/words_to_learn.csv")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        original_data = pd.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient='records')
    else:
        if len(data_to_learn) == 0:
            original_data = pd.read_csv("data/french_words.csv")
            to_learn = original_data.to_dict(orient='records')
        else:
            to_learn = data_to_learn.to_dict(orient='records')

load_data()


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    palavras_restantes = len(to_learn)
    label_contador.config(text=f"Palavras restantes: {palavras_restantes}")

    # Validação caso o usuário acerte todas as palavras
    if palavras_restantes == 0:
        canvas.itemconfig(card_title, text="Parabéns!", fill="black")
        canvas.itemconfig(card_word, text="Você aprendeu tudo!", fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        known_button.config(state="disabled")
        unknown_button.config(state="disabled")
        return
    current_card = choice(to_learn)
    canvas.itemconfig(card_title,text="French", fill="black")
    canvas.itemconfig(card_word,text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image = card_back_img)



def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


def reset_game():
    global to_learn
    # Deleta o arquivo de progresso se ele existir
    if os.path.exists("data/words_to_learn.csv"):
        os.remove("data/words_to_learn.csv")

    # Reativa os botões do jogo
    known_button.config(state="normal")
    unknown_button.config(state="normal")

    # Recarrega a lista original e reinicia o card
    load_data()
    next_card()


window = Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50, highlightthickness=0)

flip_timer = window.after(2000, func=flip_card)

canvas = Canvas(window, width=800, height=526)

label_contador = Label(text="",font=("Arial", 16, "bold"),bg=BACKGROUND_COLOR,fg="#2f3542")
label_contador.grid(row=0, column=0, columnspan=2, pady=(0, 20))

reset_button = Button(text="Restart", font=("Arial", 10, "bold"), command=reset_game, bg="#ffa502", fg="white", bd=0, relief="flat", padx=10, pady=5)
reset_button.grid(row=0, column=1, sticky="e", pady=(0, 10))

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,150, text="",font=("Arial", 40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Arial", 60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0, bd=0,relief="flat",bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=2, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0,bd=0,relief="flat",bg=BACKGROUND_COLOR,command=next_card)
unknown_button.grid(row=2, column=1)



next_card()

window.mainloop()