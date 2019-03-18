import random
import time
import os


def refresh(chance):
    os.system("cls")
    print("Welcome to hang-man game!")
    if chance == 0:
            print('''
            ###########################################
                               ##
                               ##
                               ##
                              ###
                            ##    ##
                           ## # #  ##
                           ##      ##
                            ##    ##
                              ###
                               #
                               #
                              ###
                             # # #
                            #  #  #
                           #   #   #
                               #
                               #
                              # #
                             #   #
                            #     #
                           #       #
                ''')

    elif chance == 1:
        print('''
        ###########################################
                           ##
                           ##
                           ##
                          ###
                        ##    ##
                       ## # #  ##
                       ##      ##
                        ##    ##
                          ###
                           #
                           #
                          ##
                         # # 
                        #  #  
                       #   #  
                           #
                           #
                          # #
                         #   #
                        #     #
                       #       #
            ''')

    elif chance == 2:
        print('''
        ###########################################
                           ##
                           ##
                           ##
                          ###
                        ##    ##
                       ## # #  ##
                       ##      ##
                        ##    ##
                          ###
                           #
                           #
                           #
                           # 
                           #  
                           #  
                           #
                           #
                          # #
                         #   #
                        #     #
                       #       #
            ''')

    elif chance == 3:
        print('''
        ###########################################
                           ##
                           ##
                           ##
                          ###
                        ##    ##
                       ## # #  ##
                       ##      ##
                        ##    ##
                          ###
                           #
                           #
                           #
                           # 
                           #  
                           #  
                           #
                           #
                          # 
                         #   
                        #     
                       #       
            ''')

    elif chance == 4:
        print('''
        ###########################################
                           ##
                           ##
                           ##
                          ###
                        ##    ##
                       ## # #  ##
                       ##      ##
                        ##    ##
                          ###
                           #
                           #
                           #
                           # 
                           #  
                           #  
                           #
                           #
                        
                          
                            
                              
            ''')

    elif chance == 5:
        print('''
        ###########################################
                           ##
                           ##
                           ##
                          ###
                        ##    ##
                       ## # #  ##
                       ##      ##
                        ##    ##
                          ###
                           
                           
                           
                            
                             
                             
                           
                           
                        
                          
                            
                              
            ''')

    elif chance == 6:
        print('''
        ###########################################
                           ##
                           ##
                           ##
                        
                           
                           
                           
                            
                             
                             
                           
                           
                        
                          
                            
                              
            ''')

def check(reveal, word, answer):
    ans = list(answer)
    word = list(word)

    final_word = []

    for i in range(len(ans)):
        if word[i] == ans[i]:
            final_word.append(ans[i])
        elif ans[i] in reveal:
            final_word.append(ans[i])
        else:
            final_word.append("_")

    final_word = "".join(final_word)
    return(final_word)

final_mark = 0

try:
    while True:
        CHANCES = 6
        word_corpus = open("word_frequency.txt", 'r').read().split("\n")
        clean_corpus = [c.split(" ++&++ ") for c in word_corpus]

        '''
        Rank     Word Part of speech  Frequency   Dispersion
        1        the  a               22038615    0.98
        '''

        nouns = [n[1] for n in clean_corpus if n[2] == 'n']
        needed_nouns = [nn for nn in nouns if len(nn) >= 8]

        test_noun = random.choice(needed_nouns)

        raw_letters = list(test_noun)
        blank_letters = []

        for i in range(int(len(test_noun)/2)-random.randint(0, 2)):
            pos = random.randint(0, len(test_noun)-1)
            blank_letters.append(test_noun[pos])

        final_letters = []

        for r in raw_letters:
            if r in blank_letters:
                r = "_"
            final_letters.append(r)


        final_test = "".join(final_letters)
        right_letter = []
        wrong_letter = []

        while True:
            refresh(CHANCES)
            if CHANCES == 0:
                break
            print("CHANCES LEFT:", CHANCES)
            word = check(right_letter, final_test, test_noun)
            if "_" not in list(word):
                break
            status = False

            print("Guess the word:", word)
            print("Guessed right:", right_letter)
            print("Guessed wrong:", wrong_letter)

            while status is not True:
                usr_guess = input(">>>")


                if usr_guess in right_letter or usr_guess in wrong_letter:
                    print("You guessed it before.")
                    status = False

                elif usr_guess in blank_letters:
                    right_letter.append(usr_guess)
                    status = True

                elif usr_guess not in blank_letters:
                    print("Wrong!!!")
                    wrong_letter.append(usr_guess)
                    time.sleep(1)
                    CHANCES -= 1
                    status = True

        final_mark += len(right_letter)
        print("\n\nFinal mark:", final_mark)
        print("The answer is:", test_noun)

        if CHANCES == 0:
            print("\nGame Over, YOU LOST THE GAME!!!")
            final_mark = 0
        else:
            print("Congrats!")
        os.system("pause")

except:
    open("score.txt", 'r').write(str(final_mark))
    os.system("pause")

