import requests

def fetch_fear_and_greed_index():
    url = "https://api.alternative.me/fng/"
    response = requests.get(url)
    data = response.json()

    value = data['data'][0]['value']
    value_classification = data['data'][0]['value_classification']
    print('______________________________________')
    print(f"Fear and Greed Index Value: {value}")
    print(f"Classification: {value_classification}")
    print('______________________________________')

if __name__ == "__main__":
    fetch_fear_and_greed_index()
