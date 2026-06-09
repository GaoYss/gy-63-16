from datetime import date

from pydantic import BaseModel, Field


class PresaleBase(BaseModel):
    title: str = Field(min_length=2, max_length=50)
    fruit_name: str = Field(min_length=2, max_length=30)
    price: float = Field(gt=0)
    original_price: float = Field(gt=0)
    start_date: date
    end_date: date
    pickup_date: date
    quota: int = Field(gt=0)
    reserved: int = Field(default=0, ge=0)


class Presale(PresaleBase):
    id: int
    remaining: int


class PresaleCreate(PresaleBase):
    pass


class PresaleOrderCreate(BaseModel):
    member_id: int = Field(gt=0)
    presale_id: int = Field(gt=0)
    quantity: int = Field(default=1, gt=0)


class PresaleOrder(BaseModel):
    id: int
    member_id: int
    presale_id: int
    quantity: int
    amount: float
    status: str
