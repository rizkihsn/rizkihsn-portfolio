from flask import Flask, render_template, request, flash, redirect, url_for
import datetime  # tambahkan import ini

app = Flask(__name__)
app.secret_key = 'super-secret-key-ubah-ini-ya'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash(f'Terima kasih {name}! Pesanmu sudah terkirim.', 'success')
        return redirect(url_for('index') + '#contact')
    
    current_year = datetime.datetime.now().year
    
    return render_template('index.html', current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True)