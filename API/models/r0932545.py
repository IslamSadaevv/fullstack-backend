from pydantic import BaseModel


class ContactFormCreate(BaseModel):
    id: int
    name: str
    email: str
    message: str


class Testimonial(BaseModel):
    id: int
    content: str
    author: str


class Portfolio(BaseModel):
    id: int
    couple_names: str
    image_url: str
