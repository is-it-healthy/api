import requests
import json
from fastapi import FastAPI, HTTPException, Query

class DataManager:
    def __init__(self, data_file="data.json", data_url="https://github.com/is-it-healthy/data/releases/download/v1.dat/data.json"):
        self.data_file = data_file
        self.data_url = data_url
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            data = self.fetch_latest_data()
            with open(self.data_file, "w") as file:
                json.dump(data, file)
            return data

    def fetch_latest_data(self):
        response = requests.get(self.data_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=500, detail="Failed to fetch the latest data.json")

class MyApp(FastAPI):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager

app = MyApp(data_manager=DataManager())

@app.get("/get_data/{item_id}")
async def read_data(
    item_id: str,
    include_code: bool = Query(True),
    include_name: bool = Query(True),
    include_href: bool = Query(True),
    include_function: bool = Query(True),
    include_more_info: bool = Query(True)
):
    item = app.data_manager.data.get(item_id)
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
    return app.data_manager.data
