import random
print("---------------------------")
print("my password generator project".upper())
print("---------------------------\n")

psswd_1 = (input('choose pswd: '))

if len(psswd_1) < 10:
    print(f"password \'{psswd_1}\' is weak.")
    

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789"

    for pswd in range(1):
        password = ""
        for p in range(10):
            password += random.choice(characters)
        print(f" this password: {password}, has been generated for you.")
elif len(psswd_1) > 10 and len(psswd_1) <= 15:
    print("password taken")
else:
    print("maximum character is 15")


"""
This project 'PASSWORD GENERATOR' generate password randomely for the user, from the given characters above. 
The founder of python is: Guido van Rossium
"""


