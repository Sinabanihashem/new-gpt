import requests

def get_response_from_api(user_input):
    url = "https://api.api-code.ir/gpt-4/"
    payload = {"text": user_input}
    try:
        response = requests.get(url, params=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('result', "No result found")  
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    while True:
        text = input("Enter your message (or type 'exit' to quit): ")
        if text.lower() == "exit":
            break
        print(get_response_from_api(text))

if __name__ == "__main__":
    main()
