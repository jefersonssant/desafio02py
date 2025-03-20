from flask import Flask,request,jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def pagina_home():
  return "<h1>Olá, seja bem-vindo! Esta é uma API de Livros"

def init_db():
  with sqlite3.connect("database.db") as conn:
    conn.execute("""
      CREATE TABLE IF NOT EXISTS LIVROS(
                 id INTERGER PRIMARY KEY AUTOINCREMENT,
                 titulo TEXT NOT NULL,
                 categoria TEXT NOT NULL,
                 autor TEXT NOT NULL,
                 image_url TEXT NOT NULL)
    """)

init_db()

@app.route("/doar", methods = ["POST"])
def doar():
  dados = request.get_json()
  titulo = dados.get("titulo")
  categoria = dados.get("categoria")
  autor = dados.get("autor")
  image_url = dados.get("image_url")

  if not titulo or not categoria or not autor or not image_url:
    return jsonify({"erro":"Todos os campos são obrigatórios"}), 400
  
  with sqlite3.connect("database.db") as conn:
    conn.execute(f"""
      INSERT INTO LIVROS (titulo,categoria,autor,image_url) VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
    """)
  
  conn.commit()

  return jsonify({"mensagem":"Livro cadastrado com sucesso"}), 201

if __name__ == "__main__":
  app.run(debug = true)