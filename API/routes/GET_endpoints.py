import os
import sys
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from queries.r0932545_queries import insert_contact_form_query, get_testimonials_query, \
    get_portfolios_sorted_with_id_query
from models.r0932545 import ContactFormCreate, Testimonial, Portfolio
from database import execute_sql_query, execute_sql_query_with_params
from dotenv import load_dotenv

app = APIRouter()


@app.get("/portfolio/id")
def get_portfolios_sorted_by_id(id: str):
    query = get_portfolios_sorted_with_id_query
    portfolios = execute_sql_query_with_params(query, {'id': id})
    if isinstance(portfolios, Exception):
        raise HTTPException(status_code=500, detail=str(portfolios))
    portfolios_list = []

    for portfolio in portfolios:
        portfolios_list.append({
            "id": portfolio[0],
            "couple_names": portfolio[1],
            "image_url": portfolio[2],
        })

    return {'portfolios': portfolios_list}

# , response_model=List[Testimonial]

@app.get("/coupleTestimonial")
def get_all_movie_bookings():
    testimonials = execute_sql_query(get_testimonials_query)
    if isinstance(testimonials, Exception):
        raise HTTPException(status_code=500, detail=str(testimonials))

    response_data = [Testimonial(**dict(zip(['id', 'content', 'author'], testimonial))) for testimonial in testimonials]
    return response_data
