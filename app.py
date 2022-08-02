import os
import uvicorn
import numpy as np
from typing import List
from tensorflow.keras.models import load_model
from fastapi import FastAPI

host = "0.0.0.0" if os.getenv("DOCKER-SETUP") else "127.0.0.1"
maxlen = 20
vocab = {'END','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
char_index = {'u': 0,'l': 1,'g': 2,'t': 3,'s': 4,'z': 5,'END': 6,'i': 7,'f': 8,'j': 9,'x': 10,'k': 11,'m': 12,'q': 13,'e': 14,
 'y': 15,'o': 16,'n': 17,'c': 18,'w': 19,'d': 20,'v': 21,'b': 22,'p': 23,'h': 24,'r': 25,'a': 26}

# Builds an empty line with a 1 at the index of character
def set_flag(i):
    tmp = np.zeros(len(vocab));
    tmp[i] = 1
    return list(tmp)

# Truncate names and create the matrix
def prepare_X(X):
    new_list = []
    trunc_train_name = [str(i)[0:maxlen].lower() for i in X]

    for i in trunc_train_name:
        tmp = [set_flag(char_index[j]) for j in str(i)]
        for k in range(0,maxlen - len(str(i))):
            tmp.append(set_flag(char_index["END"]))
        new_list.append(tmp)

    return new_list

# Import model
model = load_model('my_model')


# Assign an instance of the FastAPI class to the variable "app".
app = FastAPI(title='Gender prediction model')

@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http://localhost:8000/docs."

# Prediction endpoint
@app.post("/predict") 
def prediction(names: List[str]):
    # Prepare input
    X = prepare_X(names)
    # Model prediction    
    gender = model.predict(X)
    gender = ['M' if g[0] >= 0.5 else 'F' for g in gender]
    return gender

# Run app
uvicorn.run(app, host=host, port=8000)