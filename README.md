# SynapseFI Python Library
[![PyPI](https://img.shields.io/pypi/v/synapsepy.svg)](https://pypi.org/project/synapsepy/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/synapsepy.svg)](https://pypi.org/project/synapsepy/)
[![PyPI - Status](https://img.shields.io/pypi/status/synapsepy.svg)](https://pypi.org/project/synapsepy/)

Python wrapper for SynapseFI API
## Code Example
Refer to [samples.md](samples.md) and our [API documentation](https://docs.synapsefi.com/) for examples.

## Installation
```bash
$ pip install synapsepy
```
Clone repo
```bash
$ git clone https://github.com/SynapseFI/SynapsePy.git
```
Install requirements
```bash
$ cd SynapsePy
$ pip install -r requirements.txt
```

## USAGE
##### Import
```python
import synapsepy
```
## Development
### Package Deployment
##### 1. Install Requirements
```bash
$ pip install twine
```
##### 2. Setup Source Distribution
Update version number in [setup.py](setup.py):

```python
setup(
	name='synapsepy',
	...
	version='0.0.15' # NEW VERSION NUMBER GOES HERE
	...
)
```
Create the source distribution by running [setup.py](setup.py) using the following command:

```bash
$ python setup.py sdist
```
##### 3. Upload Distribution
Replace `{{VERSION NUMBER}}` with the new version number in the following command then run:
```bash
$ twine upload dist/synapsepy-{{VERSION NUMBER}}.tar.gz
```
### Testing
Run the following command from the root package directory
```bash
$ python -m unittest discover -s synapsepy.tests -p '*tests.py'
```
