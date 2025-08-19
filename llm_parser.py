import requests
import ast

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
        "From": "Delhi",
        "To": "Mumbai"
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
        result = response.json()
        raw_output = result.get("response", "")
        parsed = ast.literal_eval(raw_output.strip())
        return parsed
    except Exception as e:
        print(f"⚠️ Error while parsing LLM response: {e}")
        
        # --- Fallback handling ---
        q_lower = query.lower()
        if "flight" in q_lower or "travel" in q_lower:
            # crude way: try to split "from X to Y"
            if " to " in q_lower and "from " in q_lower:
                try:
                    from_city = q_lower.split("from ")[1].split(" to ")[0].strip().title()
                    to_city = q_lower.split(" to ")[1].strip().title()
                except:
                    from_city, to_city = "Delhi", "Mumbai"
            else:
                from_city, to_city = "Delhi", "Mumbai"  # default fallback

            return {
                "query_type": "flight_search",
                "target_sites": ["makemytrip"],
                "From": from_city,
                "To": to_city
            }
        else:
            return {
                "query_type": "product_search",
                "target_sites": ["amazon"],
                "search_terms": query
            }