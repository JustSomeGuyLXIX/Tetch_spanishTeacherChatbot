
from arrayInput import *
from activities import *
from spanishTest import test
from transES import tslate

def menu():
    print("\nThere are five activities prepared for you")
    print("These are: greetings, feelings, sports, opinions, and conversation enders. We can also leave and do something else.")
    while True:
        print("\nWhat to you want to do?")
        ans = input("")
     
        if checkResponse(ans,("greetings","greeting","greets","hello","hellos","hello's","greet")):
            print("You've chosen to do the Greetings Activity.")
            Greetings()
        elif checkResponse(ans, ("feelings","emotions","feel")):
            print("You've chosen to do the Feelings Activity.")
            Feelings()

        elif checkResponse(ans, ("sports","outdoors","event","events","football","basketball","tennis","handball","sport")):
            print("You've chosen to do the Sports Activity.")
            Sports()

        elif checkResponse(ans, ("opinions","reasons","opinion","reason")):
            print("You've chosen to do the Opinions Activity.")
            Opinions()

        elif checkResponse(ans, ("conversation enders","enders","convo enders","ender")):
            print("You've chosen to do the Conversation enders Activity.")
            ConvoEnders()

        elif checkResponse(ans, ("leave","something else","go back","exit","bye","adios","chao","bessos")):
            print("\nOkay, what do you want to do instead?")
            return
        else:
            print("I didn't understand what you said.")
    

print("Hello, my name is Tetch, and i'm your Spanish teacher.\nWhat would you like to do?")
while True:
    ans = input("")

    if checkResponse(ans, ("activities","activity")):
        menu()
    elif checkResponse(ans, ("translate", "translation", "help")):
        tslate()
        print("\nWhat would you like to do?")
    elif checkResponse(ans, ("test","quiz")):
        test()
    elif checkResponse(ans, ("leave","exit","bye","adios","adiós","chao","bessos")):
        print("Chao!")
        exit()
    else:
        print("\nSorry I don't understand what you're saying")



