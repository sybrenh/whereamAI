import requests
from api_key import api_key

def get_place_types(api_key, place_id):
    # Define the endpoint URL for Place Details
    url = 'https://maps.googleapis.com/maps/api/place/details/json'
    
    # Define the parameters for the API request
    params = {
        'place_id': place_id,
        'key': api_key
    }
    
    # Make the GET request to the Place Details endpoint
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the types from the response
        if 'result' in data and 'types' in data['result']:
            place_types = data['result']['types']
            return place_types
        else:
            return "No types found in the response."
    else:
        return f"Request failed with status code {response.status_code}."

# Example usage
api_key = api_key
place_id = 'ChIJ4XHfEldvxkcR70fjrOIreWk'  # Example place_id

place_types = get_place_types(api_key, place_id)
print("Place Types:", place_types)