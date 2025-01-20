import requests

def get_example():
  response = requests.get("https://google.com")
  
  print(f"Status Code: {response.status_code}")
  print(f"Content: {response.text}")

print('__name__: ', __name__)

if __name__ == "__main__":
  get_example()