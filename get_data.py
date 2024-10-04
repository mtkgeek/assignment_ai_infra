import requests
import argparse

# command-line argument parsing
parser = argparse.ArgumentParser(description="Get data with a Bearer token")
parser.add_argument('access_token', type=str,
                    help='Access token for authorization')

args = parser.parse_args()

url = 'http://localhost:8000/api/features/'
headers = {
    'Content-Type': 'application/json',
    # Use the token from the command-line argument
    'Authorization': f'Bearer {args.access_token}'
}

response = requests.get(url, headers=headers)
print(response.status_code, response.json())
