from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ('Courier', 15, 'normal')
GAME_OVER_FONT = ('Courier', 20, 'normal')
HS_FILEPATH = r"data.txt"
HS_FILEPATH = str(HS_FILEPATH)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, ALIGNMENT, SCORE_FONT)

        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, ALIGNMENT, SCORE_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HS_FILEPATH, "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, GAME_OVER_FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, ALIGNMENT, SCORE_FONT)

    def get_high_score(self):
        with open(HS_FILEPATH) as file:
            contents = (file.read())
            self.high_score = int(contents)
