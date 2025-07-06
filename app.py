from flask import Flask, render_template, request
from email_classificador import EmailClassifier
from email_responder import EmailResponder
from leitor_arquivo import FileReader
import os

app = Flask(__name__)

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

email_classificador = EmailClassifier()
responder = EmailResponder(HUGGINGFACE_API_TOKEN)
leitor_arquivo = FileReader()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/classificar", methods=["GET", "POST"])
def classificar():
    conteudo = ""    
    categoria = ""
    resposta_sugerida = ""
    if request.method == "POST":
        texto_digitado = request.form.get("texto", "")
        arquivo = request.files["arquivo"]
        if texto_digitado.strip():
            conteudo = texto_digitado.strip()
        elif arquivo:
            filename = arquivo.filename
            if filename.endswith(".txt"):
                conteudo = arquivo.read().decode("utf-8")
            elif filename.endswith(".pdf"):
                conteudo = leitor_arquivo.read_pdf_file(arquivo)
        if conteudo and conteudo != "Formato de arquivo não suportado":
            categoria = email_classificador.classificar(conteudo)
            resposta_sugerida = responder.gerar_resposta(conteudo, categoria)
        return render_template(
        "resultado.html",
        conteudo=conteudo,
        categoria=categoria,
        resposta=resposta_sugerida)
    return render_template("classificar.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
