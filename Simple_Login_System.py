# Main Project: Create a simple login system 
# Default user login details set on the backend
correct_username = "Dominion"
correct_password = "0000"
# I started with "-" for styling and also separate the code from other terminal parameters
print ("-" * 55) # I use a multiplication code here, instead of typing "-" many times 
print ("Welcome to the OTS Innovation Project. Login to Access!".upper()) # .upper() is used to print the whole string in upper case 
print ("-" * 55) # This is used to give the welcome note a unified style 

# I used the while logic here to create the loop for user to retry if they fail
while True:
    # This is the interface that the user will interact with to enter the login details
    username_attempt = input ("Enter Username: ") # The interface to enter password
    password_attempt = input ("Enter Password: ") # The interface to enter password
    # I used the if logic here to check if the user input is the same with the one on the backend
    if username_attempt == correct_username and password_attempt == correct_password:
        print ("") # The empty strings is used to have a space to separae the details from the printed login note
        print ("            ✅ login successful! welcome 🤝".title()) # .title() is used to capitalize all the first letter in the sentence and the empty space to align center
        print ("-" * 55) # "-" is used to create the unified look as the above 
        # I used the while logic here to continue the loop for user to open another layer in the ecosystem
        while True:
            passcode = "ots-042026".upper() # The upper is used here to capitalize all the strings
            
            print ("                  sign attendance here".title()) # .title() is used to capitalize all the first letter in the sentence and the empty space to align center
            print ("-" * 55) # "-" is used to create the unified look as the above 
             # This is the interface that the user will interact with to enter their required details
            passcode_attempt = input("enter your passcode: ".capitalize()) # Capitalize is used to capitalize the first letter of the interface
             # I used the if logic here to check if the user input is the same with the one on the backend
            if passcode_attempt == passcode:
                print ("") # The empty strings is used to have a space to separae the details from the printed login note
                print ("    you have successfully signed your attendance 🤝".title()) # .title() is used to capitalize all the first letter in the sentence and the empty space to align center
                print ("-" * 55) # "-" is used to create the unified look as the above 
                break
            else:
                print ("") # The empty strings is used to have a space to separae the details from the printed login note
                print ("                 🚫 invalid credential! \n             incorrect passcode try again!".title()) # \n is used to break the next strings into a new line instead of printing another
                print ("-" * 55) # "-" is used to create the unified look as the above and separate the first attempt from the next attempt
        break # This is used to break the loop if the user enters the correct details
    else:
        print ("") # The empty strings is used to have a space to separae the details from the printed login note
        print ("                 🚫 access denied! \n       incorrect username or password try again!".title()) # \n is used to break the next strings into a new line instead of printing another
        print ("-" * 55) # "-" is used to create the unified look as the above and separate the first attempt from the next attempt
