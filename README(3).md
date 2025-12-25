## **#Multi-API Data Fetching Project (Weather, News, Crypto)**

**#Overview**



This Python project fetches real-time data from multiple public APIs.

It retrieves weather information, latest news articles, and cryptocurrency prices, parses JSON responses, and displays the results in a clean, readable format in the terminal.



**#Project Goal**



To demonstrate practical API usage by fetching, filtering, and displaying data from public APIs using Python and the requests library.



**#Features**



Fetch weather information by city name (Open-Meteo API)



Search for news articles by keyword (Hacker News Search API)



Retrieve cryptocurrency prices and market info (CoinGecko API)



Parses JSON responses



Implements search and filtering functionality



Clean and readable terminal output



**#Technologies Used**



Python 3.x



requests library



REST APIs (public, no API keys required)



**#APIs Used**



Weather API – Open-Meteo: https://open-meteo.com



News API – Hacker News Search: https://hn.algolia.com



Crypto API – CoinGecko: https://www.coingecko.com



Project Files

multi\_api\_project.py

README.md

weather\_output.png

news\_output.png

crypto\_output.png



How to Run

1\. Create a virtual environment

python -m venv api\_env



2\. Activate the virtual environment



Windows:



api\_env\\Scripts\\activate





Mac/Linux:



source api\_env/bin/activate



3\. Install required module

pip install requests



4\. Run the script

python multi\_api\_project.py



Sample Output

Weather

City        : Hyderabad

Temperature : 29.4°C

Wind Speed  : 11.2 km/h



News

Title  : Open-source AI tools are transforming software development

Author : johndoe

URL    : https://example.com/article



Crypto

Name       : Bitcoin

Price      : $42650

Market Cap : $835000000000



Conclusion



This project demonstrates practical API integration using Python, including real-time data fetching, JSON parsing, and search/filter functionality.

It highlights skills useful for backend development, automation, and data analysis.





