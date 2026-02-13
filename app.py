from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Recupera il nome dell'host (che su EC2 corrisponde spesso all'ID istanza)
    hostname = socket.gethostname()
    return f"""
    <h1>Ciao da AWS!</h1>
    <p>Questa risposta arriva dall'istanza: <b>{hostname}</b></p>
    <p>Prova a ricaricare la pagina per vedere se il Load Balancer ti sposta su un'altra istanza.</p>
    """

@app.route('/health')
def health():
    # Endpoint fondamentale per il Load Balancer
    return "OK", 200

@app.route('/stress')
def stress():
    # Un miliardo di cicli invece di 10 milioni
    count = 0
    for i in range(10**8): 
        count += i
    return "Carico CPU generato pesantemente!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)