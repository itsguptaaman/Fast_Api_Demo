### Fast-API Demo

### Create a conda environment
```
conda create -p venv python==3.8 -y
```
### To install Fast-API we need to install two library
1. fastapi
```
pip install fastapi
```

2. uvicorn
```
pip install uvicorn
```

### To run the server : uvicorn file_name:variable_name --reload
* example:
```
uvicorn app:app --reload
```
### After getting the url :http://127.0.0.1:8000/function_name
* example:
```
http://127.0.0.1:8000/hello
```
