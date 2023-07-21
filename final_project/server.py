from flask import Flask, render_template, request, jsonify
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)

# Chave de API e URL do IBM Language Translator
API_KEY = '0EEFeAC_Ta2tLgB_9qqHfh6kG1x5B8dJijFFATwgqpUk'
URL = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/f163c6bd-ae6e-4c23-87cb-eb8244e17331'
# Configurar o autenticador e o cliente do IBM Language Translator
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2021-09-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a tradução
@app.route('/traduzir', methods=['POST'])
def traduzir():
    texto = request.json['texto']
    target = request.json['target']
    
    # Determina a língua de origem com base no idioma alvo
    source = 'en' if target == 'fr' else 'fr'

    # Traduz o texto
    resultado = language_translator.translate(
        text=texto,
        source=source,
        target=target
    ).get_result()

    texto_traduzido = resultado['translations'][0]['translation']

    return jsonify({'texto': texto_traduzido})

if __name__ == '__main__':
    app.run(debug=True)