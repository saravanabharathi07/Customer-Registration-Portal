def show_menu():
    print("\n--- Notes App ---")
    print("1. View All Notes")
    print("2. Add Note")
    print("3. Overwrite Notes")
    print("4. Search Note")
    print("5. Delete Note")
    print("6. Exit")

def view_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            if not notes:
                print("No notes yet!")
            else:
                print("\nYour Notes:")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("No notes found! Start adding some.")

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note added successfully!")

def overwrite_notes():
    note = input("Enter your new notes (this will ERASE old ones): ")
    with open("notes.txt", "w") as f:
        f.write(note + "\n")
    print("Notes overwritten successfully!")

def search_note():
    keyword = input("Enter keyword to search: ")
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            found = [note.strip() for note in notes
                     if keyword.lower() in note.lower()]
            if found:
                print("\nSearch Results:")
                for n in found:
                    print("-", n)
            else:
                print("No matching notes found.")
    except FileNotFoundError:
        print("No notes file found!")

def delete_note():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
        if not notes:
            print("No notes to delete.")
            return
        view_notes()
        choice = int(input("Enter note number to delete: "))
        if 1 <= choice <= len(notes):
            deleted = notes.pop(choice - 1)
            with open("notes.txt", "w") as f:
                f.writelines(notes)
            print(f"Deleted note: {deleted.strip()}")
        else:
            print("Invalid choice.")
    except FileNotFoundError:
        print("No notes file found!")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        view_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        overwrite_notes()
    elif choice == "4":
        search_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        print("Exiting Notes App... Bye bruh 👋")
        break
    else:
        print("Invalid choice! Please try again.")