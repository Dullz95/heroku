from flask import Flask
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    return  response
@app.route('/catagories',methods=['GET'])
def get_catagories():
    api_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(api_url).json()
    return '<pre style="word-wrap: break-word; white-space: pre-wrap;">{}</pre>'.format(response)

if __name__=="__main__":
    app.debug=True
    app.run()
