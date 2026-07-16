# Challenge C: The Even/Odd Counter (1 to 40)
print("") # This creates a space before the welcome note
print("-" * 13, "Even/Odd Counter Engine".upper(), "-" * 13) # This gives the header all caps and a different heading

# I initialized a tracking variable here to start our counter upward from 1
count_number = 1 

# I used the while logic here to create an infinite loop that continues counting up automatically
while True:
    
    # I used the if logic with a modulo operator here to check if the number divides cleanly by 2 with 0 remainder
    if count_number % 2 == 0:
        print(f"Number {count_number} is EVEN") # f-string is used here to dynamically display the number alongside its even status
    else:
        print(f"Number {count_number} is ODD") # This handles the alternative condition when the remainder is not 0
        
    # THE KILL SWITCH: This is the rule for this challenge to force the counting to stop the moment it hits 40
    if count_number == 40:
        print("\nTarget reached! Stopping the counter at 40.") # This prints a direct notification to the user that the target is met
        break # This is used to break the loop safely and kill the infinite engine instantly
        
    # This increases our tracking container by 1 dynamically so it can process the next number in the loop cycle
    count_number += 1 

print("-" * 43, "\n") # This marks the end of the printed sequence with a unified barrier line
