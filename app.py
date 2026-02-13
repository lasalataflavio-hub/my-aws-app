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

import time

@app.route('/stress')
def stress():
    # Facciamo girare la CPU per 60 secondi filati
    end_time = time.time() + 60  
    while time.time() < end_time:
        _ = 1000 * 1000  # Operazione inutile per tenere occupato il core
    return "CPU stressata per 60 secondi!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)