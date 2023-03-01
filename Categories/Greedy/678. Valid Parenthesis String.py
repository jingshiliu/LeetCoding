def checkValidString(s: str):
    scoreMin, scoreMax = 0, 0

    for i in s:
        if i == '(':
            scoreMin += 1
            scoreMax += 1
        elif i == ')':
            scoreMin -= 1
            scoreMax -= 1
        else:
            scoreMin -= 1
            scoreMax += 1
            
        if scoreMax < 0:
            return False
    print(scoreMin)
    return scoreMin <= 0


input = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"

print(checkValidString(input))