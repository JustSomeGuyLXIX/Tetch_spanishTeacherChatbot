from arrayInput import *
import time

class testQ:
    def __init__(self, q, corAns):
        self.q = q
        self.corAns = corAns
    def showQ(self):
        print(self.q)
    def checkAns(self):
        ans = input("")
        if correctAnswer(ans, self.corAns):
            return True
        else:
            return False

def test():
    mark = 0
    incorAns = []
    q01 = testQ("\nQ1. What would you greet someone?", ("hola","buenos dias","buenas tardes","buenas noches"))
    q02 = testQ("\nQ2. How do you feel right now?", ("me siento feliz","me siento increible","me siento increíble","me siento adurrido","me siento aburrida","me siento nervioso","me siento nerviosa","me siento enojado","me siento enojada"))
    q03 = testQ("\nQ3. Juego y veo tenis", ("i play and watch tennis"))
    q04 = testQ("\nQ4. No tengo una opinion sobre fútbol", ("i don't have an opinion on football", "i have no opinion on football","i dont have an opinion on football"))
    q05 = testQ("\nQ5. Well I have to go, bye (informal)",("bueno me tengo que ir, chao","bueno me tengo que ir chao"))
    q06 = testQ("\nHola.", ("hola","buenos dias","buenas tardes","buenas noches"))
    q07 = testQ("\nComa eastas?", ("estoy feliz","estoy increible","estoy increíble","estoy adurrido","estoy aburrida","estoy nervioso","estoy nerviosa","estoy enojado","estoy enojada"))
    q08 = testQ("\nEstoy feliz. Yo juego balonmano, tu juegas algo?", ("yo juego fútbol", "yo juego futbol", "yo juego tenis", "yo juego baloncesto", "yo juego balonmano"))
    q09 = testQ("\nMe encanta balonmano", ("me encanta", "me gusta", "no me gusta","odio","no tengo una opinion sobre"))
    q10 = testQ("\nBueno me tengo que ir, adiós!", ("nos vemos", "chao", "bessos", "adios", "adiós"))



    print("\nThe test is now beginning, the first 5 questions are exactly like the questions in the activities. The next 5 questions will be formatted like a conversation, so just respond like you would in real life.")
    time.sleep(5)
    q01.showQ()
    if q01.checkAns() == True:
        mark += 1
    else:
        incorAns.append("Q1")

    q02.showQ()
    if q02.checkAns()== True:
        mark +=1
    else:
        incorAns.append("Q2")

    q03.showQ()
    if q03.checkAns()== True:
        mark +=1
    else:
        incorAns.append("Q3")

    q04.showQ()
    if q04.checkAns()== True:
        mark +=1
    else:
        incorAns.append("Q4")

    q05.showQ()
    if q05.checkAns()== True:
        mark +=1
    else:
        incorAns.append("Q5")

    q06.showQ()
    if q06.checkAns() == True:
        mark += 1
    else:
        incorAns.append("Q6")

    q07.showQ()
    if q07.checkAns() == True:
        mark += 1
    else:
        incorAns.append("Q7")

    q08.showQ()
    if q08.checkAns() == True:
        mark += 1
    else:
        incorAns.append("Q8")

    q09.showQ()
    ans = input("")
    if checkResponse(ans, q09.corAns) == True:
        mark += 1
    else:
        incorAns.append("Q9")

    q10.showQ()
    if q10.checkAns() == True:
        mark += 1
    else:
        incorAns.append("Q10")


    print("\nYou got " + str(mark) + "/10 marks")
    if mark == 10:
        print("Perfect score!")
    else:
        print("Good job, however you got these questions incorrect: " + str(incorAns))
        