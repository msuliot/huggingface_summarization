from transformers import pipeline, AutoTokenizer
from transformers import BartForConditionalGeneration, TFBartForConditionalGeneration 

import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file
pipeline_task = os.getenv('PIPELINE_TASK') # pipeline task for huggingface.co in .env file
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def hf_local(text):
    # This will download the model and tokenizer to your local machine and run on your local machine. 
    # saved and cached ~/.cache/huggingface
    tokenizer = AutoTokenizer.from_pretrained(model_name, return_tensors="pt") # return_tensors="pt" or "tf"
    model = BartForConditionalGeneration.from_pretrained(model_name) # BartForConditionalGeneration or TFBartForConditionalGeneration
    pipe = pipeline(pipeline_task, model=model, tokenizer=tokenizer)
    output = pipe(text)
    return output


def main():
    text = "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
    return_value = hf_local(text)
    print(return_value)

if __name__ == "__main__":
    main() 