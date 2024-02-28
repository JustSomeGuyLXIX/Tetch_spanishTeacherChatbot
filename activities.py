import time
from arrayInput import *

class help:
    gHelp = "\nHola               Hello\nBuenos dias        Good morning\nBuenas tardes      Good afternoon\nBuenas noches      Good evening/night\nComo estás?        How are you?\nSeñor___           Mr(name)\nSeñora___          Mrs(name)\n"
    fHelp = "\nEstoy                        I'm/I am\nMe siento                     I feel\nMe siento como un/una___      I feel like a(m/f___noun)\nFeliz                         Happy\nAburrido/Aburrida             Bored(m/f)\nNervioso/Nerviosa             Nervous(m/f)\nIncreíble                     Incredible/amazing\nEnojado/Enojada               Angry(m/f)\n"
    sHelp = "\nVeo              I watch\nYo juego         I play\nNo veo           I don't watch\nYo no jeugo      I don't play\nFútbol           Football\nBaloncesto       Basketball\nTenis            Tennis\nBalonmano        Handball\n"
    oHelp = "\nMe gusta (el/las)                        I like\nNo me gusta (el/las)                     I dislike\nMe encanta  (el/las)                     I love\nOdio (el/las)                            I hate\nNo tengo una opinion sobre (el/las)      I don't have an opinion on\nVer                                      Watching (when used in the middle of a sentence\nJugar al                                 Playing (when used in the middle of a sentence\nporque                                   Because\nMe hace                                  It makes me\n"
    cHelp = "\nBueno...                Well...(also means good in depending on context\nMe tengo que ir         I have to go\nHablemos más tarde      Let's talk later\nNos vemos               See you\nAdiós                   Bye(more formal)\nChao                    Bye(less formal)\nBessos                  Kisses(very informal)\n"

class activity(help):
    def __init__(self, q, corAns, rspnses):
        self.q = q
        self.corAns = corAns
        self.rspnses = rspnses
    def showQ(self):
        print(self.q)
    def SingAns(self):
        while True:
            ans = input("")
            if correctAnswer(ans, self.corAns):
                print(self.rspnses)
                break
            elif checkResponse(ans, ("exit","leave","stop","something else")):
                print("ok")
                exit()
            elif checkResponse(ans, ("help")):
                print("which activity do you need help from?")
                while True:
                    ans = input("")
                    if checkResponse(ans, ("greetings","greeting","greets","hello","hellos","hello's","greet")) == True:
                       print(self.gHelp)
                       break
                    elif checkResponse(ans, ("feelings","emotions","feel")) == True:
                       print(self.fHelp)
                       break
                    elif checkResponse(ans, ("sports","outdoors","event","events","football","basketball","tennis","handball","sport")) == True:
                       print(self.sHelp)
                       break
                    elif checkResponse(ans, ("opinions","reasons","opinion","reason")) == True:
                       print(self.oHelp)
                       break
                    elif checkResponse(ans, ("conversation enders","enders","convo enders","ender")) == True:
                       print(self.cHelp)
                       break
                    else:
                        print("which one?")
            else:
                print("Try again")
    def MultAns(self):
        while True:
            ans = input("")
            if correctAnswer(ans, self.corAns):
                pos = 0
                for i in self.corAns:
                    if i == ans:
                        print(self.rspnses[pos])
                        break
                    else:
                        pos += 1
                break
            elif checkResponse(ans, ("exit","leave","stop","something else")):
                print("ok")
                exit()
            elif checkResponse(ans, ("help")):
                print("which activity do you need help from?")
                while True:
                    ans = input("")
                    if checkResponse(ans, ("greetings","greeting","greets","hello","hellos","hello's","greet")) == True:
                       print(self.gHelp)
                       break
                    elif checkResponse(ans, ("feelings","emotions","feel")) == True:
                       print(self.fHelp)
                       break
                    elif checkResponse(ans, ("sports","outdoors","event","events","football","basketball","tennis","handball","sport")) == True:
                       print(self.sHelp)
                       break
                    elif checkResponse(ans, ("opinions","reasons","opinion","reason")) == True:
                       print(self.oHelp)
                       break
                    elif checkResponse(ans, ("conversation enders","enders","convo enders","ender")) == True:
                       print(self.cHelp)
                       break
                    else:
                        print("which one?")
            else:
                print("Try again")

