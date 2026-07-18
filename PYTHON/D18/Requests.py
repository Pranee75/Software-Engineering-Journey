import requests

# --- 1. Basic GET Request ---
print("--- GET Request ---")
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
else:
    print(f"Request failed with code: {response.status_code}")


# --- 2. POST Request (Sending Data) ---
print("\n--- POST Request ---")
payload = {'title': 'New Post', 'body': 'Content here', 'userId': 1}
# jsonplaceholder is a fake API, it will return 201 Created
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")


# --- 3. Handling Query Parameters ---
print("\n--- Query Parameters ---")
# Using a real endpoint that accepts query parameters
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
print(f"Request URL: {response.url}")


# --- 4. Using raise_for_status() ---
print("\n--- raise_for_status() ---")
try:
    # Testing with a valid URL that exists
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=5)
    response.raise_for_status() 
    print("Request successful!")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")


# --- 5. Use Session Objects ---
print("\n--- Session Object ---")
session = requests.Session()
# Note: JSONPlaceholder doesn't require real auth, 
# but this shows the syntax for how you'd use a session.
session.auth = ('user', 'password')

try:
    # We use a real URL here so the session can actually connect
    resp1 = session.get('https://jsonplaceholder.typicode.com/posts/1')
    resp2 = session.get('https://jsonplaceholder.typicode.com/posts/2')
    print(f"Session Request 1 status: {resp1.status_code}")
    print(f"Session Request 2 status: {resp2.status_code}")
finally:
    session.close()