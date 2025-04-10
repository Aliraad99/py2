import signal
from fastapi import FastAPI
from app.database import engine, Base, get_db
from app.Routes.AuthRoutes import router as AuthRoutes
from app.Routes.UserRoutes import router as UserRoutes
from app.Routes.StreamsRoutes import router as StreamRoutes
from app.Routes.SourceRoutes import router as SourceRoutes


app = FastAPI()

app.include_router(AuthRoutes, prefix="/Auth", tags=["Auth"])
app.include_router(UserRoutes, prefix="/Users", tags=["Users"])
app.include_router(StreamRoutes, prefix="/Streams", tags=["Streams"])
app.include_router(SourceRoutes, prefix="/Sources", tags=["Sources"])

