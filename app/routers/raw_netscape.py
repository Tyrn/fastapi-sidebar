import os
from fastapi import Request, APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from dotenv import load_dotenv

load_dotenv()

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/raw-netscape", response_class=HTMLResponse)
async def raw_netscape_home():
    return FileResponse("static/html/raw-netscape.html", status_code=200)
