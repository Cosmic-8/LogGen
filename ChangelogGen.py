# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
from datetime import datetime


def main():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    main_menu()


def main_menu():
    print("")
    print(
        " _____ _                            _                 _____                            _")
    print(
        "/  __ \ |                          | |               |  __ \                          | |")
    print(
        "| /  \/ |__   __ _ _ __   __ _  ___| | ___   __ _    | |  \/ ___ _ __   ___  _ __ __ _| |_ ___  _ __")
    print(
        "| |   | '_ \ / _` | '_ \ / _` |/ _ \ |/ _ \ / _` |   | | __ / _ \ '_ \ / _ \| '__/ _` | __/ _ \| '__|")
    print(
        "| \__/\ | | | (_| | | | | (_| |  __/ | (_) | (_| |   | |_\ \  __/ | | | (_) | | | (_| | || (_) | |")
    print(
        " \____/_| |_|\__,_|_| |_|\__, |\___|_|\___/ \__, |    \____/\___|_| |_|\___/|_|  \__,_|\__\___/|_|")
    print(
        "                          __/ |              __/ |                                                                            ")
    print(
        "                         |___/              |___/                                                                             ")

    print("Version 1.0.1")
    time = datetime.now()
    print("The current time and date is: " + time.strftime("%b %d, %Y %H:%M:%S"))
    print("1: New file")
    print("2: Open existing")
    print("3: Exit")
    user = input("> ")
    if user == "1":
        print("--------")
        print("New File")
        print("--------")
        log_type = prompt_log_type()
        new_file(log_type)
    elif user == "2":
        print("---------")
        print("Open File")
        print("---------")
        # file_read()
        print("This feature is not yet implemented")
        main_menu()
    elif user == "3":
        sys.exit()
    else:
        print("Error")
        main_menu()


def new_file(log_type):
    log = open(log_type + " Changelog.txt", "x")
    log.close()
    log = open(log_type + " Changelog.txt", "a")
    for x in log_type:
        log.write("-")
    log.write("----------")
    log.write("\n" + log_type + " Changelog" + "\n")
    for x in log_type:
        log.write("-")
    log.write("----------")
    # REMEMBER TO UPDATE THIS PRINT ON EVERY VERSION UPDATE!!!!
    log.write("\nThis file has been generated by LogGen V1.0.1\n")
    user = prompt_user()
    log.write("\nUser: " + user)
    now = datetime.now()
    log.write("\nCreation date: ")
    log.write(now.strftime("%b %d, %Y %H:%M:%S"))
    log.write("\n")
    log.write("\n")
    log.write("\n---------")
    log.write("Log Begin")
    log.write("---------")
    name = os.path.basename(log.name)
    log.close()
    log_change(name)


def log_change(file):

    action = prompt_action()
    date = prompt_date()
    change = prompt_change()
    log = open(file, "a")
    log.write("\n")
    log.write(action)
    log.write("  ")
    log.write(date)
    log.write("  ")
    log.write(change)
    log.close()
    print("More entries?")
    yesno = input("Y/n\n> ")
    if yesno == "Y" or yesno == "y":
        log_change(file)
    elif yesno == "N" or yesno == "n":
        print("Exiting")
        sys.exit()


def prompt_user():
    print("Which user is making these changes?")
    user = input("User name\n> ")
    return user


# asks for a file path then prints the file to the terminal
def file_read():
    print("File path:")
    file = input("> ")
    try:
        doc = open(file)
        print("File contents:")
        print(doc.read())
    except FileNotFoundError:
        print("File not found")
        main_menu()


# Asks what type if log for file header naming returns Standard or fork
def prompt_log_type():
    print("What type of log is this?")
    print("1: Standard")
    print("2: Fork")
    kind = input("> ")
    if kind == "1":
        print("You entered: Standard")
        print("Is this correct?")
        answer = input("Y/n\n> ")
        if answer == "y" or answer == "Y":
            print("Confirmed")
            return_var = "Standard"
            return return_var
    elif kind == "2":
        print("You entered: Fork")
        print("Is this correct?")
        answer = input("Y/n\n> ")
        if answer == "y" or answer == "Y":
            print("Confirmed")
            return_var = "Fork"
            return return_var


def prompt_version():
    print("What is the application version?")
    version = input("Major.Minor.Patch\n> ")
    return version


# Asks user the date
def prompt_date():
    print("What is the date of the change?")
    date = input("Month Day, Year:\n" + "> ")
    print("You entered: " + date)
    print("Is this correct?")
    correct = input("Y/n:\n" + "> ")
    if correct == "Y" or correct == "y":
        print("Confirmed")
        return date
    elif correct == "n" or correct == "N":
        prompt_date()


# Asks what the change is
def prompt_change():
    print("What is the change?")
    change = input("Change:\n" + "> ")
    print("You entered: " + change)
    print("Is this correct?")
    correct = input("Y/n:\n" + "> ")
    if correct == "Y" or correct == "y":
        print("Confirmed")
        return change
    elif correct == "n" or correct == "N":
        prompt_change()


# Asks what action was taken for the current entry
def prompt_action():
    print("What did you do?")
    print("1: Added")
    print("2: Removed")
    print("3: Fixed")
    print("4: Cancel")
    action = input("> ")
    if action == "1":
        print("You selected action: Added")
        print("Is this correct?")
        correct = input("Y/n:\n" + "> ")
        if correct == "Y" or correct == "y":
            print("Confirmed")
            return "Added"
        elif correct == "n" or correct == "N":
            print("Denied")
            prompt_action()
        else:
            print("Error")
            prompt_action()
    elif action == "2":
        print("You selected action: Removed")
        print("Is this correct?")
        correct = input("Y/n:\n" + "> ")
        if correct == "Y" or correct == "y":
            print("Confirmed")
            return "Removed"
        elif correct == "n" or correct == "N":
            print("Denied")
            prompt_action()
        else:
            print("Error")
            prompt_action()
    elif action == "3":
        print("You selected action: Fixed")
        print("Is this correct?")
        correct = input("Y/n:\n" + "> ")
        if correct == "Y" or correct == "y":
            print("Confirmed")
            return "Fixed"
        elif correct == "n" or correct == "N":
            print("Denied")
            prompt_action()
        else:
            print("Error")
            prompt_action()
    elif action == "4":
        print("Exiting")
        sys.exit()
    else:
        print("Error")
        prompt_action()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
