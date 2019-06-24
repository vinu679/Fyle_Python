import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/fly')
def fly():
    r=requests.get('https://vast-shore-74260.herokuapp.com/banks?city=MUMBAI')
    details = r.json()
    return render_template('index.html',  result= details)

if __name__ == '__main__':
   app.run(debug= True)
