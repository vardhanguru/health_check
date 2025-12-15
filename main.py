import requests
import time

URL = 'https://harsha-gallery.onrender.com/health/'

try:
    response = requests.get(URL, timeout=10)
    print(f"Status: {response.status_code} | Time: {time.ctime()}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
