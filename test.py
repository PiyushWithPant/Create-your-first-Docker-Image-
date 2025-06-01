# To run this file using Docker Container

# > docker run --rm -v $(pwd):/app -w /app mycontainer:v1 python test.py


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model_name = "facebook/opt-1.3B"


print(f"Loading {model_name} model...")


print("*"*50)
print("\n")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input prompt
prompt = "Who are you?"

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate response
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=30,
        do_sample=True,           # enables sampling
        temperature=0.7,          # controls randomness (lower = less random)
        top_p=0.9,                # nucleus sampling
        top_k=50,                 # limits to top-k tokens
        repetition_penalty=1.2,   # discourages repetition
        eos_token_id=tokenizer.eos_token_id,  # stops at end of sentence
    )


# Decode and print
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)


print("\n")
print("*"*50)
print("\n")

print("Congrats! Looks like your Docker Image and Container are working pretty well. Good job :-)")


