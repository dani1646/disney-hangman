import random
import turtle

# Variables
tt = turtle.Turtle()

# Image setup
tt.speed(0)

#first guess
def draw_nothing():
    tt.penup()
    tt.goto(0, 0)
    tt.pendown()
    tt.forward(9)
    tt.color("white")
    tt.penup()

#following functions draw the hangman
#head
def draw_head():
        tt.penup()
        tt.goto(45,135)
        tt.pendown()
        tt.circle(35)
#body
def draw_body():
        tt.penup()
        tt.goto(80,100)
        tt.pendown()
        tt.setheading(0)
        tt.right(90)
        tt.forward(100)

#left leg
def draw_lleg():
        tt.penup()
        tt.goto(80,0)
        tt.pendown()
        tt.setheading(0)
        tt.left(225)
        tt.forward(80)

#right leg
def draw_rleg():
        tt.penup()
        tt.goto(80,0)
        tt.pendown()
        tt.setheading(0)
        tt.left(315)
        tt.forward(80)

#left arm`
def draw_larm():
        tt.penup()
        tt.goto(80,75)
        tt.pendown()
        tt.setheading(0)
        tt.left(180)
        tt.forward(50)

#right arm
def draw_rarm():
        tt.penup()
        tt.goto(80,75)
        tt.pendown()
        tt.setheading(0)
        tt.forward(50)

#left eye
def draw_leye():
        tt.penup()
        tt.goto(70,140)
        tt.pendown()
        tt.setheading(0)
        tt.left(135)
        tt.forward(10)
        tt.penup()
        tt.goto(70,146)
        tt.pendown()
        tt.seth(0)
        tt.right(135)
        tt.forward(10)

#right eye
def draw_reye():
        tt.penup()
        tt.goto(95,140)
        tt.pendown()
        tt.setheading(0)
        tt.left(135)
        tt.forward(10)
        tt.penup()
        tt.goto(95,146)
        tt.pendown()
        tt.seth(0)
        tt.right(135)
        tt.forward(10)

#mouth
def draw_mouth():
        tt.penup()
        tt.goto(65,120)
        tt.pendown()
        tt.seth(0)
        tt.forward(30)

#tounge
def draw_tounge():
        tt.penup()
        tt.goto(80, 115)
        tt.pendown()
        tt.color("black")
        tt.begin_fill()
        tt.circle(5)
        tt.penup()
        tt.goto(85,120)
        tt.pendown()
        tt.seth(0)
        tt.left(270)
        tt.forward(7)

# Gallows Hangman hangs from
def draw_gallows():
    tt.penup()
    tt.goto(-100, -100)
    tt.pendown()
    tt.goto(100, -100)
    tt.penup()
    tt.goto(-25, -100)
    tt.pendown()
    tt.setheading(0)
    tt.left(90)
    tt.forward(300)
    tt.right(90)
    tt.forward(105)
    tt.right(90)
    tt.forward(30)


# Function to choose a random word from the word list
def choose_word():
    with open('word.txt') as file:
        words = file.readlines()
    return random.choice(words).strip().lower()

# Function to display the current state of the word with blanks and correctly guessed letters
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Initialize the Turtle screen
screen = turtle.Screen()
screen.title("Disney Hangman Game")


# Initialize game
word_to_guess = choose_word()
guessed_letters = []
max_attempts = 10

while max_attempts > 0:
    # Display the word with blanks and guessed letters
    current_display = display_word(word_to_guess, guessed_letters)
    tt.penup()
    tt.goto(-50, -150)
    tt.pendown()
    tt.write(f"Word: {current_display}", align="left", font=("Arial", 16, "normal"))
    draw_gallows()


    if set(guessed_letters) >= set(word_to_guess):
        tt.penup()
        tt.goto(-25,0)
        tt.pendown()
        tt.clear()
        tt.write(f"You win! The word was: {word_to_guess}", align="left", font=("Arial", 16, "normal"))
        break

    guess = screen.textinput("Hangman", f"Word: {current_display}\nGuess a letter:").lower()

    if len(guess) != 1 or not guess.isalpha():
        tt.penup()
        tt.goto(-50, -200)
        tt.pendown()
        tt.write("Invalid input.", align="left", font=("Arial", 16, "normal"))
        continue

    if guess not in word_to_guess:
        max_attempts -= 1


    else:
        guessed_letters.append(guess)



# Draw the hangman figure
    if max_attempts == 10:
        draw_nothing()
    if max_attempts == 9:
        draw_head()
    elif max_attempts == 8:
        draw_body()
    elif max_attempts == 7:
        draw_lleg()
    elif max_attempts == 6:
        draw_rleg()
    elif max_attempts == 5:
        draw_larm()
    elif max_attempts == 4:
        draw_rarm()
    elif max_attempts == 3:
        draw_leye()
    elif max_attempts == 2:
        draw_reye()
    elif max_attempts == 1:
        draw_mouth()
    elif max_attempts == 0:
        draw_tounge()
        tt.penup()
        tt.goto(-150, 150)
        tt.pendown()
        tt.penup()
        tt.home()
        tt.goto(-150,-200)
        tt.pendown()
        tt.write(f"You lose! The word was: {word_to_guess}", align="left", font=("Arial", 16, "normal"))

# Hide turtle at the end
tt.hideturtle()
turtle.done()
