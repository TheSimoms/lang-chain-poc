import sys

from flask import Flask, render_template, request

sys.path.append('..')

from lang_chain_poc import still_spørsmål

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        spørsmål = request.form['spørsmål']

        if not spørsmål:
            return render_template('index.html', feil='Du må stille et spørsmål!')

        svar = still_spørsmål(spørsmål)

        return render_template('index.html', spørsmål=spørsmål, svar=svar)
