import requests
import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file


def set_local_vars():
    model_name = "facebook/bart-large-cnn"
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    return api_url


def hf_api(api_url, text):
    headers = {"Authorization": f"Bearer {hf_api_key}"}

    def query(payload):
        response = requests.post(api_url, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": text,
    })
    return output


def main():
    api_url = set_local_vars()

    text = "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
    
    return_value = hf_api(api_url, text)
    print(return_value)


if __name__ == "__main__":
    main() 