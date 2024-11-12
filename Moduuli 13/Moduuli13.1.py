from flask import Flask,request,Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku1>')

def alkuluku(luku1):
    tila = True
    luku1 = int(luku1)
    
    try:
        if luku1 < 2:
            tila = False
        
        for jako in range(2,luku1):
            if luku1 % jako == 0:
                tila = False

        tilakoodi = 200
        vastaus = {
            'Numero': luku1,
            'isPrime':tila
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            'Tilakoodi': tilakoodi,
            'Virhe': 'Alkuluvun tarkastus epäonnistui. Syötä luku'
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus,status=tilakoodi,mimetype='application/json')

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000) # localhost == 127.0.0.1