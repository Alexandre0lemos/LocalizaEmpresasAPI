import requests
import re
from flask import Flask, jsonify
import os
from dotenv import load_dotenv

URL_API = "https://nominatim.openstreetmap.org/search"

app = Flask(__name__)
load_dotenv()

@app.route("/api/v1/localizacao/empresas/<cnpj>", methods=["GET"])
def localizar_por_cnpj():
    cnpj = "17.339.293/0001-39"
    
    try:  
        dados = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{re.sub(r'\D', '', cnpj)}").json()
                
        numero = dados["numero"]
        logradouro = dados["logradouro"]
        
        street = f"{logradouro} {numero}".strip()
        
        if type(numero) == str and numero.strip() == "":
            street = logradouro
        
        params = {
            "street": street,
            "city": dados["municipio"],
            "state": dados["uf"],
            "country": "Brazil",
            "format": "json",
            "limit": 1
        }
        
        headers = {
            "User-Agent": f"SearchLocation/1.0 ({os.getenv("EMAIL")})"
        }
        
        response = requests.get(url=URL_API, params=params, headers=headers)
        
        data = response.json()
        
        if len(data) > 0:         
            dataJson = {
                "status": 200,
                "body": {
                    "Empresa_Buscada": {
                    "Nome": f"{dados["nome"]}",
                    "Fantasia": f"{dados["fantasia"]}"
                },
                
                "Endereço": f"{street}, {dados["municipio"]}, {dados["uf"]}",
                
                "geolocalizacao" : {
                    "Latitude": f"{data[0]["lat"]}",
                    "Longitude": f"{data[0]["lon"]}"  
                },
                "linkMaps": f"https://www.google.com/maps?q={data[0]['lat']},{data[0]['lon']}",
                }
            }
            
            return jsonify(dataJson)
        else:
            return jsonify({
                "status": 422
            })
            
    except requests.exceptions.ConnectionError:
        return jsonify({"status": 503, "error": "Erro de conexão com a API."})
    except requests.exceptions.Timeout:
        return jsonify({"status": 504, "error": "Tempo de resposta excedido."})
    except requests.exceptions.HTTPError as err:
        return jsonify({"status": err.response.status_code, "error": err.response.reason})
    except Exception as e:
        return jsonify({"status": 500, "error": f"Erro inesperado: {str(e)}"})
        

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
