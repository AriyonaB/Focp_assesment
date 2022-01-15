print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.")

name = input('What is your name?')                              #Input name from user

if "arthur" in name.lower():                                    #Input is lowered and If King passes, access is granted without further questions
    print('My liege! You may pass!')

else:
    seek = input('What do you seek?')                           #If Knight passes, he is asked further questions

    if "grail" not in seek.lower():                             #Input is loweres and If it isn't "The Grail" the Knight seeks, he is denied access
        print('Only those who seek the Grail may pass!')

    else:
        color = input('What is your favourite color?')          #If the Knight does not know his favourite colour, he has to face the Gorge of Eternal Peril

        if color[0].lower()==name[0].lower():                   #string of color is lowered and Knight's favourite colour must start with the first letter of his name
            print('You may pass!')                              #If answer is correct, he is allowed to pass

        else:
            print('Incorrect! You must now face the Gorge of Eternal Peril')