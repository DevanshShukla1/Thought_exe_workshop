from agno.models.huggingface import HuggingFace
from agno.agent import Agent
from .config import HF_TOKEN, MODEL_ID, MAX_TOKENS, TEMPERATURE

def get_model():
    """
    Initializes and returns the HuggingFace model.
    """
    return HuggingFace(
        id=MODEL_ID,
        api_key=HF_TOKEN if HF_TOKEN and HF_TOKEN != "your_huggingface_token_here" else None,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )

def create_planner_agent():
    """
    Creates and returns the Travel Planner agent.
    """
    llm = get_model()
    
    return Agent(
        name="Planner",
        model=llm,
        instructions=[
            "Gather details about the user's travel preferences and budget.",
            "Create a detailed itinerary with scheduled activities and estimated costs.",
            "Ensure the itinerary includes transportation options and travel time estimates.",
            "Optimize the schedule for convenience and enjoyment.",
            "Present the itinerary in a structured format."
        ]
    )

def generate_itinerary(planner, destination, num_days, travel_theme, budget, activity_preferences):
    """
    Runs the planner agent to generate an itinerary.
    """
    planning_prompt = f"""
    Destination: {destination}
    Trip duration: {num_days} days
    Travel theme: {travel_theme}
    Budget: {budget}
    Preferred activities: {activity_preferences}

    Rules:
    - Use ONLY the flight data provided if available.
    - If data is missing, say "Not available".
    - Do NOT invent airlines, prices, or timings.


    Create a realistic, day-wise travel itinerary.
    Do not invent flight prices or airlines.
    """
    
    return planner.run(planning_prompt, stream=False)
