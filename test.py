from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    title = "StarChaser Demo with Jinja2 Templates"
    message = "Message from the server"
    return templates.TemplateResponse("index.html", {"request": request, "title": title, "message": message})


