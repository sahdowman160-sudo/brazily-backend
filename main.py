from fastapi import FastAPI
from routers import add , Pc , food , time ,run , edittime, dachbord , get_dachbord, open_pc , get_open
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تضمين الراوتر داخل التطبيق
app.include_router(add.router)
app.include_router(Pc.router)
app.include_router(food.router)
app.include_router(time.router)
app.include_router(run.router)
app.include_router(dachbord.router)
app.include_router(open_pc.router)
app.include_router(open_pc.router)
app.include_router(get_open.router)
app.include_router(edittime.router
app.include_router(get_dachbord.router)


