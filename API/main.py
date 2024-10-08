from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from routes import GET_endpoints, POST_endpoints

app = FastAPI(docs_url=config.documentation_url)

app.include_router(router=GET_endpoints.app)
app.include_router(router=POST_endpoints.app)

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)