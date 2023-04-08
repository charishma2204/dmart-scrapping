import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the Dmart store locator page
url = "https://www.dmart.in/store-locator"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the store details on the page
store_details = soup.find_all("div", class_="store-detail")

# Create a list to store the extracted data
data = []

# Loop through each store detail and extract the required data
for store in store_details:
    name = store.find("div", class_="store-name").text.strip()
    address = store.find("div", class_="store-address").text.strip()
    timings = store.find("div", class_="store-timings").text.strip()
    phone = store.find("div", class_="store-phone").text.strip()
    
    # Extract the latitude and longitude values
    map_link = store.find("a", class_="view-on-map")["href"]
    lat_long = map_link.split("@")[1].split(",")[0:2]
    lat = lat_long[0]
    long = lat_long[1]
    
    data.append([name, address, timings, phone, lat, long])

# Write the extracted data to a CSV file
with open("dmart_stores.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Address", "Timings", "Phone", "Latitude", "Longitude"])
    writer.writerows(data)
