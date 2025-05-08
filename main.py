from tkinter import *  
import pandas  
import random  

# Global variable to store the current word card
global current_card
# Dictionary to store words to be learned
to_learn = {}


BACKGROUND_COLOR = "#B1DDC6"

# Try to load the CSV file that stores the words to be learned
try:
    data = pandas.read_csv("data/words_to_learn.csv")

# If 'words_to_learn.csv' doesn't exist, load the original word list ('words.csv')
except FileNotFoundError:
    og_data = pandas.read_csv("data/words.csv")
    to_learn = og_data.to_dict(orient="records")

# If the 'words_to_learn.csv' file exists, use it
else:
    to_learn = data.to_dict(orient="records")

# Function to show the next flashcard
def next_card():
    global current_card, flip_timer
    # Cancel the previous flip timer to avoid multiple flips at once
    window.after_cancel(flip_timer)
    
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Arabic", fill="black")  
    canvas.itemconfig(card_word, text=current_card["Arabic"], fill="black")  
    canvas.itemconfig(card_bg, image=card_front)  
    
    # Set a timer to flip the card after 3 seconds
    window.after(3000, func=flip_card)

# Function to mark the current word as known and remove it form the file
def iKnow():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    
    # Show the next card after marking the current one as known
    next_card()

# Function to flip the card and show the English translation
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)

window = Tk()
window.title("Flash")  
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  

# Set the timer to flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Create a canvas to hold the flashcard
canvas = Canvas(width=800, height=526)

# Load the front and back images of the flashcard
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Add text labels for the card title (Arabic/English) and the word
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_pic = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=wrong_pic, highlightthickness=0, command=next_card)
unkown_button.grid(row=1, column=0)

check_pic = PhotoImage(file="images/right.png")
check_button = Button(image=check_pic, highlightthickness=0, command=iKnow)
check_button.grid(row=1, column=1)

# Show the first flashcard
next_card()

window.mainloop()
