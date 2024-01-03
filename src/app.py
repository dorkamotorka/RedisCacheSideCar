import redis
import json
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.from_object('config.Config')  # Set the configuration variables to the flask application
r = redis.Redis()

@app.route("/universities")
def get_universities():
    cache = r.get(f"{request.url}")
    if cache is not None:
        return json.loads(cache)
    
    # In case of cache miss
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    resp = requests.get(f"{API_URL}{search}")
    r.set(f"{request.url}", json.dumps(resp.json()))
    return resp.json()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
