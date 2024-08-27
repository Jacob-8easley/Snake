from turtle import Turtle
import datetime
ALIGNMENT = "center"
FONT= ("courier",20,"normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.hi_score("./highscore.txt")
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.draw_score()
        self.hideturtle()
        #self.draw_hi_score()  
       

    def game_over(self):
        self.goto(10,0)
        self.write(arg=f"GAME OVER",move=False, align=ALIGNMENT,font=FONT)

    def draw_hi_score(self): 
        self.write(arg=f"HIGH SCORE: {self.high_score}",move=False, align=ALIGNMENT,font=FONT)  

    def draw_score(self): 
        self.write(arg=f"SCORE BOARD: {self.score} HIGH SCORE: {self.high_score}",move=False, align=ALIGNMENT,font=FONT) 


    def increase_score(self):
        self.score += 1
        self.clear()
        self.draw_score()

    def hi_score(self,text_file):
        f = open(text_file,"r")
        high_score = f.readlines()[-2]
        return high_score
    


    def update_highscore(self,):
        with open("./highscore.txt", "a") as f:
            if str(self.score) > str(self.high_score):
                f.write(str(f"\n{self.score}\n"))
                f.write(str(f"{datetime.datetime.now()}\n"))


        