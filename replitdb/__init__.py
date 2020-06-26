import requests_async
import requests
import os
class Client():
  def __init__(self):
    self.url = os.environ['REPLIT_DB_URL']
  def add(self,**args):
    keys = list(args.keys())
    for i in keys:
      requests.post(self.url,data={i:args.get(i)})
  def remove(self,*args):
    for i in args:
      requests.delete(self.url+'/'+i)
  def view(self,view):
    return(requests.get(self.url+'/'+view).text)
  def view_multiple(self,*args):
    keys = {}
    for i in args:
      keys.update({i:self.view(i)})
    return keys
  def list(self,item):
    return(requests.get(self.url+'?prefix='+item).text.splitlines())
  def list_multiple(self,*args):
    data={}
    for i in args:
      data.update({i:self.list(i)})
    return(data)
  @property
  def all(self):
    return self.list('')
  @property
  def all_dict(self):
    return self.view_multiple(*self.list(''))
  @property
  def wipe(self):
    for i in self.all:
      self.remove(i)


class AsyncClient():
  def __init__(self):
    self.url = os.environ['REPLIT_DB_URL']
  async def add(self,**args):
    keys = list(args.keys())
    for i in keys:
      request = await requests_async.post(self.url,data={i:args.get(i)})
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
