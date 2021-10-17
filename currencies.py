import requests
class currencies():
	def get_currencies():
		url = "https://api.frankfurter.app/currencies"

		response = requests.get(url)
		jsonverisi = response.json()
		return dict(jsonverisi).keys()

