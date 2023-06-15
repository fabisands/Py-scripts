print("NOTE: you can enter number zero (0) or just press enter when asking any data to kill task.")
print("Is a woman who commented?")
woman = input("Press Y if yes or N if not: ").lower()
if woman != "0" or woman != "":
    while woman != -3.141592:
        if woman == "y":
            print("Is she talking against male things?")
            w_talking = input("Press Y if yes or N if not: ").lower()
            if w_talking != "0" or w_talking != "":
                while w_talking != -3.141592:
                    if w_talking == "y":
                        print("Has she complained before about men talking against women things?")
                        complain = input("Press Y if yes or N if not: ").lower()
                        if complain != "0" or complain != "":
                            while complain != -3.141592:
                                if complain == "y":
                                    print("Is she feminist?")
                                    feminist = input("Press Y if yes or N if not: ").lower()
                                    if feminist != "0" or feminist != "":
                                        while feminist != -3.141592:
                                            if feminist == "y":
                                                print("Note the irony of all about this and just make a sarcastic and biting joke.")
                                                exit()
                                            elif feminist == "n":
                                                print("Hmph, women! Hahahahaha!")
                                                exit()
                                    else:
                                        print("Task has finished.")
                                        exit()
                                elif complain == "n":
                                    print("Listen to her and try to understand.")
                                    exit()
                                else:
                                    print("Are you dumb or something? I said Y or N, so...")
                                    complain = input("Press Y if yes or N if not: ").lower()
                                    continue
                        else:
                            print("Task has finished.")
                            exit()
                    elif w_talking == "n":
                        print("Make a bow and present your respects to her.")
                        exit()
                    else:
                        print("Are you dumb or something? I said Y or N, so...")
                        w_talking = input("Press Y if yes or N if not: ").lower()
                        continue
            else:
                print("Task has finished.")
                exit()
        elif woman == "n":
            print("Is he talking against male things?")
            m_talking = input("Press Y if yes or N if not: ").lower()
            if m_talking != "0" or m_talking != "":
                while m_talking != -3.141592:
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
            else:
                print("Task has finished.")
                exit()
        else:
            print("Are you dumb or something? I said Y or N, so...")
            woman = input("Press Y if yes or N if not: ")
            continue
else:
    print("Task has finished.")
