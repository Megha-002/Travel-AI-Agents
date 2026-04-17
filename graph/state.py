from typing import TypedDict, List

class TravelState(TypedDict):
    destination: str
    travel_dates: str
    budget_per_night: int
    preferences: str

    destination_info: str
    hotels_found: List[dict]
    available_hotels: List[dict]
    selected_hotel: dict

    final_itinerary: str
    retry_count: int