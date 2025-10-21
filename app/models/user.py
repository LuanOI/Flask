from pydantic import BaseModel

class login_pay_load(BaseModel):
    username: str
    password: str