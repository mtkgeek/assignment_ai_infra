import geopandas as gpd
import requests
import argparse

# command-line argument parsing
parser = argparse.ArgumentParser(
    description="Post GeoJSON data with a Bearer token")
parser.add_argument('access_token', type=str,
                    help='Access token for authorization')

args = parser.parse_args()

geojson_file = 'data/municipalities_nl.geojson'
gdf = gpd.read_file(geojson_file)

url = 'http://localhost:8000/api/features/'
headers = {
    'Content-Type': 'application/json',
    # Use the token from the command-line argument
    'Authorization': f'Bearer {args.access_token}'
}

for _, row in gdf.iterrows():
    feature = {
        'name': row['name'],
        'geometry': row['geometry'].__geo_interface__
    }
    response = requests.post(url, json=feature, headers=headers)
    print(response.status_code, response.json())
