from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        requires = f.read().splitlines()
except IOError:
    with open('edmodopythonfilereader.egg-info/requires.txt') as f:
        requires = f.read().splitlines()
        
with open('VERSION') as f:
    version = f.read().strip()

setup(
      # If name is changed be sure to update the open file path above.
      name = "edmodopythonfilereader",
      version = version,
      packages = find_packages(),
      package_dir = {'edmodopythonfilereader':'edmodopythonfilereader'},
      author = 'App',
      author_email = 'ssshah22@asu.edu',
      description = 'Logs Analyzer',
      license = "PSF",
      include_package_data = True,
      ) 
