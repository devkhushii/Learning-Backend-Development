import pandas as pd
import requests
from bs4 import BeautifulSoup

# Initialize empty lists to store product details
productName = []
Prices = []
Description = []

# Loop through the pages to scrape data
for i in range(1, 11):  # Loop from page 1 to page 10
    # Construct the URL for each page of search results
    url = f"https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_5_2_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_5_2_na_na_na&as-pos=5&as-type=RECENT&suggestionId=iphone&requestId=c9d40dd3-9525-491e-8a82-cb46a556e0e8&as-searchtext=ip&page={i}"
    
    # Send a GET request to the URL
    r = requests.get(url)
    
    # Parse the HTML content of the response
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')

    # Find all the product names on the page and append to the list
    names = soup.find_all("div", class_="KzDlHZ")
    for name in names:
        productName.append(name.text)

    # Find all the product prices on the page and append to the list
    prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")
    for price in prices:
        Prices.append(price.text)

    # Find all the product descriptions on the page and append to the list
    descriptions = soup.find_all("div", class_="_6NESgJ")
    for desc in descriptions:
        Description.append(desc.text)

# Create a DataFrame to store the scraped data
df = pd.DataFrame({"productName": productName, "Prices": Prices, "Description": Description})

# Print the DataFrame (optional)
print(df)

# Write the DataFrame to a CSV file named "Iphone.csv" without index column
df.to_csv("Iphone.csv", index=False)
