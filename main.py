from typing import Optional

from fastapi import FastAPI, Request, Form, UploadFile, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import uvicorn

app = FastAPI()

#origins = [
#    "*"
#]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str # Required
    price: float # Required
    is_offer: Optional[bool] = None  # Optional


@app.get("/")
async def read_root(res: Response):
    res.status_code = 404
    return {"name":"lee"}

#@app.get("/{id}")
#async def res(res: Response):



@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/json")
async def json_test(req: Request, file: UploadFile = Form(...)):
#    for element in dir(req):
#        if element[0] == "_":
#            continue
#        print(element)

    print('client = ', req.client)
    print('cookies = ', req.cookies)
    print('form = ', req.form)
    print('get = ', req.get)
    print('headers = ', req.headers)
    print('json = ', req.json)
    print('keys = ', req.keys)
    print('method = ', req.method)
    print('path_params = ', req.path_params)
#    print('query_params = ', req.query_params)
    print('receive = ', req.receive)
    print('scope = ', req.scope)
#    print('session = ', req.session)
    print('url = ', req.url)
    print('values = ', req.values)

    print(req.form)
    print(dir(req.form))

#    qp = req.query_params
#    print(qp)
#    print(type(qp))
#    print(dir(qp))
#    print(qp.values())
#    print(qp._dict)
    """
    req.query_params._dict = {"q": "123", "c": "hi"}
    """

#    print(req.values())
#    print(dir(req.values))

#    print(body)

#    print(file)
#    print(dir(file))
#    print('File Size = ', len(file))
    print('####################')
    print('File Name         = ', file.filename)
    print('File Content-Type = ', file.content_type)
    print('####################')

#    print(dir(req.form()))

    return ({"message": "success"})


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        #reload_delay=3.00,
        log_level="info"
    )
