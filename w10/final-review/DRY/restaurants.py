restaurants = [
    {"name": "Pasta Palace", "ratings": [4.5, 4.2, 4.8, 4.3, 4.6]},
    {"name": "Burger Barn", "ratings": [3.9, 4.1, 3.8, 4.0, 3.7]},
    {"name": "Sushi Spot", "ratings": [4.7, 4.9, 4.8, 4.6, 4.7]},
]

# Calculate average for each restaurant (repetitive code)
pp_total = 0
for r in restaurants[0]["ratings"]:
    pp_total += r
pp_avg = pp_total / len(restaurants[0]["ratings"])

bb_total = 0
for r in restaurants[1]["ratings"]:
    bb_total += r
bb_avg = bb_total / len(restaurants[1]["ratings"])

ss_total = 0
for r in restaurants[2]["ratings"]:
    ss_total += r
ss_avg = ss_total / len(restaurants[2]["ratings"])

# Find highest rating for each restaurant (repetitive code)
pp_high = restaurants[0]["ratings"][0]
for r in restaurants[0]["ratings"]:
    if r > pp_high:
        pp_high = r

bb_high = restaurants[1]["ratings"][0]
for r in restaurants[1]["ratings"]:
    if r > bb_high:
        bb_high = r

ss_high = restaurants[2]["ratings"][0]
for r in restaurants[2]["ratings"]:
    if r > ss_high:
        ss_high = r

# Print reports (repetitive code)
print(f"\nReport for {restaurants[0]['name']}:")
print(f"Ratings: {restaurants[0]['ratings']}")
print(f"Average Rating: {pp_avg:.2f}")
print(f"Highest Rating: {pp_high}")

print(f"\nReport for {restaurants[1]['name']}:")
print(f"Ratings: {restaurants[1]['ratings']}")
print(f"Average Rating: {bb_avg:.2f}")
print(f"Highest Rating: {bb_high}")

print(f"\nReport for {restaurants[2]['name']}:")
print(f"Ratings: {restaurants[2]['ratings']}")
print(f"Average Rating: {ss_avg:.2f}")
print(f"Highest Rating: {ss_high}")

# Calculate overall statistics (repetitive code)
total_ratings = 0
for r in restaurants[0]["ratings"]:
    total_ratings += r
for r in restaurants[1]["ratings"]:
    total_ratings += r
for r in restaurants[2]["ratings"]:
    total_ratings += r

highest_rating = restaurants[0]["ratings"][0]
for r in restaurants[0]["ratings"]:
    if r > highest_rating:
        highest_rating = r
for r in restaurants[1]["ratings"]:
    if r > highest_rating:
        highest_rating = r
for r in restaurants[2]["ratings"]:
    if r > highest_rating:
        highest_rating = r

lowest_rating = restaurants[0]["ratings"][0]
for r in restaurants[0]["ratings"]:
    if r < lowest_rating:
        lowest_rating = r
for r in restaurants[1]["ratings"]:
    if r < lowest_rating:
        lowest_rating = r
for r in restaurants[2]["ratings"]:
    if r < lowest_rating:
        lowest_rating = r

overall_average = total_ratings / (
    len(restaurants[0]["ratings"])
    + len(restaurants[1]["ratings"])
    + len(restaurants[2]["ratings"])
)
print(f"\nOverall Statistics:")
print(f"Average Rating Across All Restaurants: {overall_average:.2f}")
print(f"Highest Rating Overall: {highest_rating}")
print(f"Lowest Rating Overall: {lowest_rating}")
