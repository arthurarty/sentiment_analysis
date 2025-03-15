import json
from typing import Any, Dict, List

from langchain_ollama import OllamaLLM


def analyze(
    tweets: List[str], model_name: str = "llama3.2"
) -> List[Dict[str, Any]]:
    """
    Perform sentiment analysis on a list of tweets.

    Args:
        tweets: List of tweet strings to analyze
        model_name: Name of the Ollama model to use

    Returns:
        List of dictionaries containing sentiment analysis for each tweet
    """
    # Initialize the LLM
    llm = OllamaLLM(model=model_name)

    # List to store analysis results
    results = []

    # Process each tweet
    for tweet in tweets:
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

            # Add original tweet to the result
            analysis_json["original_tweet"] = tweet

            # Append to results list
            results.append(analysis_json)

        except json.JSONDecodeError as e:
            # Handle parsing errors by adding error information to results
            results.append(
                {"original_tweet": tweet, "error": str(e), "raw_response": response}
            )

    return results