def Greetings():
    hp = help
    g1 = activity("What is your title? {¿Cuál es tu título?}", ("senor","señor", "senora","señora"), ("Hola señor","Hola señor", "Hola señora","Hola señora"))
    g2 = activity("Keeping in mind the current time, how would you greet someone? {Teniendo en cuenta la hora actual, ¿cómo saludarías a alguien?}", ("buenos dias", "buenas tardes", "buenas noches"),("I hope you slept well {Espero que hayas dormido bien}", "I hope your lunch tasted great {Espero que tu almuerzo haya sido delicioso}", "Make sure you have a full night's rest {Asegúrate de tener una noche de descanso completa}"))
    g3 = activity("¿cómo estás?", ("how are you?", "how are you"), "I'm doing great thanks {Estoy muy bien gracias}\n")
    g4 = activity("Hola señor", "hello sir", "¡Hola!\n")
    g5 = activity("How are you mrs", ("como estas señora","como estas senora"), "Estoy muy bien gracias\n")

    print("In this activity, we'll go over some greetings and conversation starters.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity. Memorise the list below")
    #explaination of what the activity is about.
    time.sleep(2)
    print(hp.gHelp)
    time.sleep(6)
    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (though if you are, type 'help' and i'll show you the list again, also accents aren't necessary either)\n")
    #accents aren't necessary, so people don't need to cheat by copying the answer from the list above.
    time.sleep(2)

    g1.showQ()
    g1.MultAns()
    print("Spanish titles aren't capitalized, except at the beginning of a sentence or when abbreviated\n")
    time.sleep(1.5)

    g2.showQ()
    g2.MultAns()
    print("(Buenos is masculine, wheras buenas is feminine. However there are situations where you always use a specific one.)\n")
    time.sleep(1.5)
    
    print("What am I saying? {¿Que estoy diciendo?}\n")
    g3.showQ()
    g3.SingAns()
    time.sleep(1.5)
    
    g4.showQ()
    g4.SingAns()
    time.sleep(1.5)

    print("How do you say this?{¿como se dice esto?)}\n")
    g5.showQ()
    g5.SingAns()
    time.sleep(1.5)

    print("Well done! You have completed this activity {¡Bien hecho! Has completado esta actividad}\n")
    print("What activity do you want to do?")

def Feelings():
    hp = help
    f1 = activity("what emotion are you right now? {¿Qué emoción estás ahora?}", ("feliz","increíble", "increible", "aburrido","aburrida","enojado","enojada","nervioso","nerviosa"),("I'm happy to hear you're well {Me alegro que estes bien}\n","I'm happy to hear you're well {Me alegro que estes bien}\n", "I'm happy to hear you're well {Me alegro que estes bien}\n", "I hope you feel better soon {Espero que pronto te sientas mejor}\n","I hope you feel better soon {Espero que pronto te sientas mejor}\n", "I hope you feel better soon {Espero que pronto te sientas mejor}\n", "I hope you feel better soon {Espero que pronto te sientas mejor}\n","I hope you feel better soon {Espero que pronto te sientas mejor}\n", "I hope you feel better soon {Espero que pronto te sientas mejor}\n"))
    f2 = activity("What emotion did the last movie you watch make you feel? {Debe haber sido una buena pelicula entonces}\n", ("feliz","increíble", "increible", "aburrido","aburrida","enojado","enojada","nervioso","nerviosa"),("Must have been a good movie then {Debe haber sido una buena pelicula entonces}\n","Must have been a good movie then {Debe haber sido una buena pelicula entonces}\n", "Must have been a good movie then {Debe haber sido una buena pelicula entonces}\n", "Must have been a bad movie then {Debe haber sido una mala película entonces}\n","Must have been a bad movie then {Debe haber sido una mala película entonces}\n", "Must have been a bad movie then {Debe haber sido una mala película entonces}\n", "Must have been a bad movie then {Debe haber sido una mala película entonces}\n","interesting {interesante}\n", "interesting {interesante}\n"))
    f3 = activity("Estoy feliz", ("i am happy","i'm happy","im happy"), "Me too! {Yo también}")
    f4 = activity("Me siento como una princesa", "i feel like a princess", "Correct! {¡Correcto!/¡Correcta!}\n")
    f5 = activity("I feel nervous", "me siento nervioso", "It's okay to feel nervous about things {Está bien sentirse nervioso/nerviosa por las cosas}\n")

    print("In this activity, we'll go over some ways to express your feelings.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity. Memorise the list below")
    time.sleep(2)
    print(hp.fHelp)
    time.sleep(6)
    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (though if you are, type 'help' and i'll show you the list again, also accents aren't necessary either)\n")
    time.sleep(2)

    f1.showQ()
    f1.MultAns()
    time.sleep(1.5)

    f2.showQ()
    f2.MultAns()
    time.sleep(1.5)

    print("What am I saying? {¿Que estoy diciendo?}\n")
    f3.showQ()
    f3.SingAns()
    time.sleep(1.5)

    f4.showQ()
    f4.SingAns()
    time.sleep(1.5)

    print("How do you say this?{¿como se dice esto?)}\n")
    f5.showQ()
    f5.SingAns()
    time.sleep(1.5)

    print("Well done! You have completed this activity {¡Bien hecho! Has completado esta actividad}\n")
    print("What activity do you want to do?")

