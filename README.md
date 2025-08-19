# 📍 LocalizaEmpresasAPI

API RESTful para consulta de dados empresariais via **CNPJ** e obtenção da **geolocalização** com base no endereço cadastrado.  
Utiliza a [ReceitaWS](https://www.receitaws.com.br/) para obter informações da empresa e o [Nominatim OpenStreetMap](https://nominatim.openstreetmap.org/) para geocodificação.

---

## 🚀 Como funciona

A API realiza os seguintes passos:

1. Recebe um **CNPJ** como parâmetro de rota.
2. Consulta os dados da empresa via ReceitaWS.
3. Extrai o endereço cadastrado.
4. Realiza a geocodificação com a API do Nominatim (OpenStreetMap).
5. Retorna as informações estruturadas, incluindo link para o Google Maps.

---

## 📦 Tecnologias Utilizadas

- Python 3.7+
- Flask
- Requests
- python-dotenv
- ReceitaWS API
- OpenStreetMap Nominatim API

---

## 🔧 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/Alexandre0lemos/LocalizaEmpresasAPI.git
cd LocalizaEmpresasAPI
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

#### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

- Crie um arquivo .env com o seguinte conteúdo:

- EMAIL=seu_email@dominio.com

### ▶️ Executando a API

```bash
python app.py
```