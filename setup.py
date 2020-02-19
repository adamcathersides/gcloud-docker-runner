from setuptools import setup, find_packages
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "gcloud-docker-runner",
    version = "0.0.1",
    author = "Aadm Cathersides",
    author_email = "adamcathersides@gmail.com",
    description = ("Run glcoud and kubectl containers as if they were installed"),
    url='',
    packages = ['gcloud_run'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data = True,
    install_requires = [
        'click',
        'docker'
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    entry_points={
          'console_scripts': [
              'gcloud = gcloud_run.gcloud:run'
          ]
      }
)
