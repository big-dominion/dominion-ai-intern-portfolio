# Challenge B: The Random Number Generator (Like OTPs or Recharge Pins)
import random # This imports Python's built-in random module to generate random numbers
import os

print("") # This creates a space before the welcome note
print("-" * 23, "Secure PIN Generator".upper(), "-" * 23) # This gives the header all caps and a different heading

# I used the while logic here to create the loop for user to continue the process without ending
while True:

    # The interface that collects inputs from the user and converts them to integers (whole numbers)
    pin_length = int(input("How many digits long should each PIN be? ")) # To collect the length of each row
    num_lines = int(input("How many lines of PINs do you want? ")) # To collect the total number of lines/rows

    print("\nGenerating...") # This prints a temporary notification to the user before displaying the result
    print("-" * 70) # This gives the output results a unified styling barrier

    # The Outer Loop: I replaced "i" with "line_count" to clearly show this tracks the row number
    for line_count in range(num_lines):
        
        current_pin = "" # I initialized an empty string here to store and glue the random digits together for the current row
        
        # The Inner Loop: I replaced "j" with "digit_count" to clearly show this tracks the digits inside the row
        for digit_count in range(pin_length):
            # This generates a random single digit between 0 and 9, converts it to string, and attaches it to our pin container
            random_digit = str(random.randint(0, 9))
            current_pin += random_digit # This appends the new digit to the string container programmatically
            
        print(f"Row {line_count + 1}: {current_pin}") # f-string is used here to print out the final row alongside its counted position

    print("-" * 70) # This marks the end of the printed PIN lines with a unified barrier

    # Ask the user if they want to run the engine again or close it down
    print("\nOptions: Continue (C) or Exit (E)".title()) # .title() is used to capitalize all the first letters of the choice menu
    user_choice = input("What do you want to do? ").title() # .title() automatically normalizes the input to Title Case

    # THE KILL SWITCH: This evaluates if the user wants to terminate the app session
    if user_choice == "Exit" or user_choice == "E":
        print("\nShutting down PIN generator. Goodbye! 👋\n") # This prints a shutdown note to the user
        break # This is used to break the loop safely if the user wants to exit
    else:
        print("\n" + "-" * 70 + "\n") # This separates the completed generation block from the next fresh loop setup > Data Structure

simple_login_system = "Python Basic & Logic Building/simple_login_system.py"

if os.path.exists(Workspace_path)