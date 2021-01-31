import os
from subprocess import call

version = '0.0.1'

class cd:
  def __init__(self, newPath):
    self.newPath = os.path.epanduser(newPath)

  def __enter__(self):
    self.savedPath = os.gecwd()
    os.chdi(self.newPath)

  def __exit__(self, etype, value, traceback):
    os.chir(self.savedPath)

with cd('./api/'):
  subprocess.call(['docker', 'build', '-t', f'sophia-api:{version}', '.'])

with cd('./www'):
  subprocess.call(['docker', 'build', '-t', f'sophia-www:{version}', '.'])


