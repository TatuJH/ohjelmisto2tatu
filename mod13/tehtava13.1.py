from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<temp>')
def alkuluku(temp):
    luku = int(temp)

    on_alkuluku = True
    if luku <= 2:
        on_alkuluku = False
    else:
        for i in range(2, luku):
            if luku % i == 0:
                on_alkuluku = False
                break

    if on_alkuluku:
        vastaus = {
            "number" : luku,
            "isPrime" : "true"
        }
    else:
        vastaus = {
            "number" : luku,
            "isPrime" : "false"
        }

    return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)