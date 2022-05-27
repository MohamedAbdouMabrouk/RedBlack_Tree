from RBTreeClasses import *

run = True
run1 = False
while run:
    print("What do you want to do:")
    print("L:Load The English dictionary file.")
    print("D:Load anther dictionary file")
    print("E:Exit")

    user = input()
    if user == "E":
        run = False
    else:
        if user == 'L':
            tree = LoadFileClass.load_dictionary("EN-US-Dictionary.txt")
        elif user == 'D':
            print("Please enter the dictionary path:")
            path = input()
            tree = LoadFileClass.load_dictionary(path)
            if not tree:
                print("Invalid input!")
                continue
        else:
            print("Invalid input!")
            continue
        run1 = True
        print(f"Tree size: {tree.size}\nTree height: {tree.height(tree.root)}")

    while run1:
        print("What do you want to do:")
        print("I:Insert in the dictionary")
        print("S:Search in the dictionary")
        print("P:Print Size and height:")
        print("B:Back")
        user1 = input()
        if user1 == 'I':
            print("Please enter the word you want to insert in the dictionary:")
            tree.insert(input())
            print(f"Tree size: {tree.size}\nTree height: {tree.height(tree.root)}")

        elif user1 == 'S':
            print("Please enter the word you want to search for in the dictionary:")
            if tree.search(input()).value:
                print("Yes")
            else:
                print("No")
        elif user1 == 'P':
            print(f"Tree size: {tree.size}\nTree height: {tree.height(tree.root)}")

        elif user1 == 'B':
            run1 = False
        else:
            print("Invalid input!")
