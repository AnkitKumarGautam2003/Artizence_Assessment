import requests
import json
import output

def parse_query(query):
    prompt = f"""
        You are an AI assistant that takes a user's query and returns a dictionary in Python format.

        Examples:

        Query: I want a phone under 30000 on Amazon  
        Output: {{
        "query_type": "product_search",
        "target_sites": ["amazon"],
        "search_terms": "phone under 30000"
        }}

        Query: Find me flights from Delhi to Mumbai  
        Output: {{
        "query_type": "flight_search",
        "target_sites": ["makemytrip"],
        "search_terms": "Delhi to Mumbai flights"
        }}

        Now parse this query: \"{query}\"  
        Return ONLY the Python dictionary.
        """


    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })

    try:
        return eval(output.strip())
    except Exception as e:
        print("⚠️ Error while parsing LLM response:", e)
        
        # Fallback keyword detection
        if any(word in query.lower() for word in ["flight", "air", "airport", "to", "from", "departure"]):
            return {
                "query_type": "flight_search",
                "target_sites": ["makemytrip"],
                "search_terms": query
            }
        else:
            return {
                "query_type": "product_search",
                "target_sites": ["amazon"],
                "search_terms": query
            }

