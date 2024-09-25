import requests
import time

# Your Google Maps API key
API_KEY = 'AIzaSyDhw3gGILyAztXg4-xbVweyHe4N2ay7i9k'

def get_coordinates(city_name, api_key):
    """Get latitude and longitude of the specified city using Geocoding API."""
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city_name}&key={api_key}"
    response = requests.get(geocode_url)
    results = response.json()
    if results['status'] == 'OK':
        location = results['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        print(f"Error in Geocoding API: {results['status']}")
        return None, None

def find_liquor_stores(api_key, lat, lng):
    """Find liquor stores near the given latitude and longitude using Places API with pagination."""
    places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f'{lat},{lng}',
        'radius': 48280,  # Search within 20 miles (160,934 meters)
        'keyword': 'liquor store',
        'type': 'store',  # Search for liquor stores
        'key': api_key
    }

    while True:
        response = requests.get(places_url, params=params)
        results = response.json()

        if results['status'] == 'OK':
            liquor_stores = results['results']
            for idx, store in enumerate(liquor_stores, 1):
                name = store.get('name', 'N/A')
                address = store.get('vicinity', 'N/A')
                rating = store.get('rating', 'No rating')
                print(f"Store: {name}, Address: {address}, Rating: {rating}")

            # Check if more results are available via next_page_token
            if 'next_page_token' in results:
                next_page_token = results['next_page_token']
                # Google recommends a short delay before using the next_page_token
                time.sleep(2)  # Wait 2 seconds before requesting the next page
                params['pagetoken'] = next_page_token
            else:
                break
        else:
            print(f"Error fetching liquor stores: {results['status']}")
            break
def search_multiple_cities(cities, api_key):
    """Search for liquor stores in multiple cities."""
    for city in cities:
        print(f"\nSearching for liquor stores in {city}:")
        lat, lng = get_coordinates(city, api_key)
        if lat and lng:
            find_liquor_stores(api_key, lat, lng)
        else:
            print(f"Could not find coordinates for {city}")
        time.sleep(2)  # Add a delay between searches to avoid hitting API rate limits
if __name__ == "__main__":
    cities = ["Cumming Downtown", "Atlanta", "Marietta", "Alpharetta", "Dawsonville", "Woodbridge", "Canton", "Buford", "Sugar Hill", "Sandy Springs", "Roswell"]  # Add your list of cities here
    search_multiple_cities(cities, API_KEY)
    
    if lat and lng:
        print(f"Liquor Stores in {city}:")
        find_liquor_stores(API_KEY, lat, lng)