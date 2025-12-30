from fastapi import APIRouter, Request
from ..core.templates import templates

router = APIRouter()

@router.get("/", name="home")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/dashboard", name="dashboard")
async def dashboard(request: Request):
    # Retrieve resumes using the internal API logic or direct DB access
    # Ideally reuse service/controller logic, but for speed direct DB access here or calling the router function
    from ..db.mongodb import db
    resumes = []
    cursor = db.get_db()["resumes"].find()
    async for document in cursor:
        document["id"] = str(document["_id"]) # Jinja access
        resumes.append(document)
        
    return templates.TemplateResponse("dashboard.html", {"request": request, "resumes": resumes})


@router.get("/builder", name="builder")
async def builder(request: Request):
    return templates.TemplateResponse("builder.html", {"request": request})

@router.get("/p/{resume_id}", name="portfolio_view")
async def view_portfolio(request: Request, resume_id: str):
    from ..db.mongodb import db
    from bson import ObjectId
    
    try:
        resume = await db.get_db()["resumes"].find_one({"_id": ObjectId(resume_id)})
        if not resume:
            return templates.TemplateResponse("404.html", {"request": request}, status_code=404) # Assuming 404 handling or just error
    except:
        # Invalid ID format
        pass 
         
    # Convert for Jinja
    if resume:
        resume["id"] = str(resume["_id"])
    
    return templates.TemplateResponse("portfolio.html", {"request": request, "resume": resume})

