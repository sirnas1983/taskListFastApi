from fastapi import FastAPI
from app.controllers import task_controller

app = FastAPI()

app.include_router(task_controller.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "API de lista de tareas en funcionamiento"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)