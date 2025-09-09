import requests

def send_requests():
    url="https://httpbin.org/get"
    try:
        response=requests.get(url)
        print("GET Request:")
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.text)
    except requests.RequestException as e:
        print("GET request failed:", e)

    url_post="https://httpbin.org/post"
    data={'name': 'Vedika', 'age': 19}
    try:
        response=requests.post(url_post, data=data)
        print("\nPOST Request:")
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.text)
    except requests.RequestException as e:
        print("POST request failed:", e)

send_requests()
