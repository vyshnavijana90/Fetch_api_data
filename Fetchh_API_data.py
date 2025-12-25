import requests

# ---------------- WEATHER API (Open-Meteo - No API Key) ----------------
def fetch_weather(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_res = requests.get(geo_url)

    if geo_res.status_code != 200 or not geo_res.json().get("results"):
        print("City not found.")
        return

    location = geo_res.json()["results"][0]
    lat, lon = location["latitude"], location["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    weather_res = requests.get(weather_url)
    data = weather_res.json()["current_weather"]

    print("\nWeather Information")
    print("-------------------")
    print(f"City        : {city}")
    print(f"Temperature : {data['temperature']}°C")
    print(f"Wind Speed  : {data['windspeed']} km/h")


# ---------------- NEWS API (Hacker News Search - No API Key) ----------------
def fetch_news(keyword):
    news_url = f"https://hn.algolia.com/api/v1/search?query={keyword}"
    response = requests.get(news_url)
    data = response.json()["hits"]

    if not data:
        print("No news found.")
        return

    print("\nLatest News")
    print("-----------")
    for article in data[:5]:
        print(f"\nTitle : {article.get('title')}")
        print(f"Author: {article.get('author')}")
        print(f"URL   : {article.get('url')}")


# ---------------- CRYPTO API (CoinGecko - No API Key) ----------------
def fetch_crypto(coin):
    crypto_url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": coin.lower()
    }

    response = requests.get(crypto_url, params=params)
    data = response.json()

    if not data:
        print("Cryptocurrency not found.")
        return

    coin_data = data[0]

    print("\nCrypto Price Information")
    print("------------------------")
    print(f"Name  : {coin_data['name']}")
    print(f"Price : ${coin_data['current_price']}")
    print(f"Market Cap : ${coin_data['market_cap']}")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\nMulti-API Data Fetching Project")
        print("1. Weather Information")
        print("2. News Search")
        print("3. Cryptocurrency Price")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            city = input("Enter city name: ")
            fetch_weather(city)

        elif choice == "2":
            keyword = input("Enter keyword to search news: ")
            fetch_news(keyword)

        elif choice == "3":
            coin = input("Enter crypto name (bitcoin, ethereum): ")
            fetch_crypto(coin)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
