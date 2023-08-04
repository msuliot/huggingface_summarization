# Hugging Face Transformers - Summarization

## The basics

1. Must have Python3.
2. Get repository
```bash
git clone https://github.com/msuliot/getting-interviewed-by-ai.git 
```
3. use pip3 to install any dependencies.
```bash
pip3 install -r requirements.txt
```

## Hugging Face Access Token

Make sure to get an access token key from https://huggingface.co/settings/tokens

Create a ".env" file and put your access token in that file
```bash
HUGGINGFACEHUB_API_TOKEN = 'hf_XXXXXXXX'
```

# Instructions:

There are three different examples of how to use the Hugging Face Transformers library.

## 1. Run the API script
```bash
python3 api.py
```

## 2. Run the pipeline script
```bash
python3 pipeline.py
```

## 3. Run the pipeline script
```bash
python3 tensorizer.py
```