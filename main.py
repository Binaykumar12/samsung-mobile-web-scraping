import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://swappa.com/buy/phones"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all phone listings
listings = soup.find_all('div', class_='listing')

# Extract phone names and prices
for listing in listings:
    # Extract name
    name = listing.find('a', class_='listing-title').text.strip()

    # Extract price
    price = listing.find('span', class_='price').text.strip()

    # Print or store the results as needed
    print(f"Name: {name}, Price: {price}")
