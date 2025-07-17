import requests
import json

def parse_query(query):
    prompt = f"""
You are an AI that reads a user's query and returns a dictionary like this:
{{
  "query_type": "product_search",
  "target_sites": ["amazon", "flipkart"],
  "search_terms": "smartphone under 30000"
}}

Now parse this query: \"{query}\"
Only return the dictionary, nothing else.
"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })

    try:
        result = response.json()["response"].strip()
        print("Raw Ollama output:\n", result)
        return eval(result)
    except Exception as e:
        print("⚠️ Error while parsing LLM response:", e)
        return {
            "query_type": "product_search",
            "target_sites": ["amazon"],
            "search_terms": query
        }
