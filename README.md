# ruminations
An opinionated view on setting up and maintaining model development projects.

```bash
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r environment/configuration/requirements.txt
```

```bash
cd ruminations
mkdir build
cd build
cmake ..
```

```bash
environment/script/serve_documentation.py $RUMINATIONS $RUMINATIONS_OBJECTS
```
