from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the GenAI-CoverLetter model
model_name = "PanoEvJ/GenAI-CoverLetter"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prompt for user input
user_input = input("Enter your cover letter prompt: ")

# Generate a cover letter
input_ids = tokenizer.encode(user_input, return_tensors="pt")
output = model.generate(input_ids, max_length=200, num_return_sequences=1)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("\nGenerated Cover Letter:\n")
print(generated_text)
