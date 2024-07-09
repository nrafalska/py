import requests
class CountryInfo:
    def __init__(self):
        self.api_url = "https://restcountries.com/v3.1/all"
    def fetch_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    def display_data(self, data):
        if data:
            for country in data:
                name = country.get('name', {}).get('common', 'N/A')
                capital = country.get('capital', ['N/A'])[0]
                flag_url = country.get('flags', {}).get('png', 'N/A')
                print(f"Name: {name}\tCapital: {capital}\tFlag: {flag_url}")
        else:
            print("Failed to retrieve data")

if __name__ == "__main__":
    country_info = CountryInfo()
    data = country_info.fetch_data()
    country_info.display_data(data)
