import replitdb.commands
def main():
    import sys
    import os
    del sys.argv[0]
    url = False
    setUrl = os.environ['REPLIT_DB_URL']
    args = []
    for i in sys.argv:
      if(url):
        url = False
        setUrl = i
      elif(i.lower()=='-url'):
        url = True
      else:
        args.append(i)
    try:
      replitdb.commands.commandHandler(args,setUrl)
    except IndexError:
      print('Too little arguments entered (requires at leat 2)')


if __name__ == '__main__':
    main()
