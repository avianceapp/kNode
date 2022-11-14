"""
Provides linking to the panel. Allows Kosciuszko to function.
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='pages/', static_folder='assets/')


@app.route('/')
def panel():
    return render_template('panel.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
