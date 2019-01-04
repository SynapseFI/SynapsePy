# SynapseFi Python Library

Python wrapper for SynapseFi API
## Code Example
Refer to [samples.md](samples.md) and our [API documentation](https://docs.synapsefi.com/v3.1) for examples.

## Installation
```bash
$ pip install synapsefi
```
Clone repo
```bash
$ git clone https://github.com/SynapseFI/SynapseFi-Python-v2.git
```
Install requirements
```bash
$ cd SynapseFi-Python-v2
$ pip install -r requirements.txt
```

## USAGE
##### Import
```python
import synapsefi
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
    name='synapsefi',
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
$ twine upload dist/synapsefi-{{VERSION NUMBER}}.tar.gz
```
### Testing
Run the following command from the root package directory
```bash
$ python -m unittest discover -s synapsefi.tests -p '*tests.py'
```