from flask import Flask
import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='tatu',
         password='',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kentta(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    vastaus = {
        "icao" : icao,
        "name" : tulos[0][0],
        "municipality" : tulos[0][1]
    }

    return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)