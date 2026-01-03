import streamlit as st
from .config import APP_TITLE, GOOGLE_API_KEY, SERPAPI_KEY, HF_TOKEN, MODEL_ID
from .utils import format_datetime

def setup_page():
    """Sets up the Streamlit page configuration and styling."""
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    st.markdown(
        """
        <style>
            .title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #ff5733;
            }
            .subtitle {
                text-align: center;
                font-size: 20px;
                color: #555;
            }
            .stSlider > div {
                background-color: #f9f9f9;
                padding: 10px;
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_sidebar():
    """Renders the sidebar content."""
    st.sidebar.write("GOOGLE_API_KEY loaded:", bool(GOOGLE_API_KEY))
    st.sidebar.write("SERPAPI_KEY loaded:", bool(SERPAPI_KEY))
    st.sidebar.write("HF_TOKEN loaded:", bool(HF_TOKEN))
    st.sidebar.write("Model:", MODEL_ID)
    
    st.sidebar.title("🌎 Travel Assistant")
    st.sidebar.subheader("Personalize Your Trip")

    # Travel Preferences
    budget = st.sidebar.radio("💰 Budget Preference:", ["Economy", "Standard", "Luxury"])
    flight_class = st.sidebar.radio("✈️ Flight Class:", ["Economy", "Business", "First Class"])
    hotel_rating = st.sidebar.selectbox("🏨 Preferred Hotel Rating:", ["Any", "3⭐", "4⭐", "5⭐"])

    # Packing Checklist
    st.sidebar.subheader("🎒 Packing Checklist")
    packing_list = {
        "👕 Clothes": True,
        "🩴 Comfortable Footwear": True,
        "🕶️ Sunglasses & Sunscreen": False,
        "📖 Travel Guidebook": False,
        "💊 Medications & First-Aid": True
    }
    for item, checked in packing_list.items():
        st.sidebar.checkbox(item, value=checked)

    # Travel Essentials
    st.sidebar.subheader("🛂 Travel Essentials")
    visa_required = st.sidebar.checkbox("🛃 Check Visa Requirements")
    travel_insurance = st.sidebar.checkbox("🛡️ Get Travel Insurance")
    currency_converter = st.sidebar.checkbox("💱 Currency Exchange Rates")

    return budget, flight_class, hotel_rating, visa_required, travel_insurance

def render_header():
    """Renders the main header."""
    st.markdown(f'<h1 class="title">✈️ {APP_TITLE}</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Plan your dream trip with AI! Get personalized recommendations for flights, hotels, and activities.</p>', unsafe_allow_html=True)

def render_user_inputs():
    """Renders the user input form."""
    st.markdown("### 🌍 Where are you headed?")
    source = st.text_input("🛫 Departure City (IATA Code):", "BOM")
    destination = st.text_input("🛬 Destination (IATA Code):", "DEL")

    st.markdown("### 📅 Plan Your Adventure")
    num_days = st.slider("🕒 Trip Duration (days):", 1, 14, 5)
    travel_theme = st.selectbox(
        "🎭 Select Your Travel Theme:",
        ["💑 Couple Getaway", "👨‍👩‍👧‍👦 Family Vacation", "🏔️ Adventure Trip", "🧳 Solo Exploration"]
    )
    
    departure_date = st.date_input("Departure Date")
    return_date = st.date_input("Return Date")
    
    activity_preferences = st.text_area(
        "🌍 What activities do you enjoy? (e.g., relaxing on the beach, exploring historical sites, nightlife, adventure)",
        "Relaxing on the beach, exploring historical sites"
    )

    return source, destination, num_days, travel_theme, departure_date, return_date, activity_preferences

def render_welcome_message(travel_theme, destination):
    st.markdown("---")
    st.markdown(
        f"""
        <div style="
            text-align: center; 
            padding: 15px; 
            background-color: #ffecd1; 
            border-radius: 10px; 
            margin-top: 20px;
        ">
            <h3>🌟 Your {travel_theme} to {destination} is about to begin! 🌟</h3>
            <p>Let's find the best flights, stays, and experiences for your unforgettable journey.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_flight_card(flight, booking_link):
    """Renders a single flight card."""
    airline_logo = flight.get("airline_logo", "")
    price = flight.get("price", "Not Available")
    total_duration = flight.get("total_duration", "N/A")
    
    flights_info = flight.get("flights", [{}])
    departure = flights_info[0].get("departure_airport", {})
    arrival = flights_info[-1].get("arrival_airport", {})
    airline_name = flights_info[0].get("airline", "Unknown Airline") 
    
    departure_time = format_datetime(departure.get("time", "N/A"))
    arrival_time = format_datetime(arrival.get("time", "N/A"))

    st.markdown(
        f"""
        <div style="
            border: 2px solid #ddd; 
            border-radius: 10px; 
            padding: 15px; 
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
            margin-bottom: 20px;
        ">
            <img src="{airline_logo}" width="100" alt="Flight Logo" />
            <h3 style="margin: 10px 0;">{airline_name}</h3>
            <p><strong>Departure:</strong> {departure_time}</p>
            <p><strong>Arrival:</strong> {arrival_time}</p>
            <p><strong>Duration:</strong> {total_duration} min</p>
            <h2 style="color: #008000;">💰 {price}</h2>
            <a href="{booking_link}" target="_blank" style="
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                color: #fff;
                background-color: #007bff;
                text-decoration: none;
                border-radius: 5px;
                margin-top: 10px;
            ">🔗 Book Now</a>
        </div>
        """,
        unsafe_allow_html=True
    )
