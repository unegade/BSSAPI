from fastapi import APIRouter
from starlette.responses import HTMLResponse, RedirectResponse

router = APIRouter()


@router.get("/", tags=['/'])
async def read_users():
    html_body = """
    <a href='/docs'>Doc</a><br/>
    <a href='/redoc'>ReDoc</a>
    """
    return HTMLResponse(html_body)
    # return RedirectResponse(url='/redoc')
