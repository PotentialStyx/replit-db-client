import traceback
import asyncio
import http3
import json
import sys
import os

class RetryError(Exception):
  pass

class retry():
    def __init__(self, f):
        self.f = f

    async def _handle_function(self, func, selfF, *args, **kwargs):
      tb = 'None found if you get this in the stack + error section contact codemonkey51 on discord at coderman51#8112 or by email at pypi@codemonkey51.dev'
      for i in range(0,11):
        try:
          return await func(selfF, *args, **kwargs)
        except:
          tb = traceback.format_exc()
      raise RetryError(func.__name__+' was retried 10 times but got an error each time\n \033[91mstack + error: '+tb)
    async def __call__(self,selfF, *args, **kwargs):
        return await self._handle_function(self.f,selfF, *args, **kwargs)


#requests_async = http3.AsyncClient()
import requests_async


def DeprecationWarning(text):
    print(f"\033[1;31mDeprecationWarning: {text}\033[0;0m")


class Client():
    def __init__(self, url=os.environ['REPLIT_DB_URL']):
        self.asyncclient = AsyncClient(url)
        self.oldadd = '''def run(self,command,*args,**kwargs):
    try:
      return asyncio.run(command(*args,**kwargs))
    except:
      print('error')
      print(f'await {command}(*{args},**{kwargs})')
      return exec(f'asyncio.run({command}(*{args},**{kwargs}))')'''

    def add(self, **args):
        return asyncio.run(self.asyncclient.add(**args))

    def set(self, **args):
        return asyncio.run(self.asyncclient.set(**args))

    def add_dict(self, add):
        return (asyncio.run(self.asyncclient.add_dict(add)))

    def set_dict(self, add):
        return (asyncio.run(self.asyncclient.set_dict(add)))

    def remove(self, *args):
        asyncio.run(self.asyncclient.remove(*args))

    def remove_list(self, remove):
        return asyncio.run(self.asyncclient.remove_list(remove))

    def view(self, view):
        return (asyncio.run(self.asyncclient.view(view)))

    def view_multiple(self, *args):
        return (asyncio.run(self.asyncclient.view_multiple(*args)))

    def view_multiple_list(self, view):
        return asyncio.run(self.asyncclient.view_multiple_list(view))

    def list(self, item):
        return (asyncio.run(self.asyncclient.list(item)))

    def list_multiple(self, *args):
        return (asyncio.run(self.asyncclient.list_multiple(*args)))

    def list_multiple_list(self, args):
        return asyncio.run(self.asyncclient.list_multiple_list(args))

    def transfer(self, url):
        return asyncio.run(self.asyncclient.transfer(url))

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
    def __init__(self, url=os.environ['REPLIT_DB_URL']):
        self.url = url
    async def add(self, **args):
        DeprecationWarning(
            "add() is deprecated and will be removed in a later version use set() instead"
        )
        await self.set(**args)
    async def set(self, **args):
        keys = list(args.keys())
        for i in keys:
          t = None
          t2 = args.get(i)
          if(isinstance(t2,str)):
            t = t2
          else:
            t = str(json.dumps(t2))
          await requests_async.post(self.url, data={i:t})
    async def add_dict(self, add):
        DeprecationWarning(
            "add_dict() is deprecated and will be removed in a later version use set_dict() instead"
        )
        await self.set_dict(add)
    async def set_dict(self, set):
        for i in list(set.keys()):
            await self.set(**set)
    async def remove(self, *args):
        for i in args:
            await requests_async.delete(self.url + '/' + i)
    async def remove_list(self, remove):
        return await self.remove(*remove)
    async def view(self, view):
        try:
          x = await self._view_json(view)
        except:
          x = await self._view_str(view)
        return (x)
    async def view_multiple(self, *args):
        keys = {}
        for i in args:
            keys.update({i: await self.view(i)})
        return keys
    async def view_multiple_list(self, view):
        return await self.view_multiple(*view)

    async def _view_str(self, view):
        request = await requests_async.get(self.url + '/' + view)
        return (request.text)
    async def _view_str_multiple(self, *args):
        keys = {}
        for i in args:
            keys.update({i: await self._view_str(i)})
        return keys
    async def _view_str_multiple_list(self, view):
        return await self._view_str_multiple(*view)


    async def _view_json(self, view):
        request = await requests_async.get(self.url + '/' + view)
        return (json.loads(request.text))
    async def _view_json_multiple(self, *args):
        keys = {}
        for i in args:
            keys.update({i: await self._view_json(i)})
        return keys
    async def _view_json_multiple_list(self, view):
        return await self._view_json_multiple(*view)


    async def list(self, item):
        request = await requests_async.get(self.url + '?prefix=' + item)
        return (request.text.splitlines())
    async def list_multiple(self, *args):
        data = {}
        for i in args:
            data.update({i: await self.list(i)})
        return (data)
    async def list_multiple_list(self, args):
        return await self.list_multiple(*args)
    async def transfer(self, url):
        tclient = AsyncClient(url.strip())
        await self.set_dict(await tclient.all_dict)

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
