import json

from langchain_ollama import OllamaLLM

# Initialize the LLM
llm = OllamaLLM(model="llama3.2")  # or any model you're using

# Example tweet
tweet = "I absolutely HATE when people don't use their turn signals while driving!! It's dangerous and inconsiderate!! #RoadRage"

# Prompt for sentiment analysis with specific JSON structure
prompt = f"""
Analyze the following tweet and return ONLY a JSON object with sentiment analysis.

Tweet: "{tweet}"

The JSON must have exactly these three fields:
- sentiment: a string describing the overall sentiment (e.g., positive, negative, neutral)
- aggressiveness: an integer from 1 to 10 indicating how aggressive the text is
- language: a string identifying the language the text is written in

Return ONLY the JSON object without any explanation or additional text.
"""

# Get response
response = llm.invoke(prompt)

# Try to parse the JSON
try:
    # Extract JSON if it's wrapped in code blocks
    if "```json" in response:
        json_str = response.split("```json")[1].split("```")[0].strip()
    elif "```" in response:
        json_str = response.split("```")[1].split("```")[0].strip() 
    else:
        json_str = response.strip()
   
    # Parse the JSON
    analysis_json = json.loads(json_str)
    print(json.dumps(analysis_json, indent=2))
 
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
    print(f"Raw response:\n{response}")
