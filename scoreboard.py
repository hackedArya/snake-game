from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0 , 280)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align= ALIGN, font= FONT )

    def game_over(self):
        self.goto(0 , 0)

        self.write(f"Game Over", align= "center", font= FONT )

        

    def increase_score(self):
        
        self.score +=1
        self.clear()
        self.update_score()
        
        


        

        