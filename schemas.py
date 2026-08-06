from pydantic import BaseModel, EmailStr


class LaptopCreate(BaseModel):
    brand: str
    model: str
    processor: str
    ram: str
    price: int

class LaptopResponse(LaptopCreate):
    id: int

    model_config = {"from_attributes": True}



class MobileCreate(BaseModel):
    brand: str
    model: str
    storage: str
    color: str
    price: int

class MobileResponse(MobileCreate):
    id: int

    model_config = {"from_attributes": True}



class WatchCreate(BaseModel):
    brand: str
    model: str
    type: str
    color: str
    price: int

class WatchResponse(WatchCreate):
    id: int

    model_config = {"from_attributes": True}



class TVCreate(BaseModel):
    brand: str
    screen_size: str
    display_type: str
    resolution: str
    price: int

class TVResponse(TVCreate):
    id: int

    model_config = {"from_attributes": True}




class HeadphoneCreate(BaseModel):
    brand: str
    model: str
    type: str
    connectivity: str
    price: int


class HeadphoneResponse(HeadphoneCreate):
    id: int

    model_config = {
        "from_attributes": True
    }



    # ---------------- USER SCHEMAS ----------------

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    model_config = {
        "from_attributes": True
    }


class Token(BaseModel):
    access_token: str
    token_type: str