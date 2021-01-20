**Activating Virtual Environment**
```pip install virtualenv```

```virtualenv blockchain-env```

**Activate virtual environment**

```source blockchain-env/scripts/activate```

**Install all packages**

```pip3 install -r requirements.txt```

**Run the Tests**

Make sure to activate the virtual env

```python -m pytest/tests```

**Run the application and API**

Make sure to activate the virtual environment

```python -m Backend.app```


**Run a peer instance**

Make sure to activate the virtual environment

```export PEER=True && python -m Backend.app```


**Running the FrontEnd**

```cd frontend```
```npm run start```