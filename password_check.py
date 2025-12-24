import string

password = input("Enter a password to test: ")
#(@, $, #, %)
has_special = any(char in string.punctuation for char in password)

if password == "":
    print("Error: password cannot be empty!")
elif len(password) < 8:
    print("Security Warning: Password is too short!(Min 8 chars)")
elif not has_special:
    print("Weak: You should add a special character (like @, $, #, %)")    
else:
    print("Strong: Password lenght and complexity are okay.")
