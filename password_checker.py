import pwinput
common_passwords = ["password", "password123", "Password@123", "12345678", "qwerty", "admin", "secret"]
password = pwinput.pwinput("Enter your password: ", mask="*")
if password in common_passwords: print("WARNING: This is a common password!!!")
length = len(password)
print("Password lenght:", length)
#Minimum length check 
has_min_length = length >= 8

if length >= 8: print("Password meets the minimum length requirment.")
else: print("Password is too short. Minimum length is 8 characters.")
#Upper and lowercase checks
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
if has_uppercase: print("Contains an uppercase letter")
else: print("Must contain at least one uppercase letter")
if has_lowercase: print("Contains a lowercase letter")
else: print("Must contain at least one lowercase letter")
#Number check 
has_number = any(char.isdigit() for char in password)
if has_number: print("contains a number.")
else: print("Must contain atleast one number")
#Special character check
has_special = any(not char.isalnum() and not char.isspace() for char in password)
if has_special: print("Contains a special character")
else: print("Must contain atleast one special character")
#calculate score 
is_common = password in common_passwords 
score = sum([
    has_min_length,
    has_uppercase,
    has_lowercase,
    has_number,
    has_special,
    not is_common
])
print("\nScore;", score, "/ 6")
if score <= 2: 
    strength = "WEAK"
elif score <=4:
    strength = "MEDIUM"
else: strength = "STRONG"
print("Strength:", strength)