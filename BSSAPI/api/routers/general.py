from fastapi import APIRouter
from starlette.responses import HTMLResponse, RedirectResponse

router = APIRouter()


@router.get("/", tags=['general'])
async def read_users():
    html_body = """
    <a href='localhost:8000/docs'>Doc</a><br/>
    <a href='localhost:8000/redoc'>ReDoc</a>
    """
    # return HTMLResponse(html_body)
    return RedirectResponse(url='/redoc')
