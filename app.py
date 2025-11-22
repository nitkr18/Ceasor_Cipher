from flask import Flask, render_template, request, flash
from ceasor_cipher import encrypt_message, decrypt_message

app = Flask(__name__)
app.secret_key = 'dev-secret'


@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    result = ''
    shift = 3
    candidates = None

    if request.method == 'POST':
        text = request.form.get('text', '')
        action = request.form.get('action')
        shift_raw = request.form.get('shift', '0')
        try:
            shift = int(shift_raw)
        except Exception:
            flash('Shift must be an integer')
            shift = 0

        if action == 'encrypt':
            result = encrypt_message(text, shift)
        elif action == 'decrypt':
            result = decrypt_message(text, shift)
        elif action == 'bruteforce':
            # produce all 26 possibilities
            candidates = [(i, decrypt_message(text, i)) for i in range(26)]

    return render_template('index.html', text=text, result=result, shift=shift, candidates=candidates)


import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
