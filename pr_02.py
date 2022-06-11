def game() :
    return 2875
score = game()

with open("high_score.txt") as f :
    highscore=f.read()

if highscore=='':
    with open("high_score.txt","w") as f :
        f.write(str(score))

elif int(highscore) < score:
    with open("high_score.txt","w") as f :
        f.write(str(score))