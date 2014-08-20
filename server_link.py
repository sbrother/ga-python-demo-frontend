import requests
import json

BACKEND_URL = "http://127.0.0.1:5000"

def get_sentiment(text):
	payload = {'q': text}
	r = requests.get(BACKEND_URL + '/sentiment', params=payload)
	if r.status_code != 200:
		raise IOError("Server not reachable.")

	result = r.json()
	return result.get('polarity')
