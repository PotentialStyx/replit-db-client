import requests_async
import asyncio
import os
def DeprecationWarning(text):
  print(f"\033[1;31mDeprecationWarning: {text}\033[0;0m")
class Client():
  def __init__(self,url=os.environ['REPLIT_DB_URL']):
    self.asyncclient = AsyncClient(url)
    self.oldadd = '''def run(self,command,*args,**kwargs):
    try:
      return asyncio.run(command(*args,**kwargs))
    except:
      print('error')
      print(f'await {command}(*{args},**{kwargs})')
      return exec(f'asyncio.run({command}(*{args},**{kwargs}))')'''
  def add(self,**args):
    return asyncio.run(self.asyncclient.add(**args))
  def set(self,**args):
    return asyncio.run(self.asyncclient.set(**args))
  def add_dict(self,add):
    return(asyncio.run(self.asyncclient.add_dict(add)))
  def set_dict(self,add):
    return(asyncio.run(self.asyncclient.set_dict(add)))
  def remove(self,*args):
    asyncio.run(self.asyncclient.remove(*args))
  def remove_list(self,remove):
    return asyncio.run(self.asyncclient.remove_list(remove))
  def view(self,view):
    return(asyncio.run(self.asyncclient.view(view)))
  def view_multiple(self,*args):
    return(asyncio.run(self.asyncclient.view_multiple(*args)))
  def view_multiple_list(self,view):
    return asyncio.run(self.asyncclient.view_multiple_list(view))
  def list(self,item):
    return(asyncio.run(self.asyncclient.list(item)))
  def list_multiple(self,*args):
    return(asyncio.run(self.asyncclient.list_multiple(*args)))
  def list_multiple_list(self,args):
    return asyncio.run(self.asyncclient.list_multiple_list(args))
  @property
  def all(self):
    return asyncio.run(self.asyncclient.all)
  @property
  def all_dict(self):
    return asyncio.run(self.asyncclient.all_dict)
  @property
  def wipe(self):
    asyncio.run(self.asyncclient.wipe)


class AsyncClient():
  def __init__(self,url=os.environ['REPLIT_DB_URL']):
    self.url = url
  async def add(self,**args):
    DeprecationWarning("add() is deprecated and will be removed in a later version use set() instead")
    await self.set(**args)
  async def set(self,**args):
    keys = list(args.keys())
    for i in keys:
      await requests_async.post(self.url,data={i:args.get(i)})
  async def add_dict(self,add):
    DeprecationWarning("add_dict() is deprecated and will be removed in a later version use set_dict() instead")
    await self.set_dict(add)
  async def set_dict(self,set):
    for i in list(set.keys()):
      await requests_async.post(self.url,data={i:set.get(i)})
  async def remove(self,*args):
    for i in args:
      await requests_async.delete(self.url+'/'+i)
  async def remove_list(self,remove):
    return await self.remove(*remove)
  async def view(self,view):
    request = await requests_async.get(self.url+'/'+view)
    return(request.text)
  async def view_multiple(self,*args):
    keys = {}
    for i in args:
      keys.update({i:await self.view(i)})
    return keys
  async def view_multiple_list(self,view):
    return await self.view_multiple(*view)
  async def list(self,item):
    request = await requests_async.get(self.url+'?prefix='+item)
    return(request.text.splitlines())
  async def list_multiple(self,*args):
    data={}
    for i in args:
      data.update({i:await self.list(i)})
    return(data)
  async def list_multiple_list(self,args):
    return await self.list_multiple(*args)
  @property
  async def all(self):
    return await self.list('')
  @property
  async def all_dict(self):
    return await self.view_multiple(*await self.list(''))
  @property
  async def wipe(self):
    for i in await self.all:
      await self.remove(i)
