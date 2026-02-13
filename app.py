from flask import Flask
import socket
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Recupera il nome dell'host (ID istanza su EC2)
    hostname = socket.gethostname()
    return f"""
    <html>
        <head><title>AWS Demo</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>Ciao da AWS! 🚀</h1>
            <p>Questa risposta arriva dall'istanza: <b style="color: blue;">{hostname}</b></p>
            <p>Stato sistema: <span style="color: green;">In funzione</span></p>
            <hr>
            <p>Prova la rotta <b>/stress</b> per testare l'Auto Scaling.</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    # Endpoint fondamentale per il Load Balancer
    return "OK", 200

@app.route('/stress')
def stress():
    # Stress test: tiene impegnata la CPU per circa 45 secondi
    # Usiamo un mix di calcolo e tempo per evitare il timeout immediato
    hostname = socket.gethostname()
    end_time = time.time() + 45  
    
    print(f"Inizio stress test su {hostname}")
    
    count = 0
    while time.time() < end_time:
        # Operazione di calcolo intensiva
        for i in range(1000):
            count += i
        # Un micro-riposo per evitare che il processo diventi zombie
        time.sleep(0.001) 
        
    return f"<h1>Stress test completato!</h1><p>Istanza: {hostname}</p>"

if __name__ == "__main__":
    # Fondamentale: host 0.0.0.0 e porta 80 per AWS
    app.run(host='0.0.0.0', port=80)