# beta
### 0.0.10
deprecated add() and add_dict() replaced with set() and set_dict()
### 0.0.9
added command line usage
### 0.0.8
only pre-releases for 0.0.9
### 0.0.7
fised list_multiple_list and view_multiple_list
### 0.0.6
fixed installation errors
### 0.0.5
fixed client.wipe (sync) also added add_dict to add dicts, remove_list to remove the keys in that list, list_multiple_list (same as list_multiple but takes a list not infinite parameters), and view_multiple_list which is view_multiple but takes in a list
### 0.0.4
changed it so that under the cover all commands are async (no changes for user) although the asyncio package is required (should be normally installed by default)
