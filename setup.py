from setuptools import setup, find_packages
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "python-project",
    version = "0.0.1",
    author = "",
    author_email = "",
    description = ("A prjoect"),
    url='',
    packages = ['package_name'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data = True,
    install_requires = [
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    entry_points={
          'console_scripts': [
              'project-entrypoint = package_name.package_name:run'
          ]
      }
)
