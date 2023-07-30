from tkinter import *

def prssing_button(num):
    # Function to handle button presses and update the equation

    global equation
    equation = equation + str(num)  # Concatenate the button value to the equation string
    equation_lable.set(equation)   # Update the label with the new equation

def equal():
    # Function to calculate the result when the equal sign is pressed

    try:
        global equation
        total = str(eval(equation))  # Evaluate the equation and convert the result to a string
        equation_lable.set(total)    # Update the label with the result

        equation = total             # Set the equation to the result for future calculations

    except SyntaxError:
        # Handling syntax errors

        equation_lable.set("Syntax Error")
        equation = ""

    except ZeroDivisionError:
        # Handling arithmetic errors (division by zero)

        equation_lable.set("Arithmetic Error")
        equation = ""

def clear_screen():
    # Function to clear the calculator screen

    global equation
    equation_lable.set("")  # Clear the label
    equation = ""           # Clear the equation variable

# Create the main application window
window_page = Tk()
window_page.title("Simple Calculator")
window_page.geometry("500x500")

# Initialize the equation variable to store the mathematical expression
equation = ""

# Create a StringVar to update the label text dynamically
equation_lable = StringVar()

# Create the label to display the equation and result
label = Label(window_page, textvariable=equation_lable, bg="white", width=50, height=3, font=50)
label.pack()

# Create a frame to hold the calculator buttons
frame = Frame(window_page)
frame.pack()

# Create number buttons (1-9)
button_1 = Button(frame, text=1, height=3, width=10, font=40, command=lambda: prssing_button(1))
button_1.grid(row=0, column=0)

# (Buttons 2 to 9 follow the same pattern)
button_2=Button(frame,text=2,height=3,width=10,font=40,
                command=lambda:prssing_button(2))
button_2.grid(row=0,column=1)

button_3=Button(frame,text=3,height=3,width=10,font=40,
                command=lambda:prssing_button(3))
button_3.grid(row=0,column=2)

button_4=Button(frame,text=4,height=3,width=10,font=40,
                command=lambda:prssing_button(4))
button_4.grid(row=1,column=0)

button_5=Button(frame,text=5,height=3,width=10,font=40,
                command=lambda:prssing_button(5))
button_5.grid(row=1,column=1)

button_6=Button(frame,text=6,height=3,width=10,font=40,
                command=lambda:prssing_button(6))
button_6.grid(row=1,column=2)

button_7=Button(frame,text=7,height=3,width=10,font=40,
                command=lambda:prssing_button(7))
button_7.grid(row=2,column=0)

button_8=Button(frame,text=8,height=3,width=10,font=40,
                command=lambda:prssing_button(8))
button_8.grid(row=2,column=1)

button_9=Button(frame,text=9,height=3,width=10,font=40,
                command=lambda:prssing_button(9))
button_9.grid(row=2,column=2)


# Create number button for 0
button_0 = Button(frame, text=0, height=3, width=10, font=40, command=lambda: prssing_button(0))
button_0.grid(row=3, column=0)

# Create operator buttons (+, -, *, /)
plus_sign = Button(frame, text="+", height=3, width=10, font=40, command=lambda: prssing_button("+"))
plus_sign.grid(row=0, column=3)

# (Other operator buttons follow the same pattern)

minus_sign=Button(frame,text="-",height=3,width=10,font=40,
                command=lambda:prssing_button("-"))
minus_sign.grid(row=1,column=3)

multiply_sign=Button(frame,text="*",height=3,width=10,font=40,
                command=lambda:prssing_button("*"))
multiply_sign.grid(row=2,column=3)

divide_sign=Button(frame,text="/",height=3,width=10,font=40,
                command=lambda:prssing_button("/"))
divide_sign.grid(row=3,column=3)


# Create the equal sign button (=)
equal_sign = Button(frame, text="=", height=3, width=10, font=40, command=equal)
equal_sign.grid(row=3, column=2)

# Create the decimal point button (.)
decimal_sign = Button(frame, text=".", height=3, width=10, font=40, command=lambda: prssing_button("."))
decimal_sign.grid(row=3, column=1)

# Create the clear button
clear = Button(window_page, text="Clear", height=3, width=14, font=40, command=clear_screen)
clear.pack()

# Start the main event loop
window_page.mainloop()
