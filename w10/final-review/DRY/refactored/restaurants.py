from statistics import mean
from typing import List, Dict, Callable


def calculate_statistic(ratings: List[float], operation: Callable) -> float:
    """Calculate a statistic (average, max, min) for a list of ratings."""
    return operation(ratings)


def process_restaurant_ratings(
    restaurants: List[Dict], operation: Callable
) -> List[Dict]:
    """Process ratings for all restaurants using the given operation."""
    return [
        {
            "name": restaurant["name"],
            "result": calculate_statistic(restaurant["ratings"], operation),
        }
        for restaurant in restaurants
    ]


def generate_restaurant_report(restaurant: Dict, stats: Dict) -> None:
    """Generate a formatted report for a single restaurant."""
    print(f"\nReport for {restaurant['name']}:")
    print(f"Ratings: {restaurant['ratings']}")
    print(f"Average Rating: {stats['average']:.2f}")
    print(f"Highest Rating: {stats['highest']}")


def calculate_overall_statistics(restaurants: List[Dict]) -> Dict:
    """Calculate overall statistics across all restaurants."""
    all_ratings = [
        rating for restaurant in restaurants for rating in restaurant["ratings"]
    ]
    return {
        "average": mean(all_ratings),
        "highest": max(all_ratings),
        "lowest": min(all_ratings),
    }


def main():
    restaurants = [
        {"name": "Pasta Palace", "ratings": [4.5, 4.2, 4.8, 4.3, 4.6]},
        {"name": "Burger Barn", "ratings": [3.9, 4.1, 3.8, 4.0, 3.7]},
        {"name": "Sushi Spot", "ratings": [4.7, 4.9, 4.8, 4.6, 4.7]},
    ]

    # Calculate restaurant statistics
    averages = process_restaurant_ratings(restaurants, mean)
    highest_ratings = process_restaurant_ratings(restaurants, max)

    # Generate individual reports
    for restaurant, avg, high in zip(restaurants, averages, highest_ratings):
        generate_restaurant_report(
            restaurant, {"average": avg["result"], "highest": high["result"]}
        )

    # Calculate and display overall statistics
    overall_stats = calculate_overall_statistics(restaurants)
    print("\nOverall Statistics:")
    print(f"Average Rating Across All Restaurants: {overall_stats['average']:.2f}")
    print(f"Highest Rating Overall: {overall_stats['highest']}")
    print(f"Lowest Rating Overall: {overall_stats['lowest']}")


if __name__ == "__main__":
    main()
