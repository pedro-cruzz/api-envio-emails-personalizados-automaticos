# 🚀 IJA Email Service API

Uma API REST desenvolvida em Python com **Flask** para o envio de e-mails transacionais e notificações de leads totalmente personalizadas para o ecossistema **Oceano Azul / IJA Drones**.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Flask:** Framework web para a criação da API.
* **Resend SDK:** Motor de disparo de e-mails de alta performance.
* **Jinja2:** Engine para renderização de templates HTML dinâmicos.
* **Python-dotenv:** Gerenciamento de variáveis de ambiente e segurança.

## 📋 Funcionalidades

* [x] Recebimento de dados via requisição POST (JSON).
* [x] Renderização de e-mails altamente estilizados e responsivos.
* [x] Integração com a logo oficial da IJA Drones.
* [x] Tratamento de erros e logs de disparo.

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/api-email-resend.git](https://github.com/seu-usuario/api-email-resend.git)
cd api-email-resend
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```
RESEND_API_KEY=sua_chave_api
FLASK_ENV=development
```

### 4. Iniciar o servidor
```bash
python app.py
```

O servidor estará disponível em `http://localhost:5000`

## 📨 Endpoint Principal

**POST** `/send-email`

### Body (JSON)
```json
{
    "to": "destinatario@example.com",
    "subject": "Assunto",
    "template": "lead_notification",
    "variables": {
        "nome": "João",
        "mensagem": "Seu conteúdo aqui"
    }
}
```

### Resposta de Sucesso
```json
{
    "success": true,
    "message": "E-mail enviado com sucesso",
    "email_id": "uuid-123"
}
```

## 📁 Estrutura do Projeto

```
api-email/
├── app.py
├── templates/
│   └── emails/
├── .env
├── requirements.txt
└── README.md
```

## 📝 Licença

Este projeto é licenciado sob a MIT License.

