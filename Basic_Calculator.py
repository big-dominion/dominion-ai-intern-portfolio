# Challenge A: Basic Calculator
print("") # This creates a space before the welcome note
print("-" * 25, "Desktop Calculator".upper(), "-" * 25) # This gives the header all caps and a different heading

# I used the while logic here to create the loop for user to continue the process without ending
while True:
   
    # The interface that collects numbers the user wants to work with and converts to float in case they want to work with decimals too
    number_1 = float(input("enter your first number: ".capitalize())) # To collect the first number and convert to float
    number_2 = float(input("Enter your second number: ".capitalize())) # To collect the second number and convert to float
   
    # Ask the user what they want to do
    print("-" * 70) # This is used to separate the input numbers from the operations layout
    print("Operations: Add (+), Subtract (-), Divide (/), Multiply (*), or Exit".title()) # .title() is used to capitalize all the first letters of the menu selection
   
    # .title() automatically converts inputs like "add" to "Add", preventing case-sensitivity errors from the user
    operations = input("\nWhat do you want to do? ").title()


    # The kill switch: This evaluates if the user wants to exit the app instead of performing calculations
    if operations == "Exit":
        print("\nShutting down calculator. Goodbye! 👋\n") # This prints a shutdown note to the user
        break # This is used to break the loop safely if the user types exit

    # I used the if logic here to check if the user input matches addition execution
    if operations == "Add" or operations == "+":
        result = number_1 + number_2 # The math engine that adds the two numbers together
        print("") # The empty string is used to create a breathing space before the final output result
        print("-" * 70) # This gives the output results a unified styling barrier
        print(f"Result: {number_1} + {number_2} = {result}") # f-string is used here to dynamically inject our numbers and the final result together
        print("-" * 70, "\n") # This marks the end of the first calculation and sets up the spacing for the next calculation loop

    # I used the elif logic here to check if the user input matches subtraction execution
    elif operations == "Subtract" or operations == "-":
        result = number_1 - number_2 # The math engine that subtracts number two from number one
        print("") # The empty string is used to create a breathing space before the final output result
        print("-" * 70) # This gives the output results a unified styling barrier
        print(f"Result: {number_1} - {number_2} = {result}") # f-string is used here to dynamically inject our numbers and the final result together
        print("-" * 70, "\n") # This marks the end of the calculation and sets up the spacing for the next calculation loop
       
    # I used the elif logic here to check if the user input matches multiplication execution
    elif operations == "Multiply" or operations == "*":
        result = number_1 * number_2 # The math engine that multiplies the two numbers together
        print("") # The empty string is used to create a breathing space before the final output result
        print("-" * 70) # This gives the output results a unified styling barrier
        print(f"Result: {number_1} * {number_2} = {result}") # f-string is used here to dynamically inject our numbers and the final result together
        print("-" * 70, "\n") # This marks the end of the calculation and sets up the spacing for the next calculation loop
       
    # I used the elif logic here to check if the user input matches division execution
    elif operations == "Divide" or operations == "/":
        # I nested an if statement here to handle an edge case error before performing the math
        if number_2 == 0:
             print("") # The empty string is used to create a breathing space
             print("-" * 70) # This gives the error message a unified styling barrier
             print("Error: Cannot divide by zero!") # This stops the program from crashing if a user divides by zero
             print("-" * 70, "\n") # This marks the end of the error block and loops back safely
        else:
             result = number_1 / number_2 # The math engine that executes safe division arithmetic
             print("") # The empty string is used to create a breathing space before the final output result
             print("-" * 70) # This gives the output results a unified styling barrier
             print(f"Result: {number_1} / {number_2} = {result}") # f-string is used here to dynamically inject our numbers and the final result together
             print("-" * 70, "\n") # This marks the end of the calculation and sets up the spacing for the next calculation loop
             
    # I used the else logic here to trap random invalid options typed by the user
    else:
        print("\nError: Invalid operation selected. Please try again.\n") # Prints a direct error warning text to the terminal
        print("-" * 70, "\n") # This separates the failed attempt from the next fresh loop setup