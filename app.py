from flask import Flask,render_template
import requests
app = Flask(__name__)
@app.route('/')
def home():
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()
        setup = data['setup']
        punchline = data['punchline']
        return render_template('index.html',setup=setup,punchline=punchline)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)