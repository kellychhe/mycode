#!/usr/bin/python3
"""Alta3 Research - API challenge """
# http://api.open-notify.org/iss-now.json

# import requests to use to get API info
import requests
# import datetime to use for epoch time conversion
import datetime
# import geolocation to use for finding city and country
import reverse_geocoder as rg

# store url in a variable for readability
url = "http://api.open-notify.org/iss-now.json"

# create main function
def main():
    
    # Send an HTTPS GET request to the ISS API and decode it. then store it in response variable
    resp = requests.get(url).json()
    
    # display the information from request
    latitude = resp["iss_position"]["latitude"]
    longitude = resp["iss_position"]["longitude"]
    time = datetime.datetime.fromtimestamp(resp["timestamp"]).strftime("%Y-%m-%d %H:%M:%S") 
    geocoder = rg.search( (latitude, longitude) )
    city = geocoder[0]["name"]
    country = geocoder[0]["cc"]

    print(f'''
    CURRENT LOCATION OF THE ISS:
    TIMTESTAMP: {time}
    LAT: {latitude}
    LON: {longitude}
    CITY/COUNTRY: {city}, {country}
    ''')

# call main function
if __name__ == "__main__":
    main()