def Sports():
    hp = help
    s1 = activity("What sport do you play? {¿Que deporte juegas?}", ("yo juego fútbol","yo juego futbol", "yo juego tenis", "yo juego baloncesto", "yo juego balonmano"), ("Football is the most popular sport in Spain {El fútbol es el deporte más popular en España}\n","Football is the most popular sport in Spain {El fútbol es el deporte más popular en España}\n", "There are many tennis courts in Spain {Hay muchas pistas de tenis en España}\n", "Basketball is the second most popular sport in Spain {El baloncesto es el segundo deporte más popular en España}\n", "The Spanish national team have won 2 world championships {La selección española ha ganado 2 campeonatos del mundo}\n"))
    s2 = activity("What sport do you not watch? {¿Qué deporte no ves?}", ("no veo fútbol","no veo futbol", "no veo tenis", "no veo baloncesto", "no veo balonmano"), ("A lot of people watch it passionately {Mucha gente lo mira apasionadamente}\n", "I prefer playing it {Prefiero jugarlo}\n", "There's a lot of tall people in basketball {Hay mucha gente alta en el baloncesto}\n", "I'm assuming that you've not heard of handball before {Supongo que no has oído hablar del balonmano antes}\n"))
    s3 = activity("Veo balonmano", "i watch handball", "if you don't know what handball is, then your homework is to find that out. {si no sabes qué es el balonmano, tu tarea es averiguarlo.}\n")
    s4 = activity("Juego y veo fútbol", "i play and watch football", "I'm happy you got that! {¡Estoy feliz de que lo hayas conseguido!}\n")
    s5 = activity("I watch basketball and i play tennis", "veo baloncesto y juego tenis", "Yes, that was great {si, eso estuvo genial}\n")

    print("In this activity, we'll go over some ways to talk about sports.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity. Memorise the list below")
    time.sleep(2)
    print(hp.sHelp)
    time.sleep(6)
    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (though if you are, type 'help' and i'll show you the list again, also accents aren't necessary either)\n")
    time.sleep(2)

    s1.showQ()
    s1.MultAns()
    time.sleep(1.5)

    s2.showQ()
    s2.MultAns()
    time.sleep(1.5)

    print("What am I saying? {¿Que estoy diciendo?}\n")
    s3.showQ()
    s3.SingAns()
    time.sleep(1.5)

    s4.showQ()
    s4.SingAns()
    time.sleep(1.5)

    print("How do you say this?{¿como se dice esto?)}\n")
    s5.showQ()
    s5.SingAns()
    time.sleep(1.5)

    print("Well done! You have completed this activity {¡Bien hecho! Has completado esta actividad}\n")
    print("What activity do you want to do?")

def Opinions():
    hp = help
    o1 = activity("What sport (except football) do you like? {¿Qué deporte (excepto el fútbol) te gusta?}", ("me gusta el tenis", "me gusta el baloncesto", "me gusta el balonmano"), ("Me too! Anyway... {¡Yo también! De todos modos...}\n", "Oh really, anyway... {Oh, de verdad, de todos modos...}\n", "I'm actually pretty decent at basketball. Anyway... {De hecho, soy bastante decente en el baloncesto. De todos modos...}\n"))
    o2 = activity("I heard you hate football, why? {Escuché que odio el fútbol, ¿por qué?}", ("odio el futbol porque me hace aburrido","odio el futbol porque me hace aburrida","odio el fútbol porque me hace aburrido","odio el fútbol porque me hace aburrida","odio el futbol porque me hace nervioso","odio el futbol porque me hace nerviosa","odio el fútbol porque me hace nervioso","odio el fútbol porque me hace nerviosa","odio el futbol porque me hace enojado","odio el futbol porque me hace enojada","odio el fútbol porque me hace enojado","odio el fútbol porque me hace enojada"), ("I understand {Entiendo}\n","I understand {Entiendo}\n","I understand {Entiendo}\n","I understand {Entiendo}\n", "Makes sense {Tiene sentido}\n","Makes sense {Tiene sentido}\n","Makes sense {Tiene sentido}\n","Makes sense {Tiene sentido}\n", "Funnily enough, it feels like many enjoy football for that reason {Curiosamente, parece que muchos disfrutan del fútbol por ese motivo}\n","Funnily enough, it feels like many enjoy football for that reason {Curiosamente, parece que muchos disfrutan del fútbol por ese motivo}\n","Funnily enough, it feels like many enjoy football for that reason {Curiosamente, parece que muchos disfrutan del fútbol por ese motivo}\n","Funnily enough, it feels like many enjoy football for that reason {Curiosamente, parece que muchos disfrutan del fútbol por ese motivo}\n"))
    o3 = activity("Me encanta el baloncesto", "i love basketball", "You can do it! {¡Puedes hacerlo!}\n")
    o4 = activity("No me gusta jugar al fútbol porque me hace aburrido", "i dislike playing football because it makes me bored", "Only one more question! {¡Solo una pregunta más!}\n")
    o5 = activity("I don't have an opinion on tennis", "no tengo una opinion sobre tenis", "Perfect! {¡Perfecto/perfecta!}\n")

    print("In this activity, we'll go over some ways to express opinions and reasons.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity. Memorise the list below")
    time.sleep(2)
    print(hp.sHelp)
    time.sleep(6)
    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (though if you are, type 'help' and i'll show you the list again, also accents aren't necessary either)\n")
    time.sleep(2)

    o1.showQ()
    o1.MultAns()
    time.sleep(1.5)

    o2.showQ()
    o2.MultAns()
    time.sleep(1.5)

    print("What am I saying? {¿Que estoy diciendo?}\n")
    o3.showQ()
    o3.SingAns()
    time.sleep(1.5)

    o4.showQ()
    o4.SingAns()
    time.sleep(1.5)

    print("How do you say this?{¿como se dice esto?)}\n")
    o5.showQ()
    o5.SingAns()
    time.sleep(1.5)

    print("Well done! You have completed this activity {¡Bien hecho! Has completado esta actividad}\n")
    print("What activity do you want to do?")

