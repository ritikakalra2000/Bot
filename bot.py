#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pickle
from socialbot import Bot
pickle_in=open('bot.pickle','rb')
bot=pickle.load(pickle_in)


# In[7]:


import fastapi


# In[9]:


from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import json
from selenium.common.exceptions import ElementClickInterceptedException


# In[10]:


app=FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    i=0
    b=" "
    while(i<len(exc.errors())) :
        if (exc.errors()[i]['type']=="type_error.float"):
            b=b+"    "+ exc.errors()[i]['loc'][1]+ " has been given wrong data type"
        elif (exc.errors()[i]['type']=="value_error.missing"):
            b=b+"    "+ exc.errors()[i]['loc'][1]+" is missing"
        else:
            b=exc.errors()
        i=i+1
    return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"detail": b}),
        )

class Item(BaseModel):
    user: str
    passw: str
    hasht: str
@app.put("/insta")
async def instag(item: Item):
    recieved=item.dict()
    #action=bot(recieved['user'],recieved['passw'],recieved['hasht'])
    
    return {"done"}


# In[ ]:




