from os import path
from io import open
import re
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, 'papermill_jupytext/version.py')) as f:
    version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    version = version_match.group(1)

setup(
    name='papermill_jupytext',
    version=version,
    author='Marc Wouts',
    author_email='marc.wouts@gmail.com',
    description='Parametrize and run scripts as notebooks with jupytext and papermill',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mwouts/papermill_jupytext',
    packages=find_packages(exclude=['tests']),
    entry_points={'papermill.io': ["txt://=papermill_jupytext:TextFileHandler"]},
    tests_require=['pytest'],
    install_requires=['papermill', 'jupytext'],
    license='MIT',
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Environment :: Console',
                 'Framework :: Jupyter',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'Topic :: Text Processing :: Markup',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7']
)
