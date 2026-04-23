from graph.state import TravelState
from tools.bing_search import search_destination
from tools.hotel_api import get_hotels

# Phase 1: State (KEEP THIS)
state: TravelState = {
    "destination": "Goa",
    "travel_dates": "10-15 May",
    "budget_per_night": 3000,
    "preferences": "beach, luxury",

    "destination_info": "",
    "hotels_found": [],
    "available_hotels": [],
    "selected_hotel": {},

    "final_itinerary": "",
    "retry_count": 0
}

print("Initial State:", state)


# Phase 2: Tools (ADD THIS)

# Call destination tool
destination_info = search_destination(state["destination"])
state["destination_info"] = destination_info

# Call hotel tool
hotels = get_hotels(state["destination"], state["budget_per_night"])
state["hotels_found"] = hotels

print("\nUpdated State After Tools:", state)