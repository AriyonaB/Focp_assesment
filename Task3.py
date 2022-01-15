import random


def check_email_validity(email, domain):
    if '@' in email:
        name = email.split('@')[0]
        e_domain = email.split('@')[1]
        if email.count('@') == 1 and len(name) >= 2 and domain == e_domain:
            print("{} is valid at {}.".format(email, domain))
            return True
        else:
            print("{} is invalid at {}.".format(email, domain))
            return False
    else:
        print("{} is invalid at {}.".format(email, domain))
        return False


def extract_user(email):
    user = email.split('@')[0].title()
    return user


def random_name():
    name_list = ['James', 'Robert', 'John', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles',
                 'Christopher', 'Daniel', 'Elijah', 'Rose', 'Alberta', 'Gabriel', 'Logan', 'Alan', 'Russel', 'Simon']
    return random.choice(name_list)


def spot_word(question, word):
    if word.lower() in question.lower().replace(".", "").replace("?", "").strip().split(' '):
        return True
    else:
        return False


def chat_system():
    print("Welcome to Pop Chat")
    print("One of our operators will be pleased to help you today.", end="\n\n")

    email = input("Please enter your Poppleton email address: ")

    if not check_email_validity(email, 'pop.ac.uk'):
        exit()
    else:
        username = extract_user(email)
        operator_name = random_name()
        print("Hi, {}! Thank you, and Welcome to PopChat!".format(username))
        print("My name is {}, and it will be my pleasure to help you.".format(
            operator_name))

        ending_word = ["bye", "exit", "goodbye", "end"]
        unmatched_response = ["Hmmm.", "Oh, yes, I see.", "Tell me more."]
        question = input("---> ")

        while True:
            if question.lower().replace(".", "").strip() in ending_word:
                print(
                    "\nThanks, {}, for using PopChat. See you again soon!".format(username))
                exit()
            elif spot_word(question, "library"):
                print("The library is closed today.")
            elif spot_word(question, "Wifi"):
                print("WiFi is excellent across the campus.")
            elif spot_word(question, "deadline"):
                print("Your deadline has been extended by two working days.")
            elif spot_word(question, "coffee"):
                print("POPP Coffee House is open until 8pm this evening.")
            elif spot_word(question, "meeting"):
                print("Your class meeting will be on tommorrow by 10AM online.")
            elif spot_word(question, "holiday"):
                print("Every students will be noticed about holiday some hours ago.")
            elif spot_word(question, "covid"):
                print(
                    "All the academic activities of college have been postponed due to the world wide effect of COVID.")
            else:
                print(random.choice(unmatched_response))
            question = input("---> ")


chat_system()
