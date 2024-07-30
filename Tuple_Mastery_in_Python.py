def format_itineraries(itineraries):
    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        print(f"Itinerary {index}: {traveler_name} - From {origin} to {destination}")

# Example usage
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
format_itineraries(itineraries)

