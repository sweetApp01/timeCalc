from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .calculator import TimeCalculator

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

calc = TimeCalculator()

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/calculate")
async def do_calculate(
    time1: str = Form(...),
    operator: str = Form(...),
    operand2: str = Form(...)
):
    result = calc.calculate(time1, operator, operand2)
    return {"result": result}
