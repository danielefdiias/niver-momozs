from flask import Flask, render_template, send_from_directory
import datetime
import os

app = Flask(__name__)

# Dicionário de vouchers
vouchers = {
    "02/01": "Jantar romântico",
    "03/01": "Piquenique no Parque",
    "04/01": "Sessão de Cinema em Casa",
    "05/01": "Dia de Spa em Casa",
    "06/01": "Noite de Jogos na Ludus Luderia",
    "07/01": "Viagem Surpresa (tu só escolhe a data e eu o destino kkk)",
    "08/01": "Caça ao melhor pudim de SP",
    "09/01": "Ir a praça do pôr do sol",
    "10/01": "escapada para um airbnb",
    "11/01": "Noite de Observação de Estrelas",
    "12/01": "Leitura Compartilhada",
    "13/01": "Treino juntos",
    "14/01": "Tour histórico por SP",
    "15/01": "desenhar com tinta",
    "16/01": "Visitar feiras de artesanato",
    "17/01": "café na cama",
}

@app.route('/')
def index():
    today = datetime.datetime.now().strftime("%d/%m")
    current_voucher = vouchers.get(today, "Sem voucher para hoje.")
    return render_template('index.html', voucher=current_voucher)

# Rota para servir arquivos estáticos do diretório 'docs' quando executado localmente
@app.route('/docs/<path:filename>')
def serve_static(filename):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    return send_from_directory(os.path.join(root_dir, 'docs'), filename)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5000)
