print(f'\nPlease Sign Up first ... \n')

input_username = input("     Username : ")
input_password = input("     Password : ")

username = input_username
password = input_password

print(f'You can log in NOW ... \n')

login_username = input("     Username : ")
# login_password = input("     Password : ")

# print("Hi...")

if login_username == username:
    # print(789)
    login_password = input("     Password : ")
    if password == login_password:
        print("Login successful! Welcome!")
    else:
        login_password = input("Incorrect password. You have 2 attempts left\n     Password : ")
        if login_password == password:
            print("Login successful! Welcome!")
        else:
            login_password = input("Incorrect password. You have 1 attempts left\n     password : ")
            if login_password == password:
                print("Login successful! Welcome!")
            else:
                print("Too many attempts. Please try again later.")

else:
    login_username = input("Incorrect username. You have 2 attempts left\n     Username : ")
    if login_username == username:
        login_password = input("     Password : ")
        if login_password == password:
            print("Login successful! Welcome!")
        else:
            login_password = input("Incorrect password. You have 1 attempts left\n     password : ")
            if login_password == password:
                print("Login successful! Welcome!")
            else:
                print("Too many attempts. Please try again later.")
    else:
        login_username = input("Incorrect username. You have 1 attempts left\n     Username : ")
        if login_username == username:
            login_password = input("     Password : ")
            if login_password == password:
                print("Login successful! Welcome!")
            else:
                print("Too many attempts. Please try again later.")
        else:
            print("Too many attempts. Please try again later.")
