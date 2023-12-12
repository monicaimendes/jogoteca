from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)


@app.route("/inicio")
def ola():
    # jogos = ["Tetris", "Minecraft", "It Takes Two"]

    jogo1 = Jogo("Tetris", "Puzzle", "Atari")
    jogo2 = Jogo("Minecraft", "Platform", "XBOX")
    jogo3 = Jogo("It Takes Two", "Coop", "PS5")
    lista = [jogo1, jogo2, jogo3]
    return render_template("lista.html", titulo="Jogos", jogos=lista)


app.run()
