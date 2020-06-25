import requests
import os
class Client():
  def __init__(self):
    os.system('export REPLIT_DB_URL=$REPLIT_DB_URL')
    self.url = os.environ['REPLIT_DB_URL']
    os.system('export REPLIT_DB_URL=lol gone')
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
