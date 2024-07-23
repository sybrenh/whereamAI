import json
from sentence_transformers import SentenceTransformer
import pinecone

# Load Google location data
with open('location_history.json', 'r') as f:
    location_data = json.load(f)

# Initialize embedding model and vector database
model = SentenceTransformer('all-MiniLM-L6-v2')
pinecone.init(api_key='your_api_key')
index = pinecone.Index('location_index')

# Embed and store locations
for entry in location_data['locations']:
    coordinates = f"{entry['latitudeE7'] / 1e7}, {entry['longitudeE7'] / 1e7}"
    embedding = model.encode(coordinates)
    index.upsert([(entry['timestampMs'], embedding)])
