import json

def extract_place_details(json_data):
    """
    Extracts place details from the JSON data and returns a dictionary with placeId as keys and a tuple
    of (name, address, startTimestamp) as values.
    
    Parameters:
    json_data (dict): The input JSON data containing timelineObjects.

    Returns:
    dict: A dictionary with placeId as keys and (name, address, startTimestamp) as values.
    """
    placesfiltered = {}
    
    for timeline_object in json_data.get("timelineObjects", []):
        place_visit = timeline_object.get("placeVisit", {})
        location = place_visit.get("location", {})
        place_id = location.get("placeId")
        name = location.get("name")
        address = location.get("address")
        start_timestamp = place_visit.get("duration", {}).get("startTimestamp")
        
        if place_id:
            placesfiltered[place_id] = (name, address, start_timestamp)
    
    return placesfiltered

# Example usage
file_path = 'takeout-20240721T150356Z-001/Takeout/Location History (Timeline)/Semantic Location History/2024/2024_JULY.json' 
with open(file_path, 'r', encoding="utf-8") as file:
    json_data = json.load(file)

placesfiltered = extract_place_details(json_data)
print(placesfiltered)
