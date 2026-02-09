import os
import resend
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
resend.api_key = os.getenv("RESEND_API_KEY")

@app.route('/disparar-email', methods=['POST'])
def enviar():
    # 1. Pegamos os dados enviados pelo formulário/JSON
    data = request.json
    
    # 2. Renderizamos o HTML e guardamos na variável html_estilizado
    # Certifique-se que o nome do arquivo seja exatamente o que está na pasta templates
    html_estilizado = render_template(
        'email_contato.html', 
        nome_form=data.get('nome'), 
        email_form=data.get('email_cliente'), 
        tel_form=data.get('telefone'), 
        mensagem_form=data.get('mensagem')
    )

    try:
        resend.Emails.send({
            "from": "Sistema IJA <onboarding@resend.dev>",
            "to": "ijadronessystem@gmail.com",
            "subject": f"Lead: {data.get('nome')}",
            "html": html_estilizado
        })
        return jsonify({"mensagem": "E-mail enviado!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)