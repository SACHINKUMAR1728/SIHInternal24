from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import user_routes, account_routes
import os

app = FastAPI()
 
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
 
app.include_router(user_routes.router, prefix="/auth")
app.include_router(account_routes.router, prefix="/account")