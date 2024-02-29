#author: David Tokar

import time
print("What would you like me to call you")
name = input("")
#code wont run without this, tho it should once everything is in one file
# Corey has changed it so name will = an input so it can suit any user.
#  David changed it, so chatbot seems less forgetful

def acGreetings(q):
#q stands for question
    print("You chose Greetings.")
    time.sleep(2)
    print("In this activity, we'll go over some greetings and conversation starters.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity.")
    #explaination of what the activity is about.
    time.sleep(2)

    print("""
feel free to copy/paste these to use these as a reference
    Hola               Hello
    Buenos dias        Good morning
    Buenas tardes      Good afternoon
    Buenas noches      Good evening/night
    Como estás?        How are you?
    Señor___           Mr(name)
    Señora___          Mrs(name)
    """)
    time.sleep(7)

    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (accents aren't necessary either)\n")
    #accents aren't necessary, so people don't need to cheat, and since I plan accents to be necessary in the higher difficulties.
    while q == 1:
        time.sleep(2)
        print("What is your title?")
        print("{¿Cuál es tu título?}")
        ans = input("")
        ans = ans.lower()
        if ans in ["senor","señor"]:
            print("Hola señor", name)
            time.sleep(1.5)
            print("(Spanish titles aren't capitalized, except at the beginning of a sentence or when abbreviated)\n")
            q = 2
            #ensures that they get to the next question.
        elif ans in ["senora","señora"]:
            print("Hola senora", name)
            time.sleep(1.5)
            print("Spanish titles aren't capitalized, except at the beginning of a sentence or when abbreviated\n")
            q = 2
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")
            #validation

    while q == 2:
        time.sleep(2)
        print("Keeping in mind the current time, how would you greet someone?")
        print("{Teniendo en cuenta la hora actual, ¿cómo saludarías a alguien?}")
        ans = input("")
        ans = ans.lower()

        if ans in ["buenos dias"]:
            print("I hope you slept well")
            print("{Espero que hayas dormido bien}")
            time.sleep(1.5)
            print("(Buenos is masculine, wheras buenas is feminine. However there are situations where you always use a specific one.)\n")
            q = 3
        elif ans in ["buenas tardes"]:
            print("I hope your lunch tasted great")
            print("{Espero que tu almuerzo haya sido delicioso}")
            time.sleep(1.5)
            print("(Buenos is masculine, wheras buenas is feminine. However there are situations where you always use a specific one.)\n")
            q = 3
        elif ans in ["buenas noches"]:
            print("Make sure you have a full night's rest")
            print("(Asegúrate de tener una noche de descanso completa)")
            time.sleep(1.5)
            print("Buenos is masculine, wheras buenas is feminine. However there are situations where you always use a specific one.\n")
            q = 3
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    
    while q == 3:
        time.sleep(2)
        print("What am I saying?")
        print("(¿Que estoy diciendo?)\n")
        time.sleep(1.5)
        
        print("¿cómo estás?")
        ans = input("")
        ans = ans.lower()

        if ans in ["how are you?"]:
            print("I'm doing great thanks")
            print("(Estoy muy bien gracias)\n")
            q = 4
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again (Remember to put a ?)")
            print("(Intentar otra vez)\n")

    while q == 4:
        time.sleep(2)
        print("Hola señor")
        ans = input("")
        ans = ans.lower()

        if ans in ["hello sir"]:
            print("Hola", name, "\n")
            q = 5
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:    
            print("Try again")
            print("(Intentar otra vez)\n")
    
    while q == 5:
        time.sleep(2)
        print("How do you say this?")
        print("(¿como se dice esto?)\n")
        time.sleep(1.5)
        print("How are you mrs")
        ans = input("")
        ans = ans.lower()
        
        if ans in ["como estas señora","como estas senora"]:
            print("Estoy muy bien gracias\n")
            time.sleep(1.5)
            
            print("Well done! You have completed this activity")
            print("(¡Bien hecho! Has completado esta actividad)\n")
            time.sleep(3)
            break
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")
            

def acFeelings(q):
    print("You chose Feelings.")
    time.sleep(2)
    print("In this activity, we'll go over some ways to express your feelings.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity.")
    time.sleep(2)

    print("""
feel free to copy/paste these to use these as a reference
    Estoy                        I'm/I am
    Me siento                     I feel
    Me siento como un/una___      I feel like a(m/f___noun)
    Feliz                         Happy
    Aburrido/Aburrida             Bored(m/f)
    Nervioso/Nerviosa             Nervous(m/f)
    Increíble                     Incredible/amazing
    Enojado/Enojada               Angry(m/f)
    """)
    time.sleep(7)

    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (accents aren't necessary either)\n")
          
    while q == 1:
        time.sleep(2)
        print("what emotion are you right now?")
        print("(¿Qué emoción estás ahora?)")
        ans = input("")
        ans = ans.lower()

        if ans in ["feliz","increíble"]:
            print("I'm glad that you're happy,", name)
            print("(Estoy contento/contenta  de que estés feliz,", name,")\n")
            q = 2
        elif ans in ["aburrido","aburrida","enojado","enojada","nervioso","nerviosa"]:
            print("I hope you feel better soon,", name)
            print("(Espero que pronto te sientas mejor,", name,")\n")
            q = 2
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again, make sure to only include the emotion")
            print("(Intentar otra vez)\n")

    while q == 2:
        time.sleep(2)
        print("What emotion did the last movie you watch make you feel?")
        print("(¿Qué emoción te hizo sentir la última película que viste?)")
        ans = input("")
        ans = ans.lower()

        if ans in ["feliz","increíble"]:
            print("Must have been a good movie then")
            print("(Debe haber sido una buena pelicula entonces)\n")
            q = 3
        elif ans in ["aburrido","aburrida","enojado","enojada"]:
            print("Must have been a bad movie then")
            print("(Debe haber sido una mala película entonces)\n")
            q = 3
        elif ans in ["nervioso","nerviosa"]:
            print("interesting")
            print("(interesante)\n")
            q = 3
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 3:
        time.sleep(2)
        print("what am I saying")
        print("(¿Que estoy diciendo?)\n")
        time.sleep(1.5)
        
        print("Estoy feliz")
        ans = input("")
        ans = ans.lower()

        if ans in ["i am happy","i'm happy","im happy"]:
            print("I'm happy too")
            print("(Yo también estoy felíz)\n")
            q = 4
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 4:
        time.sleep(2)
        print("Me siento como una princesa")
        ans = input("")
        ans = ans.lower()

        if ans in ["i feel like a princess"]:
            print("Correct!,", name)
            print("(¡Correcto!/¡Correcta!",name,")\n")
            q = 5
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 5:
        print("How do you say this?")
        print("¿como se dice esto? \n")
        time.sleep(1.5)
        
        print("I feel nervous (masculine)")
        ans = input("")
        ans = ans.lower()

        if ans in ["me siento nervioso"]:
            print("It's okay to feel nervous about things")
            print("(Está bien sentirse nervioso/nerviosa por las cosas)\n")
            time.sleep(1.5)
            
            print("\nWell done! You have completed this activity")
            print("(¡Bien hecho! Has completado esta actividad)\n")
            time.sleep(3)
            break
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")
        

def acSports(q):
    print("You chose Sports.")
    time.sleep(2)
    print("In this activity, we'll go over some ways to talk about sports.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity.")
    time.sleep(2)

    print("""
feel free to copy/paste these to use these as a reference
    Veo              I watch
    Yo juego         I play
    No veo           I don't watch
    Yo no jeugo      I don't play
    Fútbol           Football
    Baloncesto       Basketball
    Tenis            Tennis
    Balonmano        Handball
    """)
    time.sleep(7)

    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (accents aren't necessary either)\n")
          
    while q == 1:
        time.sleep(2)
        print("What sport do you play?")
        print("(¿Que deporte juegas?)")
        ans = input("")
        ans = ans.lower()

        if ans in ["yo juego fútbol","yo juego futbol"]:
            print("Football is the most popular sport in Spain")
            print("(El fútbol es el deporte más popular en España)\n")
            q = 2
        elif ans in ["yo juego tenis"]:
            print("There are many tennis courts in Spain")
            print("(Hay muchas pistas de tenis en España)\n")
            q = 2
        elif ans in ["yo juego baloncesto"]:
            print("Basketball is the second most popular sport in Spain")
            print("(El baloncesto es el segundo deporte más popular en España)\n")
            q = 2
        elif ans in ["yo juego balonmano"]:
            print("The Spanish national team have won 2 world championships")
            print("(La selección española ha ganado 2 campeonatos del mundo)\n")
            q = 2
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 2:
        time.sleep(2)
        print("What sport do you not watch?")
        print("(¿Qué deporte no ves?)")
        ans = input("")
        ans = ans.lower()

        if ans in ["no veo fútbol","no veo futbol"]:
            print("A lot of people watch it passionately")
            print("(Mucha gente lo mira apasionadamente)\n")
            q = 3
        elif ans in ["no veo tenis"]:
            print("I prefer playing it")
            print("(Prefiero jugarlo)\n")
            q = 3
        elif ans in ["no veo baloncesto"]:
            print("There's a lot of tall people in basketball")
            print("(Hay mucha gente alta en el baloncesto)\n")
            q = 3
        elif ans in ["no veo balonmano"]:
            print("I'm assuming that you've not heard of handball before")
            print("(Supongo que no has oído hablar del balonmano antes)\n")
            q = 3
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 3:
        time.sleep(2)
        print("what am I saying")
        print("(¿Que estoy diciendo?)\n")
        time.sleep(1.5)
            
        print("Veo balonmano")
        ans = input("")
        ans = ans.lower()

        if ans in ["i watch handball"]:
            print(name, "if you don't know what handball is, then your homework is to find that out.")
            print(name, "(si no sabes qué es el balonmano, tu tarea es averiguarlo.)\n")
            q = 4
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 4:
        time.sleep(2)
        print("Juego y veo fútbol")
        ans = input("")
        ans = ans.lower()

        if ans in ["i play and watch football"]:
            print("I'm happy you got that!")
            print("(¡Estoy feliz de que lo hayas conseguido!)\n")
            q = 5
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 5:
        time.sleep(2)
        print("How do you say this?")
        print("(¿como se dice esto?)\n")
        time.sleep(1.5)
                
        print("I watch basketball and i play tennis")
        ans = input("")
        ans = ans.lower()

        if ans in ["veo baloncesto y juego tenis"]:
            print("Yes", name, "that was great")
            print("(si", name,"eso estuvo genial)")
            time.sleep(1.5)
            
            print("\nWell done! You have completed this activity")
            print("¡Bien hecho! Has completado esta actividad\n")
            time.sleep(3)
            break
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")
                
def acOpinions(q):
    print("You chose Opinions.")
    time.sleep(2)
    print("In this activity, we'll go over some ways to express opinions and reasons.")
    time.sleep(3)
    print("Make sure you do the Feelings and Sports activities.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity.")
    
    print("""
feel free to copy/paste these to use these as a reference
    Me gusta (el/las)                        I like
    No me gusta (el/las)                     I dislike
    Me encanta  (el/las)                     I love
    Odio (el/las)                            I hate
    No tengo una opinion sobre (el/las)      I don't have an opinion on
    Ver                                      Watching (when used in the middle of a sentence
    Jugar al                                 Playing (when used in the middle of a sentence
    porque                                   Because
    Me hace                                  It makes me
    """)
    time.sleep(7)

    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (accents aren't necessary either)")
    time.sleep(1.5)
    print("during this activity, only el will be used, as the four sports mentioned in the sports activities use el.\n")

    while q == 1:
        time.sleep(2)
        print(name, "What sport(except football) do you like?")
        print("(",name, "¿Qué deporte (excepto el fútbol) te gusta?)")
        ans = input("")
        ans = ans.lower()

        if ans in ["me gusta el tenis"]:
            print("Me too! Anyway...")
            print("(¡Yo también! De todos modos...)\n")
            q = 2
        elif ans in ["me gusta el baloncesto"]:
            print("Oh really, anyway...")
            print("(Oh, de verdad, de todos modos...)\n")
            q = 2
        elif ans in ["me gusta el balonmano"]:
            print("I'm actually pretty decent at basketball. Anyway...")
            print("(De hecho, soy bastante decente en el baloncesto. De todos modos...)\n")
            q = 2
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 2:
        time.sleep(2)
        print("I heard you hate football, why?")
        print("(Escuché que odio el fútbol, ¿por qué?)")
        ans = input("")
        ans = ans.lower()

        if ans in ["odio el futbol porque me hace aburrido","odio el futbol porque me hace aburrida","odio el fútbol porque me hace aburrido","odio el fútbol porque me hace aburrida"]:
            print("I understand")
            print("(Entiendo)\n")
            q = 3
        elif ans in ["odio el futbol porque me hace nervioso","odio el futbol porque me hace nerviosa","odio el fútbol porque me hace nervioso","odio el fútbol porque me hace nerviosa"]:
            print("Makes sense")
            print("(Tiene sentido)\n")
            q = 3
        elif ans in ["odio el futbol porque me hace enojado","odio el futbol porque me hace enojada","odio el fútbol porque me hace enojado","odio el fútbol porque me hace enojada"]:
            print("Funnily enough,", name,"it feels like many enjoy football for that reason.")
            print("(Curiosamente,", name,"parece que muchos disfrutan del fútbol por ese motivo.)\n")
            q = 3
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 3:
        time.sleep(2)
        print("what am I saying")
        print("¿Que estoy diciendo?\n")
        time.sleep(1.5)
            
        print("Me encanta el baloncesto")
        ans = input("")
        ans = ans.lower()

        if ans in ["i love basketball"]:
            print("You can do it!")
            print("(¡Puedes hacerlo!)\n")
            q = 4
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 4:
        time.sleep(2)
        print("No me gusta jugar al fútbol porque me hace aburrido")
        ans = input("")
        ans = ans.lower()

        if ans in ["i dislike playing football because it makes me bored"]:
            print("Only one more question!")
            print("(¡Solo una pregunta más!)\n")
            q = 5
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 5:
        time.sleep(2)
        print("How do you say this?")
        print("(¿como se dice esto?)\n")
        time.sleep(1.5)
                
        print("I love watching tennis because it makes me happy")
        ans = input("")
        ans = ans.lower()

        if ans in ["me encanta ver tenis porque me hace feliz"]:
            print("Perfect!")
            print("(¡Perfecto/perfecta!)\n")
            time.sleep(1.5)
            
            print("\nWell done! You have completed this activity")
            print("(¡Bien hecho! Has completado esta actividad)\n")
            time.sleep(3)
            break
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
             print("Try again")
             print("(Intentar otra vez)\n")

def acConvEnd(q):
    print("You chose Conversation enders.")
    time.sleep(2)
    print("In this activity, we'll go over some ways to end a conversation.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity.")
    time.sleep(1.5)

    print("""
feel free to copy/paste these to use these as a reference")
    Bueno...                Well...(also means good in depending on context
    Me tengo que ir         I have to go
    Hablemos más tarde      Let's talk later
    Nos vemos               See you
    Adiós                   Bye(more formal)
    Chao                    Bye(less formal)
    Bessos                  Kisses(very informal)
    """)
    time.sleep(7)
  
    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (accents aren't necessary either)\n")
  
    while q == 1:
        time.sleep(2)
        print("How would you say bye to a stranger?")
        print("(¿Cómo le dirías adiós a un extraño/una extraña?)")
        ans = input("")
        ans = ans.lower()

        if ans in ["adiós""adios"]:
            print("By the way, saying 'bye' in English also works, as many Spanish people also use it.")
            print("(Por cierto, decir 'bye' en inglés también funciona, ya que muchos españoles también lo usan.)\n")
            q = 2
        elif ans in ["chao"]:
            print("By the way, saying 'bye' in English also works, as many Spanish people also use it.")
            print("(Por cierto, decir 'bye' en inglés también funciona, ya que muchos españoles también lo usan.)\n")
            q = 2
        elif ans in ["bessos"]:
            print("Kisses is only used with people you are close to.")
            print("(Besos solo se usa con personas cercanas.)\n")
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 2:
        time.sleep(2)
        print("What would you say just before saying bye?")
        print("(¿Qué dirías justo antes de decir adiós?)")
        ans = input("")
        ans = ans.lower()

        if ans in ["nos vemos","bueno nos vemos"]:
            print("Yor're doing great!")
            print("(Lo estás haciendo genial)\n")
            q = 3
        elif ans in ["hablemos más tarde","hablemos mas tarde","bueno hablemos más tarde","bueno hablemos mas tarde"]:
            print("Amazing!")
            print("(Asombroso/asombrosa)\n")
            q = 3
        elif ans in ["me tengo que ir","bueno me tengo que ir"]:
            print("Good job!")
            print("(¡Buen trabajo!)\n")
            q = 3
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 3:
        time.sleep(2)
        print("What am I saying?")
        print("(¿Que estoy diciendo?)\n")
        time.sleep(1.5)
            
        print("Bueno me tengo que ir")
        ans = input("")
        ans = ans.lower()

        if ans in ["well i have to go"]:
            print("Goodbye,", name,"just kidding, next question!")
            print("(Adiós,", name,"es broma, ¡siguiente pregunta!)\n")
            q = 4
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again")
            print("(Intentar otra vez)\n")

    while q == 4:
        time.sleep(2)
        print("Hablemos más tarde, chao")
        ans = input("")
        ans = ans.lower()

        if ans in ["lets talk later, bye","let's talk later, bye"]:
            print("Next question!")
            print("(¡Siguiente pregunta!)\n")
            q = 5
        elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
            print("ok")
            break
        else:
            print("Try again, make sure you include the comma")
            print("(Intentar otra vez)\n")

        while q == 5:
            time.sleep(2)
            print("How do you say this?")
            print("(¿como se dice esto?)\n")
                
            print("Well, I have to go, kisses")
            ans = input("")
            ans = ans.lower()

            if ans in ["bueno, me tengo que ir, bessos","bueno,me tengo que ir,bessos"]:
                print("Remember,", name," only use 'bessos' if you're talking to a friend")
                print("(Recuerda,", name," solo usa 'bessos' si estás hablando con un/una amigo.)")
                time.sleep(1.5)
                
                print("\nWell done! You have completed this activity")
                print("¡Bien hecho! Has completado esta actividad\n")
                time.sleep(3)
                break
            elif ans in ["exit","leave","stop","something else","i want to exit","i want to leave","i want to stop","i want to do something else"]:
                print("ok")
                break
            else:
                 print("Try again")
                 print("(Intentar otra vez)\n")


print("There are five activities I have made for you.")
time.sleep(1.5)
#wont print instantly - more like a conversation.
#can be removed once teams/discord is implemented
print("These are: greetings, feelings, sports, opinions, conversation enders. We can also do something else.")
time.sleep(1)
while True:
    print("What do you want to do")
    dec = input("")
    dec = dec.lower()
    #dec as in decision
    
    for word in ["greetings","greets","hello","hellos","hello's"]:
        if word in dec:
            print("ok")
            acGreetings(1)

    for word in ["feelings","emotions"]:
        if word in dec:
             print("ok")
             acFeelings(1)

    for word in ["sports","outdoors","event","events","football","basketball","tennis","handball"]:
        if word in dec:
            print("ok")
            acSports(1)

    for word in ["opinions","reasons"]:
        if word in dec:
            print("ok")
            acOpinions(1)

    for word in ["conversation enders","enders","convo enders"]:
        if word in dec:
            print("ok")
            acConvEnd(1)
    
    for word in ["leave","something else","go back","exit","bye","adios","adiós","chao","bessos"]:
        if word in dec:
            print("ok")
            import main