import requests

def make_api_call(access_token, api_url):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'x-gw-ims-org-id': 'YOUR_ORGANIZATION_ID',
        'x-api-key': 'YOUR_API_KEY'
    }

    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Raise an exception for error responses

    return response.json()

if __name__ == '__main__':
    access_token = "YOUR_ACCESS_TOKEN"
    api_url = "https://api-inference.huggingface.co"

    try:
        response_data = make_api_call(access_token, api_url)
        print("API Response 1:")
        print(response_data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    api_url2 = "https://endpoints.huggingface.cloud"

    try:
        response_data = make_api_call(access_token, api_url2)
        print("API Response 2:")
        print(response_data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
