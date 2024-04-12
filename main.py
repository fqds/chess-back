from flask import Flask

app = Flask(__name__)

class Game():
    def __init__(self):
        self.newGame()

    def newGame(self):
        self.white_turn = True
        self.board = ["r1", "h1", "b1", "k1", "q1", "b1", "h1", "r1", "p1", "p1", "p1", "p1", "p1", "p1", "p1", "p1", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "p2", "p2", "p2", "p2", "p2", "p2", "p2", "p2", "r2", "h2", "b2", "k2", "q2", "b2", "h2", "r2"]

game = Game()

@app.route("/api/connect")
def apiConnect():
    return {"board": game.board, "white_turn": game.white_turn}

if __name__ == "__main__":
    app.run("0.0.0.0", "8083")