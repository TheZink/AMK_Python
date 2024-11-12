from flask import Flask,request,Response
import json
import icao_haku

app = Flask(__name__)
@app.route('/kentta/<icao>')

def lentokentta(icao):
    icao = icao

    try:
        tilakoodi = 200
        vastaus = {
            'ICAO': icao_haku.etsi_lentoasema(icao)[0],
            'Name': icao_haku.etsi_lentoasema(icao)[1],
            'Municipality': icao_haku.etsi_lentoasema(icao)[2]
        }

    
    except ValueError:
        tilakoodi = 400
        vastaus = {
            'Tilakoodi': tilakoodi,
            'Virhe': 'Virheellinen ICAO-koodi'
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus,status=tilakoodi,mimetype='application/json')

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)