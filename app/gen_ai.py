import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_direct_answer(question, passages):
    # Construct a prompt with the question and passages
    prompt = f"Question: {question}\nContext: {' '.join(passages)}"
    
    # Use OpenAI's GPT-3.5 Turbo to generate a direct answer
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose the appropriate engine
        prompt=prompt,
        max_tokens=150  # Adjust the max tokens based on your requirements
    )
    
    # Extract the generated answer from the response
    direct_answer = response.choices[0].text.strip()
    return direct_answer
