from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

# Banco de dados
def init_db():
    conn = sqlite3.connect('ocorrencias.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS ocorrencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            descricao TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    nome = request.form['nome']
    endereco = request.form['endereco']
    descricao = request.form['descricao']
    
    conn = sqlite3.connect('ocorrencias.db')
    c = conn.cursor()
    c.execute('INSERT INTO ocorrencias (nome, endereco, descricao) VALUES (?, ?, ?)', (nome, endereco, descricao))
    conn.commit()
    conn.close()
    
    return redirect(url_for('visualizar'))

@app.route('/visualizar')
def visualizar():
    conn = sqlite3.connect('ocorrencias.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ocorrencias')
    ocorrencias = c.fetchall()
    conn.close()
    
    return render_template('visualizar.html', ocorrencias=ocorrencias)

if __name__ == '__main__':
    app.run(debug=True)
