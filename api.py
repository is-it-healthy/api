import requests
import json
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

def get_latest_data():
    url = "https://github.com/is-it-healthy/data/releases/download/v1.dat/data.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch the latest data.json")
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = get_latest_data()
    with open("data.json", "w") as file:
        json.dump(data, file)

@app.get("/get_data/{item_id}")
async def read_data(
    item_id: str,
    include_code: bool = Query(True),
    include_name: bool = Query(True),
    include_href: bool = Query(True),
    include_function: bool = Query(True),
    include_more_info: bool = Query(True)
):
    item = data.get(item_id)
    if item:
        response_data = {}
        if include_code:
            response_data["code"] = item["code"]
        if include_name:
            response_data["name"] = item["name"]
        if include_href:
            response_data["href"] = item["href"]
        if include_function:
            response_data["function"] = item["function"]
        if include_more_info:
            response_data["more_info"] = item["more_info"]
        
        return response_data
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/list_items")
async def list_items():
    return data
