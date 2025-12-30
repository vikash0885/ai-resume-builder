from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .api import routes, pages

app = FastAPI(title="AI Resume Builder")

# Mount static files
BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

app.include_router(pages.router)
app.include_router(routes.router, prefix="/api")

# Remove root handler as it is now in pages router



