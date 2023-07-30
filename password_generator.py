from tkinter import *
import random

def generate_password():
    global length_value
    # Define the characters that can be used to generate the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^*().[]<>,?:;"
    # Get the desired length of the password from the input field
    length = length_value.get()
    # Check if the input is a valid numeric value
    if length.isnumeric():
        # Generate the password by randomly selecting characters from the defined set
        password = ''.join(random.choice(characters) for _ in range(int(length)))
        # Update the password_label with the generated password
        password_label.config(text="Generated_Password: " + password)
    else:
        # If the input is not a valid number, show an error message in the password_label
        password_label.config(text="Enter_a_Valid_Number")

# Create the main window
window = Tk() 
window.geometry("700x200")
window.title("PASSWORD_GENERATOR")

# Create and place widgets on the window
label = Label(window, text="P@55W0RD GENER@T0R", font="bold", bg="white")
label.grid(row=0, column=2)

length_label = Label(window, text="Length_of_password(only _number): ")
length_label.grid(row=1, column=1)

length_value = StringVar()
length_entry = Entry(window, textvariable=length_value)
length_entry.grid(row=1, column=2)

generate_button = Button(window, text="Generate Password", command=generate_password, font="bold")
generate_button.grid(row=2, column=2)

password_label = Label(window, text="", font="bold")
password_label.grid(row=3, column=1, columnspan=5)

# Start the main event loop
window.mainloop()
