# This is a CVSS score classification calculator.
# Useful for converting CVSS 2.0 scores to CVSS 3.0

# display welcome message
print("Welcome to the CVSS Classification Calculator.")
while True:
    user_input = input("Enter your CVSS risk score (0-10) or type 'q' to quit: ")
    if user_input == 'q':
        break
    try:
        score = float(user_input)
        if score < 0 or score > 10:
            raise ValueError("Invalid input. Score must be between 0 and 10 (decimals allowed).")
    except ValueError as e:
        if str(e) == "could not convert string to float: " + user_input:
            print("Error: Enter a valid number. (Decimals Allowed)")
        else:
            print(e)
        continue
    if score == 0.0:
         print("Your CVSS Risk Score is: None")
    elif score <=3.9:
        print("Your CVSS Risk Score is: Low")
    elif score <=6.9:
        print("Your CVSS Risk Score is: Medium")
    elif score <=8.9:
        print("Your CVSS Risk Score is: High")
    elif score <=10.0:
        print("Your CVSS Risk Score is: Critical")
    else:
        print("Invalid input. Score must be between 0 and 10 (decimals allowed).")

