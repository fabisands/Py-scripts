print("NOTE: you can enter number zero (0) or just press enter when asking any data to kill task.")
print("Is a woman who commented?")
woman = input("Press Y if yes or N if not: ").lower()
while woman != "0" and woman != "":
    if woman == "y":
        print("Is she talking against male things?")
        w_talking = input("Press Y if yes or N if not: ").lower()
        while w_talking != "0" and w_talking != "":
            if w_talking == "y":
                print("Has she complained before about men talking against women things?")
                w_talking = input("Press Y if yes or N if not: ").lower()
                if w_talking == "y":
                    print("Is she feminist?")
                    feminist = input("Press Y if yes or N if not: ").lower()
                    while feminist != "0" and feminist != "":
                        if feminist == "y":
                            print("Note the irony of all about this and just make a sarcastic and biting joke.")
                            exit()
                        elif feminist == "n":
                            print("Hmph, women! Hahahahaha!")
                            exit()
                        else:
                            print("Are you dumb or something? I said Y or N, so...")
                            feminist = input("Press Y if yes or N if not: ").lower()
                            continue
                    if feminist == "0" or feminist == "":
                        print("Task has finished.")
                        exit()
                elif w_talking == "n":
                    print("Listen to her and try to understand.")
                    exit()
                else:
                    print("Are you dumb or something? I said Y or N, so...")
                    w_talking = input("Press Y if yes or N if not: ").lower()
                    continue
            elif w_talking == "n":
                print("Make a bow and present your respects to her.")
                exit()
            else:
                print("Are you dumb or something? I said Y or N, so...")
                w_talking = input("Press Y if yes or N if not: ").lower()
                continue
        if w_talking == "0" or w_talking == "":
            print("Task has finished.")
            exit()
    elif woman == "n":
        print("Is he talking against male things?")
        m_talking = input("Press Y if yes or N if not: ").lower()
        while m_talking != "0" and m_talking != "":
            if m_talking == "y":
                print("Haha! Simp.")
                exit()
            elif m_talking == "n":
                print("Take a beer, mate!")
                exit()
            else:
                print("Are you dumb or something? I said Y or N, so...")
                m_talking = input("Press Y if yes or N if not: ").lower()
                continue
        if m_talking == "0" or m_talking == "":
            print("Task has finished.")
            exit()
    else:
        print("Are you dumb or something? I said Y or N, so...")
        woman = input("Press Y if yes or N if not: ")
if woman == "0" or woman == "":
    print("Task has finished.")
