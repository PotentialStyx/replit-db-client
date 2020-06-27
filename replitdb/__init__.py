import requests_async
import requests
import asyncio
import os
class Client():
  def __init__(self):
    self.asyncclient = AsyncClient()
  def add(self,**args):
    asyncio.run(self.asyncclient.add(**args))
  def remove(self,*args):
    asyncio.run(self.asyncclient.remove(*args))
  def view(self,view):
    return(asyncio.run(self.asyncclient.view(view)))
  def view_multiple(self,*args):
    return(asyncio.run(self.asyncclient.view_multiple(*args)))
  def list(self,item):
    return(asyncio.run(self.asyncclient.list(item)))
  def list_multiple(self,*args):
    return(asyncio.run(self.asyncclient.list_multiple(*args)))
  @property
  def all(self):
    return asyncio.run(self.asyncclient.all)
  @property
  def all_dict(self):
    return asyncio.run(self.asyncclient.all_dict)
  @property
  def wipe(self):
    asyncio.run(self.wipe)


class AsyncClient():
  def __init__(self):
    self.url = os.environ['REPLIT_DB_URL']
  async def add(self,**args):
    keys = list(args.keys())
    for i in keys:
      await requests_async.post(self.url,data={i:args.get(i)})
  async def remove(self,*args):
    for i in args:
      await requests_async.delete(self.url+'/'+i)
  async def view(self,view):
    request = await requests_async.get(self.url+'/'+view)
    return(request.text)
  async def view_multiple(self,*args):
    keys = {}
    for i in args:
      keys.update({i:await self.view(i)})
    return keys
  async def list(self,item):
    request = await requests_async.get(self.url+'?prefix='+item)
    return(request.text.splitlines())
  async def list_multiple(self,*args):
    data={}
    for i in args:
      data.update({i:await self.list(i)})
    return(data)
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
