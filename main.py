from fastapi import FastAPI
from database.database import engine, Base
import models
from router import parent, child

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include Routers
app.include_router(parent.router, prefix="/parent", tags=["Parent"])
app.include_router(child.router, prefix="/child", tags=["Child"])

@app.get("/")
async def root():
    return {"message": "Hello World"}