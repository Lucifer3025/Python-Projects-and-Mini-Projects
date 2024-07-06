import random as r
import sys
import os

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit()
    except Exception as e:
        print(f"An error occurred while reading the file {filepath}: {e}")
        sys.exit()

def read_leaderboard():
    if not os.path.exists(lfile):
        return {}
    
    leaderboard = {}
    try:
        file=open("leaderboard.txt","w")
        for line in file:
                name, score = line.strip().split(",")
                leaderboard[name] = int(score)
    except FileNotFoundError:
        print(f"File not found: {lfile}")
    except Exception as e:
        print(f"An error occurred while reading the leaderboard file: {e}")
    return leaderboard

def write_leaderboard(leaderboard):
    try:
        file=open("leaderboard.txt","w")
        for name, score in leaderboard.items():
                file.write(f"{name},{score}\n")
    except Exception as e:
        print(f"An error occurred while writing to the leaderboard file: {e}")

def add_or_update_leaderboard(name, score):
    leaderboard = read_leaderboard()
    if name in leaderboard:
        leaderboard[name] += score
    else:
        leaderboard[name] = score
    write_leaderboard(leaderboard)

def display_leaderboard():
    leaderboard = read_leaderboard()
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)
    print("Leaderboard:")
    for i, (name, score) in enumerate(sorted_leaderboard, start=1):
        print(f"{i}. {name}: {score} points")

def check(ss, list):
    if ss == wr and ss in list:
        print("\nCongratulations!! Your answer is correct.\n")
        return True
    else:
        print("\nSorry, your answer is incorrect.\nThe right answer is:", wr, "\n")
        return False

def hint(ss, list):
    if hints > 0:
        if list == l3:
            print("The hint for the word is:")
            print("The word starts with:", ss[0])
        elif list == l5:
            print("The hint for the word is:")
            print("The word starts with:", ss[0], "and ends with:", ss[len(ss) - 1])
        else:
            print("The hint for the word is:")
            print("The word starts with:", ss[0], ", the 5th letter is:", ss[4], "and ends with:", ss[len(ss) - 1])
    else:
        print("You have no more hints left for this level!!")

def scramble(word):
    word = list(word)
    r.shuffle(word)
    return "".join(word)

l3 = [line.strip().lower() for line in read_file("C:\\Users\\ADMIN\\Desktop\\mp3.txt")]
l5 = read_file("C:\\Users\\ADMIN\\Desktop\\mp25.txt")[0].split()
l5 = [i.lower() for i in l5]
l8 = [line.strip().lower() for line in read_file("C:\\Users\\ADMIN\\Desktop\\mp7.txt")]
i = 0
x = 0
o = 0
h = 0
z = 0
l = 0
hints = 3
lfile = "C:\\Users\\ADMIN\\OneDrive\\Documents\\Ifacet\\Mini Projects\\leaderboard.txt"
try:
 id = input("Enter the player's name=")
except KeyboardInterrupt:
    print("Keyboard interupet occured! Enter the name again:\n")
    id = input("Enter the player's name=")
    
    
print("Let's play jumbled words game!!\n# Rules:-\n-> There will be 3 levels 'Easy' 'Medium' and 'Hard'.\n-> Each correct answer will give you 1 point.\n-> Words will start becoming hard as you progress to upper levels.\n-> You will be provided 1 chance for each question.\n-> There will be 10 words in total on each level.\n-> You will be provided with 3 hints for each level.\n")

print("Level 1: difficulty(Easy)\n")
while i < 10:
    wr = r.choice(l3)
    m = scramble(wr)
    print("Your jumbled word is:", m)
    h1 = 2
    if hints > 0:
        try:
            print("Hints remaining =", hints, "\nDo you want a hint??")
            h1 = int(input("Press '1' for 'YES' and '2' for 'NO'="))
        except ValueError:
            print("Invalid input.\nPlease enter '1' for 'YES' or '2' for 'NO'.")
            continue
    try:
        if h1 == 2:
            i1 = str(input("Enter your answer="))
            s = check(i1, l3)
            i += 1
            if s == True:
                x += 1
        else:
            hint(wr, l3)
            hints -= 1
            i1 = str(input("Enter your answer="))
            s = check(i1, l3)
            i += 1
            if s == True:
                x += 1
    except ValueError:
        print("Invalid input. Please enter a valid word.")
        continue

