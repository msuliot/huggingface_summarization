import os
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM, BartForConditionalGeneration
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN')
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def set_local_vars():
    model_name = "facebook/bart-large-cnn"
    pipeline_task = "summarization"
    return model_name, pipeline_task


def hf_tensorizer(model_name, pipeline_task, text):
    tokenizer = AutoTokenizer.from_pretrained(model_name) 
    model = BartForConditionalGeneration.from_pretrained(model_name)
    pipe = pipeline(pipeline_task, model=model, tokenizer=tokenizer)
    output = pipe(text)
    return output


def main():
    model_name, pipeline_task = set_local_vars()

    text = "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
    
    return_value = hf_tensorizer(model_name, pipeline_task, text)
    print(return_value)

if __name__ == "__main__":
    main() 