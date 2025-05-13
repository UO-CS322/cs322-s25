# Rubber duckies

### Step 1: Set Up MongoDB

1. **Install MongoDB:**
   * Download and install MongoDB from its official [website](https://www.mongodb.com/try/download/community). Follow the installation instructions specific to your OS: [Mac](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)[,]() [Linux](https://www.mongodb.com/docs/manual/administration/install-on-linux/), [Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)
2. **Run MongoDB:**
   * Start the MongoDB server. On most systems, this can be done by running `mongod` from the terminal or command prompt.
   * Mac:
     `brew services start mongodb-community@8.0`
   * Linux
     `sudo systemctl start mongod`
   * Windows (see [Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/) docs, or just run in your VM)
3. **Use MongoDB Shell:**
   * Optionally, you can start the MongoDB shell with `mongo` to interact with MongoDB directly.

### Step 2: Install Python Driver

Install the `pymongo` library to allow Python to interface with MongoDB:


```
pip install pymongo
```

### Step 3: Create a Database and Collection

In MongoDB, we'll create a database named `duckdb` and a collection named `ducks`.

### Step 4: Interact with MongoDB Using Python

Here’s a Python script to insert and retrieve rubber duckies from the MongoDB collection:


```
from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient('localhost', 27017)

# Access the database
db = client['duckdb']

# Access the collection
ducks_collection = db['DuckCollection']

# Function to insert a new rubber duck
def insert_duck(name, color, size, rarity):
    duck = {
        "name": name,
        "color": color,
        "size": size,
        "rarity": rarity
    }
    result = ducks_collection.insert_one(duck)
    return result.inserted_id

# Function to retrieve all ducks
def get_all_ducks():
    return list(ducks_collection.find())

# Insert a few rubber duckies
insert_duck("Classic Yellow", "Yellow", "Medium", "Common")
insert_duck("Pirate Duck", "Black", "Small", "Rare")
insert_duck("Glow-in-the-dark Duck", "Green", "Large", "Ultra Rare")

# Retrieve and print all rubber duckies
all_ducks = get_all_ducks()
for duck in all_ducks:
    print(duck)
```

### Explanation

* **MongoClient:** Connects to the MongoDB server running locally on the default port.
* **Database and Collection:** Creates or accesses a database (`duckdb`) and a collection within it (`ducks`).
* **Insert Operation:** The `insert_duck` function adds a document representing a rubber duck to the collection.
* **Find Operation:** The `get_all_ducks` function retrieves all documents from the collection. See more information about `find` at https://www.w3schools.com/python/python_mongodb_find.asp (includes a server that lets you run example pymongo code snippets).

### Step 5: Run the Script

* Ensure your MongoDB server is running.
* Execute the Python script. It will insert sample documents and retrieve them from the collection.

This setup allows you to manage and query a collection of rubber duckies using Python and MongoDB. You can extend this example by adding more attributes, employing complex queries, or integrating it into an application.

# Miscellaneous

## Creating a Database and Collection

MongoDB doesn't require you to explicitly create a database or collection before using them. Simply start using the database and collection names in your code, and MongoDB creates them the first time you use them.

Access (or Create) a Database:

```python
from pymongo import MongoClient

# Connect to the local MongoDB instance
client = MongoClient('localhost', 27017)

# Access (or create) a database named 'duckdb'
db = client['duckdb']
```

Here, duckdb is the database name. It doesn't exist until you perform an operation that writes data to it, but you don't need to explicitly create it beforehand.
Access (or Create) a Collection:

```python
# Access (or create) a collection named 'DuckCollection'
ducks_collection = db['DuckCollection']
```

ducks is the collection name. Like with databases, it will be created automatically when you first store a document in it.

### Important Notes

* No Pre-definition Needed: Unlike relational databases where you need to define a schema before using it, MongoDB is schema-less. Collections and databases are created when they first receive data.
* Automatic Indexing: MongoDB automatically indexes the _id field, which is added to each document by default and serves as a primary key.
* Persistence: The database and collections will persist as long as there is data within them. If you empty a collection or database (by deleting all its documents), MongoDB may remove these from the disk.

By following these steps, you will have a MongoDB database named `duckdb` and a collection named `DuckCollection` as soon as you insert your first document. There's no separate command necessary to create them explicitly in most usage scenarios.