print("Your final score of level 1 is =", x)

try:
    cho = int(input("\nIf you want to play the next level press '1' and to exit press '0'.\nEnter your choice="))
except ValueError:
    print("Invalid input. Exiting the game.")
    cho = 0

if cho == 1:
    hints = 3
    print("Level 2: difficulty(Medium)\n")
    while z < 10:
        wr = r.choice(l5)
        m = scramble(wr)
        print("Your jumbled word is:", m)
        h1 = 2
        if hints > 0:
            try:
                print("Hints remaining =", hints, "\nDo you want a hint??")
                h1 = int(input("Press '1' for 'YES' and '2' for 'NO'="))
            except ValueError:
                print("Invalid input. Please enter '1' for 'YES' or '2' for 'NO'.")
                continue
        try:
            if h1 == 2:
                i1 = str(input("Enter your answer="))
                n = check(i1, l5)
                z += 1
                if n == True:
                    l += 1
            else:
                hint(wr, l5)
                hints -= 1
                i1 = str(input("Enter your answer="))
                n = check(i1, l5)
                z += 1
                if n == True:
                    l += 1
        except ValueError:
            print("Invalid input. Please enter a valid word.")
            continue

    print("Your final score of level 2 is =", l)
else:
    add_or_update_leaderboard(id, x)
    print("\nThank you for playing!!\n-> Do you want to check the leaderboard? If 'Yes' press '1' and if 'NO' press '0'")
    try:
        lb = int(input("Enter your choice="))
        if lb == 1:
            display_leaderboard()
    except ValueError:
        print("Invalid input. Exiting the game.")
    sys.exit()

try:
    cho = int(input("\nIf you want to play the next level press '1' and to exit press '0'.\nEnter your choice="))
except ValueError:
    print("Invalid input. Exiting the game.")
    cho = 0

if cho == 1:
    hints = 3
    print("Level 3: difficulty(Hard)\n")
    while o < 10:
        wr = r.choice(l8)
        m = scramble(wr)
        print("Your jumbled word is:", m)
        h1 = 2
        if hints > 0:
            try:
                print("Hints remaining =", hints, "\nDo you want a hint??")
                h1 = int(input("Press '1' for 'YES' and '2' for 'NO'="))
            except ValueError:
                print("Invalid input. Please enter '1' for 'YES' or '2' for 'NO'.")
                continue
        try:
            if h1 == 2:
                i1 = str(input("Enter your answer="))
                n = check(i1, l8)
                o += 1
                if n == True:
                    h += 1
            else:
                hint(wr, l8)
                hints -= 1
                i1 = str(input("Enter your answer="))
                n = check(i1, l8)
                o += 1
                if n == True:
                    h += 1
        except ValueError:
            print("Invalid input. Please enter a valid word.")
            continue

    print("Your final score of level 3 is =", h)
    sum2 = x + h + l
    print("Your overall score is =", sum2)
    add_or_update_leaderboard(id, sum2)
    print("\nThank you for playing!!\n-> Do you want to check the leaderboard? If 'Yes' press '1' and if 'NO' press '0'")
    try:
        lb = int(input("Enter your choice="))
        if lb == 1:
            display_leaderboard()
    except ValueError:
        print("Invalid input. Exiting the game.")
    sys.exit()
else:
    sum1 = x + l
    add_or_update_leaderboard(id, sum1)
    print("\nThank you for playing!!\n-> Do you want to check the leaderboard? If 'Yes' press '1' and if 'NO' press '0'")
    try:
        lb = int(input("Enter your choice="))
        if lb == 1:
            display_leaderboard()
    except ValueError:
        print("Invalid input. Exiting the game.")
    sys.exit()
