import streamlit as st
import json
from src.config import SERPAPI_KEY
from src.ui import (
    setup_page, render_header, render_sidebar, render_user_inputs, 
    render_welcome_message, render_flight_card
)
from src.services import fetch_flights, extract_cheapest_flights, get_booking_link
from src.agent import create_planner_agent, generate_itinerary

# Setup
setup_page()
render_header()

# Sidebar
budget, flight_class, hotel_rating, visa_required, travel_insurance = render_sidebar()

# Main Inputs
source, destination, num_days, travel_theme, departure_date, return_date, activity_preferences = render_user_inputs()

# Welcome Message
render_welcome_message(travel_theme, destination)

# Main Logic
if st.button("🚀 Generate Travel Plan"):
    # 1. Fetch Flights
    with st.spinner("✈️ Fetching best flight options..."):
        flight_data = fetch_flights(source, destination, departure_date, return_date)
        
        # Check for empty results
        if not flight_data or (not flight_data.get('best_flights') and not flight_data.get('answer_box_list')):
            st.warning("No flight data found. Full API response:")
            st.json(flight_data)
        
        cheapest_flights = extract_cheapest_flights(flight_data)
    
    # 2. Display Flights
    st.subheader("✈️ Flights extracted from SerpAPI")
    # st.json(cheapest_flights) # Optional: Show raw JSON

    st.subheader("✈️ Cheapest Flight Options")
    if cheapest_flights:
        cols = st.columns(len(cheapest_flights))
        for idx, flight in enumerate(cheapest_flights):
            with cols[idx]:
                # Get booking link
                departure_token = flight.get("departure_token", "")
                booking_token = get_booking_link(idx, source, destination, departure_date, return_date, departure_token)
                booking_link = f"https://www.google.com/travel/flights?tfs={booking_token}" if booking_token else "#"
                
                # Render card
                render_flight_card(flight, booking_link)
    else:
        st.warning("⚠️ No flight data available.")

    # 3. Generate Itinerary
    with st.spinner("🧠 Creating itinerary with Zephyr..."):
        planner = create_planner_agent()
        itinerary = generate_itinerary(
            planner, 
            destination, 
            num_days, 
            travel_theme, 
            budget, 
            activity_preferences
        )

    # 4. Display Itinerary
    st.subheader("🗺️ AI-Generated Itinerary")
    st.write(itinerary.content)

    st.success("✅ Travel plan generated successfully!")
