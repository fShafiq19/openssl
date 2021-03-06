from tkinter import *
import json
import os

def main_account_screen():
    global main_screen
    main_screen = Tk()  # create a GUI window
    main_screen.geometry("300x250")  # set the configuration of GUI window
    main_screen.title("Account Login")  # set the title of GUI window


    # create a Form label
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    # create Login Button
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()

    # create a register button
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()  # start the GUI

def register():
    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window.
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable
    global username
    global password
    global username_entry
    global password_entry
    global register_screen

    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    # Set text variables
    username = StringVar()
    password = StringVar()

    # Set label for user's instruction
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()

    # Set username label
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    # Set password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()

    # Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    # Set register button
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()

def register_user():

    # get username and password
    username_info = username.get()
    password_info = password.get()
    newUser = {username_info: password_info}
    json_obj = json.dumps(newUser)

    if os.path.isfile("users.json"):
        with open('users.json') as openfile:
            # Reading existing data from json file
            existingUsers = json.load(openfile)
        # adding the new user data
        existingUsers.update(newUser)
        newList = json.dumps(existingUsers)
        with open('users.json', 'w') as openfile:
            openfile.write(newList)
    else:
        with open("users.json", "w") as file:
            file.write(json_obj)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login():
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    global login_screen

    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()

def login_verification():
    print("working...")
#get username and password
    username1 = username_verify.get()
    password1 = password_verify.get()
# this will delete the entry after login button is pressed
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

#The method listdir() returns a list containing the names of the entries in the directory given by path.
    list_of_files = os.listdir()

    if os.path.isfile("users.json"):
        with open('users.json') as openfile:
            # Reading existing data from json file
            existingUsers = json.load(openfile)

        if username1 in existingUsers:
            if (existingUsers[username1] == password1):
                login_success()
            else:
                password_not_recognised()
        else:
            user_not_found()

def login_success():
    global login_success_screen   # make login_success_screen global

    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
# create OK button
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen

    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Invalid pass")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()

    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()



def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_login_success():
    login_success_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()


main_account_screen()  # call the main_account_screen() function