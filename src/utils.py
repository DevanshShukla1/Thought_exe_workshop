from datetime import datetime

def format_datetime(iso_string):
    """Formats ISO datetime string to a readable format."""
    try:
        dt = datetime.strptime(iso_string, "%Y-%m-%d %H:%M")
        return dt.strftime("%b-%d, %Y | %I:%M %p")  # Example: Mar-06, 2025 | 6:20 PM
    except:
        return "N/A"
