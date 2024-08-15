import os
import sys
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from queries.r0932545_queries import insert_contact_form_query, get_testimonials_query, \
    get_portfolios_sorted_with_id_query
from models.r0932545 import ContactFormCreate, Testimonial, Portfolio
from database import execute_sql_query, execute_sql_query_with_params
from dotenv import load_dotenv

app = APIRouter()


@app.post("/contact_forms")
def create_contact_form(contact_form: ContactFormCreate):
    try:
        execute_sql_query_with_params(insert_contact_form_query, contact_form.dict())
        return {"message": "contact form has successfully been sent"}
    except Exception as i:
        raise HTTPException(status_code=500, detail=str(i))
