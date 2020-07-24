[![PyPI version](https://badge.fury.io/py/replitdb.svg)](https://pypi.org/project/replitdb) [![Run on Repl.it](https://repl.it/badge/github/codemonkey51/replit-db-client)](https://repl.it/github/codemonkey51/replit-db-client) [![Downloads](https://pepy.tech/badge/replitdb/week)](https://pepy.tech/project/replitdb)

## ReplitDB Client
A Pythonic Client for use with the repl.it DataBase. Created by [Codemonkey51](https://repl.it/@codemonkey51). Documentation by [IreTheKID](https://repl.it/@irethekid).

## Installation
There are many different methods of installing `replitdb` to your enviornment. `pip` is recommended as it is the most stable.

+ Pip: `pip install replitdb`
+ Easy Install: `easy_install replitdb`
+ Git: `$ git clone https://github.com/codemonkey51/replit-db-client replitdb`
+ Replit UPM: `python3 -m poetry init --no-interaction;
python3 -m poetry add replitdb`

## Getting Started
Once you have the package installed, simply import it and define the client to get started:
```py
import replitdb

client = replitdb.Client()
```

## Using the Client
The replitDB client can be used to write, delete, and edit keys/values within your database. Let's say you have your dictionary ready, like so:
```py
import replitdb

client = replitdb.Client()
data = {
	"users" : {
		"name1" : {...},
		"name2" : {...}
	},
	"posts" : {
		"post1" : {...},
		"post2" : {...}
	},
	"codes" : [
		12345,
		67890,
	],
	"sessionID" : "837379829-2"
}
```
You can write to the DB with either:
```py
for key, value in data.items():
	client.set(key=value) 
```
or:
```py
client.set_dict(data)
```
**Editor's Note:** Using the for loop will set 'key' equal to the variable value. Using `client.set_dict({key:value})` is recommended instead.

After adding items to your DB, you may want to remove some. There are different methods to deleting values from the DB:
```py
client.remove("codes") # Deletes the item the key "codes"
client.remove_list(["users", "posts"]) # Deletes a list of items

client.wipe # Wipes the whole DataBase clean
```

## Client Functions

### Adding:
+ `client.set(name=value, name2=value2, ...)` Adds an item with it's name and value.
+ `client.set_dict({key:val})` Adds an item for every key/value pair in the dict.

### Removing:
+ `client.remove(name)` Removes an item by its name.
+ `client.remove_list([key])` Removes a list of items by name.
+ `client.wipe` Clears DB. (Caution: **Cannot Be Undone**)

### Viewing:
+ `client.view(name)` Returns the value of the name (tries to detect if it is a str or ddict/list and returns accordingly).
+ `client.view_multiple(name, name2, ...)` Returns a dictionary with each item being the name/value pair found (tries to detect if it is a str or ddict/list and returns accordingly).
+ `client.view_multiple_list([key])` Returns a dictionary with each item being the key/value pair found in the list (tries to detect if it is a str or ddict/list and returns accordingly).
+ `client.all` Returns all key names.
+ `client.all_dict` Returns the entire DB as a dictionary.

### Viewing internals (async only) (recommended not to call directly)
+ `client._view_str(name)` Returns the value of the name as a string.
+ `client._view_str_multiple(name, name2, ...)` Returns a dictionary with each item being the name/value pair as a string found.
+ `client._view_str_multiple_list([key])` Returns a dictionary with each item being the key/value pair found as a string in the list.
+ `client._view_json(name)` Returns the value of the name json decoded.
+ `client._view_json_multiple(name, name2, ...)` Returns a dictionary with each item being the name/value pair json decoded found json decoded.
+ `client._view_json_multiple_list([key])` Returns a dictionary with each item being the key/value pair json decoded found in the list.

### Searching:
+ `client.list(prefix)` Returns lists of all keys found that start with the prefix.
+ `client.list_multiple(prefix, prefix2, ...)` Returns dict with each item being the prefix/key pair for all keys found that start each prefix.
+ `client.list_multiple_list([prefix])` Returns dict with each item being the prefix/key pair for all keys found that start each prefix in the list passed.

## Async Capabilities

You can use asynchronous functions by defining your client with the `AsyncClient()` class. All functions will become coroutines that need to be awaited. Here are two examples:

```py
import asyncio
import replitdb

client = AsyncClient()
loop = asyncio.get_event_loop()

data = {
	...
}

loop.run_until_complete(client.set_dict(data))
```

```py
import asyncio
import replitdb

client = AsyncClient()

data = {
	...
} 

async def foo():
	await client.set_dict(data)

asyncio.run(foo())
```

## Known Issues

+ Repl.it UPM can't auto-detect package import.
+ Defualt client does not work in asynchronous enviornment.

## Deprecated Functions
+ `client.add(name)` is now `client.set(name)`
+ `client.add_dict({key:val})` is now `client.set_dict({key:val})`
