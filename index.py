from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from api.inget import process_query

app = FastAPI()

# Allow CORS for the React frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def read_root():
    return {"message": "API is Working."}


@app.get("/api/prompts")
async def get_prompt_response(msg: str = Query(...)):
    # Process the message and generate a response
    # response = await process_query(msg)
    # return {"response": response}
    return "API is Working."
