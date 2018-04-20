from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def poke(query):
	url = 'http://pokeapi.co/api/v2/pokemon/' + query
	r = requests.get(url)

	poke_data = r.json()
	print(poke_data["id"])
	print(poke_data["forms"][0]['name'])
	
	return render_template('pokemon.html')

if __name__ == '__main__':
    app.run()
