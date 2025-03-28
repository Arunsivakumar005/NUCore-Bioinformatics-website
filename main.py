from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
    
app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Task execution simulation
def process_request(username: str, task_type: str):
    print(f"Processing task for {username}: {task_type}")
    # Create the Nextflow command dynamically
    nextflow_command = f"""
    nextflow run nf-core/rnaseq \\
    --input {path_bcl} \\
    --outdir {output_dir} \\
    --genome GRCh38 \\
    -profile singularity
    """
            
    # Execute the command
    result = subprocess.run(nextflow_command, shell=True, capture_output=True, text=True)
    print(result.stdout if result.returncode == 0 else result.stderr)
            
# Home page with form
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
            
# Handle form submission
@app.post("/submit")
async def submit(background_tasks: BackgroundTasks, username: str = Form(...), task_type: str = Form(...)):
    background_tasks.add_task(process_request, username, task_type)
    return {"message": f"Task '{task_type}' submitted for {username}."}
