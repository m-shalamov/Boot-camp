from typing import List, Optional
from pydantic import BaseModel, ValidationError
from datetime import datetime


class User(BaseModel):
    id: int
    name = "Jack"
    data: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"],
}
try:
    user = User(**external_data)
    print(user.friends)
except ValidationError as e:
    print(e.json())
