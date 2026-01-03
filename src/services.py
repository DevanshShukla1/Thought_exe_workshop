from serpapi import GoogleSearch
import streamlit as st
from .config import SERPAPI_KEY

def fetch_flights(source, destination, departure_date, return_date):
    """
    Fetches flight data from Google Flights via SerpAPI.
    """
    params = {
        "engine": "google_flights",
        "departure_id": source,
        "arrival_id": destination,
        "outbound_date": str(departure_date),
        "return_date": str(return_date),
        "currency": "INR",
        "hl": "en",
        "api_key": SERPAPI_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    # Debug: Show raw SerpAPI response if error
    if 'error' in results:
        st.error(f"SerpAPI Error: {results['error']}")
        # We might want to avoid direct UI calls here in strict MVC, 
        # but for now we'll keep the error reporting logic.
        return results
        
    return results

def extract_cheapest_flights(flight_data):
    """
    Extracts the top 3 cheapest flights from the SerpAPI response.
    """
    # Case 1: google_flights engine
    if "best_flights" in flight_data:
        return flight_data.get("best_flights", [])[:3]

    # Case 2: google engine with answer box
    flights = []
    for block in flight_data.get("answer_box_list", []):
        if block.get("type") == "google_flights":
            flights.extend(block.get("flights", []))

    return flights[:3]

def get_booking_link(flight_index, source, destination, departure_date, return_date, departure_token):
    """
    Fetches the booking link for a specific flight using its departure token.
    """
    if not departure_token:
        return None

    try:
        params_with_token = {
            "engine": "google_flights",
            "departure_id": source,
            "arrival_id": destination,
            "outbound_date": str(departure_date),
            "return_date": str(return_date),
            "currency": "INR",
            "hl": "en",
            "api_key": SERPAPI_KEY,
            "departure_token": departure_token
        }
        search_with_token = GoogleSearch(params_with_token)
        results_with_booking = search_with_token.get_dict()

        if 'best_flights' in results_with_booking and len(results_with_booking['best_flights']) > flight_index:
            return results_with_booking['best_flights'][flight_index].get('booking_token', None)
    except Exception as e:
        # In a real app we'd log this exception
        print(f"Error fetching booking link: {e}")
        return None
    
    return None
