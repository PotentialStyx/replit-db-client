[![PyPI version](https://badge.fury.io/py/replitdb.svg)](https://pypi.org/project/replitdb) [![Run on Repl.it](https://repl.it/badge/github/codemonkey51/replit-db-client)](https://repl.it/github/codemonkey51/replit-db-client) [![Downloads](https://pepy.tech/badge/replitdb/week)](https://pepy.tech/project/replitdb)
# replit-db-client
a client for repl db for python

# installing
### repl
on repl you will need to add the package on the packager tab
### everywhare else
install with pip or your prefered python packager

# docs
### import
`import replitdb`
### define the client
`client = replitdb.Client()`
### use async
`client = replitdb.AsyncClient()` (all commands same except with await before them)
### edit keys
##### adding/setting
`client.set(name=value)` note you can set multiple at one time just add a comma and another `name=value` (returns nothing)
`client.set_dict({key:value})` sets all the key value pairs in the passed in dict (returns nothing)
##### removing
`client.remove(name)` like before just add more seperated by commas to do more (returns nothing)
`client.remove_list([key])` removes all keys in the list passed (returns nothing)
##### clearing
`client.wipe` WARNING THIS CANNOT BE UNDONE (returns nothing)
### viewing keys
##### list keys
`client.list(prefix)` list all keys with that in the begining of their name (returns list)
`client.list_multiple(prefix)` you can add more seperated by commas (returns dict)
`client.list_multiple_list([key])` it works like `client.list_multiple` but takes in a list instead (returns dict)
##### viewing keys
`client.view(name)` returns the value
`client.view_multiple(name)` add more seperated by commas (returns dict)
`client.view_multiple_list([key])` it works like `client.view_multiple` but takes in a list instead (returns dict)
##### view all keys
`client.all` returns all key names (returns list)
##### view all data
`client.all_dict` (returns dict)

# known errors
* cant use regualar client in async environment
* repl doesnt auto-install

# deprecated features
`client.add()` and `client.add_dict()` have been moved to `client.set()` and `client.set_dict()`
