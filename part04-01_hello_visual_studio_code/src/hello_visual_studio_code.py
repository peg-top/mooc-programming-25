# Write your solution here

best_editor = "Visual Studio Code"

while True:

    editor = input("Editor: ").lower()

    if editor == best_editor.lower():
        print("an excellent choice!")
        break
    elif editor == "notepad" or editor == "word":
        print("awful")
    else:
        print("not good")