def ConvoEnders():
    hp = help
    c1 = activity("How would you say bye to a stranger? {¿Cómo le dirías adiós a un extraño/una extraña?}", ("adiós""adios", "chao", "bessos"), ("By the way, saying 'bye' in English also works, as many Spanish people also use it {Por cierto, decir 'bye' en inglés también funciona, ya que muchos españoles también lo usan}\n", "By the way, saying 'bye' in English also works, as many Spanish people also use it {Por cierto, decir 'bye' en inglés también funciona, ya que muchos españoles también lo usan}\n","By the way, saying 'bye' in English also works, as many Spanish people also use it {Por cierto, decir 'bye' en inglés también funciona, ya que muchos españoles también lo usan}\n","By the way, saying 'bye' in English also works, as many Spanish people also use it {Por cierto, decir 'bye' en inglés también funciona, ya que muchos españoles también lo usan}\n", "Kisses is only used with people you are close to {Besos solo se usa con personas cercanas}\n"))
    c2 = activity("What would you say just before saying bye? {¿Qué dirías justo antes de decir adiós?}", ("nos vemos","bueno nos vemos", "hablemos más tarde","hablemos mas tarde","bueno hablemos más tarde","bueno hablemos mas tarde", "me tengo que ir","bueno me tengo que ir"), ("You're doing great! {Lo estás haciendo genial}\n","You're doing great! {Lo estás haciendo genial}\n", "Amazing! {Asombroso/Asombrosa}\n","Amazing! {Asombroso/Asombrosa}\n","Amazing! {Asombroso/Asombrosa}\n","Amazing! {Asombroso/Asombrosa}\n", "Good job! {¡Buen trabajo!}\n","Good job! {¡Buen trabajo!}\n"))
    c3 = activity("Bueno me tengo que ir", "well i have to go", "Goodbye... just kidding, next question! {Adiós... es broma, ¡siguiente pregunta!}\n")
    c4 = activity("Hablemos más tarde, chao", ("lets talk later, bye","let's talk later, bye","lets talk later bye","let's talk later bye"), "Next question! {¡Siguiente pregunta!}\n")
    c5 = activity("Well, I have to go, kisses", ("bueno, me tengo que ir, bessos","bueno,me tengo que ir,bessos","bueno me tengo que ir bessos"), "Remember, only use 'bessos' if you're talking to a friend {Recuerda, solo usa 'bessos' si estás hablando con un/una amigo}\n")

    print("In this activity, we'll go over some ways to end a conversation.\n")
    time.sleep(1.5)
    print("Let me know if you want to stop this activity. Memorise the list below")
    time.sleep(2)
    print(hp.sHelp)
    time.sleep(6)
    print("Now I'm going to ask you questions, try not to use the list above unless you're stuck (though if you are, type 'help' and i'll show you the list again, also accents aren't necessary either)\n")
    time.sleep(2)

    c1.showQ()
    c1.MultAns()
    time.sleep(1.5)

    c2.showQ()
    c2.MultAns()
    time.sleep(1.5)

    print("What am I saying? {¿Que estoy diciendo?}\n")
    c3.showQ()
    c3.SingAns()
    time.sleep(1.5)

    c4.showQ()
    c4.SingAns()
    time.sleep(1.5)

    print("How do you say this?{¿como se dice esto?)}\n")
    c5.showQ()
    c5.SingAns()
    time.sleep(1.5)

    print("Well done! You have completed this activity {¡Bien hecho! Has completado esta actividad}\n")
    print("What activity do you want to do?")