from llm_parser import parse_query
from workflows.amazon_scraper import search_amazon
from workflows.flipkart_scraper import search_flipkart
from workflows.travel_scraper import search_travel
from excel_writer import save_to_excel_multi

if __name__ == "__main__":
    query = input("Enter your query: ")
    parsed = parse_query(query)
    print("Parsed Query:", parsed)

    all_results = {}

    if parsed['query_type'] == 'product_search':
        if 'amazon' in parsed['target_sites']:
            all_results['Amazon'] = search_amazon(parsed['search_terms'])
        if 'flipkart' in parsed['target_sites']:
            all_results['Flipkart'] = search_flipkart(parsed['search_terms'])

    elif parsed['query_type'] == 'flight_search':
        if 'makemytrip' in parsed['target_sites']:
            all_results['MakeMyTrip'] = search_travel(parsed['search_terms'])

    if all_results:
        save_to_excel_multi(all_results, filename="output/search_results.xlsx")
        print("Excel file generated: output/search_results.xlsx")
    else:
        print("This type of query or site is not supported yet.")
