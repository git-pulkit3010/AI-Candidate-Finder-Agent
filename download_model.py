from transformers import GPT2LMHeadModel, GPT2Tokenizer

def download_model():
    print("Downloading model...")
    GPT2Tokenizer.from_pretrained("gpt2")
    GPT2LMHeadModel.from_pretrained("gpt2")
    print("Model download complete.")

if __name__ == "__main__":
    download_model()
