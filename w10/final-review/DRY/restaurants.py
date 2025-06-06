restaurants = [
    {"name": "Pasta Palace", "ratings": [4.5, 4.2, 4.8, 4.3, 4.6]},
    {"name": "Burger Barn", "ratings": [3.9, 4.1, 3.8, 4.0, 3.7]},
    {"name": "Sushi Spot", "ratings": [4.7, 4.9, 4.8, 4.6, 4.7]},
]

# Calculate average ratings
averages = []
for restaurant in restaurants:
    total = 0
    for rating in restaurant["ratings"]:
        total += rating
    average = total / len(restaurant["ratings"])
    averages.append({"name": restaurant["name"], "average": average})

# Find highest rating for each restaurant
highest_ratings = []
for restaurant in restaurants:
    highest = restaurant["ratings"][0]
    for rating in restaurant["ratings"]:
        if rating > highest:
            highest = rating
    highest_ratings.append({"name": restaurant["name"], "highest": highest})

# Generate report for each restaurant
for i in range(len(restaurants)):
    restaurant = restaurants[i]
    avg = averages[i]["average"]
    high = highest_ratings[i]["highest"]

    print(f"\nReport for {restaurant['name']}:")
    print(f"Ratings: {restaurant['ratings']}")
    print(f"Average Rating: {avg:.2f}")
    print(f"Highest Rating: {high}")

# Calculate overall statistics
total_ratings = 0
highest_rating = restaurants[0]["ratings"][0]
lowest_rating = restaurants[0]["ratings"][0]

for restaurant in restaurants:
    for rating in restaurant["ratings"]:
        total_ratings += rating
        if rating > highest_rating:
            highest_rating = rating
        if rating < lowest_rating:
            lowest_rating = rating

overall_average = total_ratings / (len(restaurants) * len(restaurants[0]["ratings"]))
print(f"\nOverall Statistics:")
print(f"Average Rating Across All Restaurants: {overall_average:.2f}")
print(f"Highest Rating Overall: {highest_rating}")
print(f"Lowest Rating Overall: {lowest_rating}")
