from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def poke(query):
	
	url = 'http://pokeapi.co/api/v2/pokemon/' + query.lower()
	r = requests.get(url)

	if r.status_code != 200:
		return '<html><body><h1>Sorry No Pokemon Found!</h1></body></html>'
	else:
		poke_data = r.json()
		poke_id = poke_data["id"]
		poke_name = poke_data["forms"][0]['name']
		return render_template('pokemon.html', query=query, name=poke_name, value=poke_id)

if __name__ == '__main__':
    app.run()
