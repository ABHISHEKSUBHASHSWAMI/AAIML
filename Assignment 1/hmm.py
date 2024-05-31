
# Program to predict User's next location

# Example Using HMMs (Hidden Markov Models)

def predict_next_location(transition_matrix, current_location):
    next_location_probabilities = transition_matrix.get(current_location, {})
    return max(next_location_probabilities, key=next_location_probabilities.get)


transition_matrix = {
    "home": {"work": 0.5, "gym": 0.2, "park": 0.3},
    "work": {"home": 0.7, "restaurant": 0.2, "bar": 0.1},
    "gym": {"home": 0.8, "park": 0.2},
    "park": {"home": 0.6, "restaurant": 0.3, "cafe": 0.1},
    "restaurant": {"work": 0.4, "home": 0.3, "bar": 0.3},
    "bar": {"home": 0.6, "restaurant": 0.2, "cafe": 0.2},
    "cafe": {"work": 0.1, "park": 0.4, "home": 0.5},
}

current_location = "restaurant"

next_location = predict_next_location(transition_matrix, current_location)
print(f"Next location predicted is {next_location}")
