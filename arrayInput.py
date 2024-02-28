def correctAnswer(ans, words):
    ans = ans.lower()
    if ans in words:
        return True
    else:
        return False

def checkResponse(ans, group):
    ans = ans.lower()
    
    for word in group:
        if word in ans:
            return True
    else:
        return False
