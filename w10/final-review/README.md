# DRY (Don't Repeat Yourself) Refactoring Exercises

This directory contains three exercises to practice applying the DRY principle in Python when refactoring code. Each exercise consists of an original code snippet (in the `DRY` directory) and its refactored version (in the `DRY/refactored` directory).

## Exercise 1: Command Handler

**Files:**
- `DRY/command.py`: Original implementation using `if-elif-else` statements
- `DRY/refactored/command.py`: Example refactored version (do not look at this until you do your own refactoring)

**Tasks:**
1. Study both implementations
2. Identify the repetitive patterns in the original code
3. Understand how the refactored version eliminates repetition
4. Try adding a new command (e.g., "RESUME") to both versions and compare the effort required

## Exercise 2: Number Processing

**Files:**
- `DRY/number_processor.py`: Original implementation with repeated loop patterns
- `DRY/refactored/number_processor.py`: Refactored example version (do not look at this until you do your own refactoring)

**Tasks:**
1. Study both implementations
2. Identify the repetitive loop patterns in the original code
3. Understand how the refactored version uses a higher-order function
4. Try adding a new operation (e.g., tripling the numbers) to both versions and compare the effort required

## Exercise 3: Restaurant Rating System

**Files:**
- `DRY/restaurants.py`: Original implementation with repeated rating processing patterns
- `DRY/refactored/restaurants.py`: Refactored example version (do not look at this until you do your own refactoring)

**Tasks:**
1. Study both implementations
2. Identify the repetitive rating processing patterns in the original code
3. Understand how the refactored version:
   - Uses higher-order functions for rating calculations
   - Separates reporting from data processing
   - Leverages Python's built-in functions and type hints
4. Try adding a new feature (e.g., calculating rating trends) to both versions and compare the effort required

## How to Use These Exercises

1. Start by running the original versions to understand the functionality
2. Study the refactored versions to see how DRY principles were applied
3. Try to refactor the original versions yourself before looking at the solutions
4. Experiment with extending both versions to understand the benefits of DRY code
