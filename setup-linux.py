# setup-linux.py

from os import environ, mkdir, remove
from os.path import exists, expanduser, join
from platform import machine as machine_architecture
from subprocess import check_call
from sys import version_info
import tarfile

if version_info.major == 2:
  from urllib import urlretrieve
else:
  from urllib.request import urlretrieve

address_julia_linux64 = 'https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.2-linux-x86_64.tar.gz'
address_julia_linux32 = 'https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.2-linux-i686.tar.gz'

def namefile(filename, suffix):
  if not exists(filename + suffix):
    return filename + suffix
  count = 1
  while exists(filename + str(count) + suffix):
    count = count + 1
  return filename + str(count) + suffix


filename = 'juila-1.10'
filesuffix = '.tar.gz'
foldername = expanduser('~/.julia/')
if not exists(foldername):
  mkdir(foldername)
filename = namefile(join(foldername, filename), filesuffix)


try:
  if machine_architecture().endswith('64'):
    urlretrieve(address_julia_linux64, filename)
  else:
    urlretrieve(address_julia_linux32, filename)

  tar = tarfile.open(filename)
  tar.extractall(foldername, tar.getmembers())
finally:
  remove(filename)

target = join(foldername, 'julia-903644385b/bin/julia')
check_call(['ln', '-s', target, '/usr/local/bin/julia'])
'''if target not in environ["PATH"]:
  if exists(expanduser('~/.bashrc')):
    with open(expanduser('~/.bashrc'), 'a') as fout:
      fout.write('export PATH=$PATH:' + target + ' # Added by Pyglrm \n')
  if exists(expanduser('~/.bash_profile')):
    with open(expanduser('~/.bash_profile'), 'a') as fout:
      fout.write('export PATH=$PATH:' + target + ' # Added by Pyglrm \n')
  elif exists(expanduser('~/.profile')):
    with open(expanduser('~/.profile'), 'a') as fout:
      fout.write('export PATH=$PATH:' + target + ' # Added by Pyglrm \n')'''
