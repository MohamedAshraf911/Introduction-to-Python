import os

def display_menu():
    print("** Personal Diary Application **")
    print("1. Write a new entry")
    print("2. View previous entries")
    print("3. Exit")

def write_entry():
    entry = input("Write your entry: ")
    try:
        # Open the file in append mode and write the entry to it
        file = open("diary.txt", "a") 
        file.write(entry + "\n")
        print("Entry saved successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_entries():
    try:
        if not os.path.exists("diary.txt"):
            print("No entries found.")
            return
        file = open("diary.txt", "r")
        entries = file.readlines()
        if entries:
            print("Previous Entries:")
            for entry in entries:
                print(entry.strip())
        else:
            print("No entries found.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            write_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

main()