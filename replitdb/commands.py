import replitdb
def commandHandler(args,url):
  client = replitdb.Client(url)
  command = args[0].lower()
  if(command=='add'):
    sub = args[1].split('=')
    client.add_dict({sub[0]:sub[1]})
  elif(command=='remove'):
    client.remove(args[1])
  elif(command=='list'):
    print(client.list(args[1]))
  elif(command=='view'):
    print(client.view(args[1]))
  elif(command=='search'):
    print(client.list(args[1]))
  elif(command=='all'):
    print(client.all_dict)
  elif(command=='wipe'):
    client.wipe
    print("wiped")
  else:
    print(f"{command} is not a valid command")
