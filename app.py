from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
DB_PATH = "signos.db"


def descobrir_signo(data_str):
    data = datetime.strptime(data_str, "%Y-%m-%d")
    mes = data.month
    dia = data.day

    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricórnio"
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Peixes"
    return None


def buscar_signo(nome):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM signos WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    conn.close()
    return dict(resultado) if resultado else None


def registrar_consulta(data_nascimento, signo):
    """Registra a consulta no banco com data e hora"""
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO consultas (data_nascimento, signo, data_hora)
        VALUES (?, ?, ?)
    """, (data_nascimento, signo, data_hora))
    conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    data = request.form.get("data_nascimento")

    if not data:
        return render_template("resultado.html", erro="Data não informada.")

    nome_signo = descobrir_signo(data)

    if not nome_signo:
        return render_template("resultado.html", erro="Não foi possível determinar o signo.")

    info = buscar_signo(nome_signo)

    if not info:
        return render_template("resultado.html", erro="Signo não encontrado no banco de dados.")

    # ===== REGISTRA A CONSULTA =====
    registrar_consulta(data, nome_signo)

    return render_template("resultado.html", signo=info)


@app.route("/historico")
def historico():
    """Página opcional para ver as consultas registradas"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM consultas 
        ORDER BY data_hora DESC 
        LIMIT 50
    """)
    consultas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return render_template("historico.html", consultas=consultas)


if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        print("Banco não encontrado! Execute: python criar_banco.py")
    app.run(debug=True)