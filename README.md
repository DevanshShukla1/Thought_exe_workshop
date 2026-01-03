# 🌍 AI Travel Planner

A modern, AI-powered travel planning app that helps you create personalized itineraries, find the best flights, and organize your dream trip—all in one place!

---

## ✨ Features

- **AI-Powered Itinerary Generation:**
  - Uses advanced language models (HuggingFace) to create detailed, day-wise travel plans based on your preferences, budget, and destination.
- **Live Flight Search:**
  - Integrates with SerpAPI to fetch real-time flight data from Google Flights.
- **Interactive Web UI:**
  - Built with Streamlit for a beautiful, responsive, and easy-to-use interface.
- **Personalized Recommendations:**
  - Customize your trip theme, activities, hotel rating, and more.
- **Packing Checklist & Essentials:**
  - Sidebar tools to help you prepare for your journey.

---

## 🏗️ Project Structure

```
travel/
├── main.py                # Entry point (demo)
├── travelagent.py         # Main Streamlit app
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project metadata
├── .env                   # API keys (not committed)
├── src/
│   ├── agent.py           # AI agent setup and itinerary generation
│   ├── config.py          # Loads API keys and app config
│   ├── services.py        # Flight data fetching and processing
│   ├── ui.py              # Streamlit UI components
│   ├── utils.py           # Utility functions
```

---

## 🚀 Quickstart

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/your-repo-name.git
cd travel
```

### 2. Install Dependencies

> **Python 3.11+ is required.**

```sh
pip install -r requirements.txt
```

### 3. Set Up API Keys

Create a `.env` file in the project root with the following (replace with your own keys):

```
SERPAPI_KEY=your_serpapi_key
GOOGLE_API_KEY=your_google_api_key
HF_TOKEN=your_huggingface_token
```

- **SERPAPI_KEY:** Get from [serpapi.com](https://serpapi.com/)
- **GOOGLE_API_KEY:** For Google services (optional, for future features)
- **HF_TOKEN:** Get from [huggingface.co](https://huggingface.co/settings/tokens)

### 4. Run the App

```sh
streamlit run travelagent.py
```

The app will open in your browser. Enter your travel details, and let the AI do the rest!

---

## 🧩 How It Works

- **User Input:**
  - Enter your departure/destination, trip duration, travel theme, and preferences.
- **Flight Search:**
  - The app fetches real-time flight options using SerpAPI and displays the top choices.
- **AI Itinerary:**
  - The AI agent generates a detailed, day-wise itinerary tailored to your input.
- **Booking Links:**
  - Direct links to book flights are provided (when available).

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Streamlit** (UI)
- **SerpAPI** (Flight data)
- **HuggingFace Transformers** (AI itinerary)
- **dotenv** (Config management)

---

## 📁 Modules Overview

- **src/agent.py**: Sets up the AI agent and handles itinerary generation.
- **src/config.py**: Loads API keys and app settings from `.env`.
- **src/services.py**: Fetches and processes flight data from SerpAPI.
- **src/ui.py**: Streamlit UI components for user input, sidebar, and results display.
- **src/utils.py**: Helper functions (e.g., date formatting).

---

## 📝 Customization & Extending

- Add new travel themes or preferences in `src/ui.py`.
- Swap out the AI model in `src/agent.py` by changing the HuggingFace model ID.
- Integrate more APIs (hotels, activities) in `src/services.py`.

---

## ❓ FAQ

**Q: Why do I need API keys?**
A: The app fetches live flight data and uses AI models that require authentication.

**Q: Can I use my own AI model?**
A: Yes! Edit `src/agent.py` to use any HuggingFace-compatible model.

**Q: Is my data private?**
A: API keys are loaded from `.env` and not committed to the repo. Never share your keys.

---

## 📜 License

MIT License. See LICENSE file for details.

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [SerpAPI](https://serpapi.com/)
- [HuggingFace](https://huggingface.co/)

---

Enjoy planning your next adventure! ✈️🌏
