# FastApiLearningWithMongoDB

![FastAPI official Img](./ImpSS/FastAPI_SS-Doc.png)


### Some important points related to request body :
```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    book_name: str
    author_name: str
    genre: Optional[str] = None
    publish_year: Optional[int] = None

app = FastAPI()

@app.post("/books/")
def create_book(book: Book):
    return book

```
- In the above snippet, the first important point is the import statement where we import BaseModel from `Pydantic`.
- Using the **`BaseMode`**, we create our own data model class **`Book`**. Basically, the Book class inherits from the **`BaseMode`** class. We use standard python types such as **`str`** and **`int`** for the various attributes.
- On similar lines as `query parameters`, when a model attribute has a default value, it is an `optional` field. In the Book class, **`genre`** and **`publish_year`** are optional since we have set a **`default`** value of None for them.
- Once the class is defined, we use it as a parameter in the request handler function **create_book**. If a parameter is not present in the path and it also uses **`Pydantic BaseModel`**, FastAPI automatically considers it as a **request body**. `FastAPI` will read the incoming request payload as **JSON** and convert the corresponding data types if needed. Also, it will perform validation and return an appropriate error response.