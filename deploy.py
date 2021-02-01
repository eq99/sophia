import os
from subprocess import call

version = '0.0.1'

class cd:
  def __init__(self, newPath):
    self.newPath = os.path.expanduser(newPath)

  def __enter__(self):
    self.savedPath = os.getcwd()
    os.chdir(self.newPath)

  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)

with cd('./api/'):
  call(['docker', 'build', '-t', f'sophia-api:{version}', '.'])

with cd('./www'):
  call(['docker', 'build', '-t', f'sophia-www:{version}', '.'])

