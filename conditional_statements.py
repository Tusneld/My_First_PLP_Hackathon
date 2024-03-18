# Prompt user to enter their age
age_str = input("Enter your age: ")

# Check if input is a valid integer
if age_str.isdigit():
    age = int(age_str)
    
    # Check if age is greater than or equal to 18
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
    # Check if age is less than 0        
else:
    print("Invalid age entered")
