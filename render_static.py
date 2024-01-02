from flask import Flask, render_template
from flask.templating import render_template as flask_render_template
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

# Diretório onde será salvo o HTML estático
output_dir = 'docs'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Rota para gerar e salvar HTML estático para cada voucher
for day, voucher_text in vouchers.items():
    with app.app_context():
        rendered_html = flask_render_template('index.html', voucher=voucher_text)
    
    # Substitua "/" por "_" no nome do arquivo para evitar problemas com caminhos
    day_filename = day.replace("/", "_") + ".html"
    
    output_file = os.path.join(output_dir, day_filename)
    
    with open(output_file, 'w') as f:
        f.write(rendered_html)

print("Versão estática gerada com sucesso!")
