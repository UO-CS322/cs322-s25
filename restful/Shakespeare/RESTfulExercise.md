# Exercise: RESTful Shakespeare Insult Generator

## The Challenge
You've been given the small Flask application we looked at a few weeks ago that generates Shakespearean insults by combining words from three columns. Your mission is to transform this into a RESTful API that others can use to create, customize, and play with these creative insults. 

## What You Have
- A Flask application that generates insults like "Thou artless base-court apple-john!"
- Three columns of vocabulary words in `vocab.py`
- A simple web interface at `/insultme`

## Your Mission
Design and implement a RESTful API that makes this insult generator more powerful and fun to use. Think about:
- How might someone want to use this API?
- What features would make it more interesting?
- How can you make it easy for others to integrate with their own applications?

## Getting Creative
Here are some ideas to help you get started:

1. **Insult Generation**
   - What if someone wants to get multiple insults at once?
   - Could they customize how the insults are formatted?
   - Maybe they want to save their favorite insults?

2. **Vocabulary Exploration**
   - How could someone discover new words to use?
   - Should they be able to add their own words?
   - What if they want to see how many possible combinations exist?

3. **Custom Insults**
   - How might someone create their own insult patterns?
   - Could they mix and match words from different columns?
   - What if they want to create themed insults?

4. **Fun Features**
   - Maybe add an "insult of the day"?
   - Could you create an insult battle system?
   - What about insult categories or themes?

## Making It RESTful
As you design your API:
- Think about what resources you're working with
- Choose appropriate HTTP methods
- Design clear and intuitive URLs; remember to use plural nouns for collections and singular nouns for individual resources (avoid verbs)
- Consider how to handle errors gracefully
- Make your responses helpful and informative

## Documentation
When describing your API, help others understand how to use your API by:
- Explaining what each endpoint does
- Providing examples of requests and responses
- Describing any parameters or options
- Including error messages and their meanings

You only need paper and pen to complete this exercise, but if you wish, you can use this code as a starting point to implement your new API later. For the paper and pen exercise, here is a suggested template for describing each of the REST endpoints you decide to create (you can make up error codes, parameters, etc., these can be anything you like):

> ### Example Endpoint Documentation
> 
> ### Endpoint: `GET /api/insults`
> 
> #### Description
> Returns a random Shakespearean insult. Optionally returns multiple insults if specified.
> 
> #### Parameters
> **Query Parameters:**
> - `count` (int, optional): Number of insults to generate (default: 1)
> - `format` (string, optional): Response format - "json" or "text" (default: "json")
> 
> #### Response
> **Success (200 OK):**
> ```json
> {
>     "insults": [
>         "Thou artless base-court apple-john!",
>         "Thou bawdy bat-fowling baggage!"
>     ]
> }
> ```
> 
> **Error (400 Bad Request):**
> ```json
> {
>     "error": "Invalid count parameter. Must be between 1 and 10."
> }
> ```
> 
> #### Example Usage
> ```bash
> curl -X GET "http://localhost:7005/api/insults?count=2&format=json"
> ```
> 
> #### Notes
> - Maximum of 10 insults can be requested at once
> - If format is "text", returns plain text with one insult per line

## Evaluation
After you create some endpoints and write them down, switch papers with another student (team) and evaluate each other's work.
- How well you follow REST principles
- The creativity and usefulness of your endpoints
- How well you handle errors and edge cases
- The clarity of your documentation
- The quality of your tests
