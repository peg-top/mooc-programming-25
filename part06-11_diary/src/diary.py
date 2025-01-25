# Write your solution here

while True:
    
    print("1 - add an entry, 2 - read entries, 0 - quit")
    func = int(input("Function: "))

    if func == 1:
        new_entry = input("Diary entry: ")
        with open("diary.txt", "a") as diary_file:
            diary_file.write(new_entry + "\n")
        print("Diary saved")
    elif func == 2:
        print("Entries:")
        with open("diary.txt") as diary_file:
            for line in diary_file:
                print(line.strip())
    else: 
        print("Bye now!")
        break

    print()
