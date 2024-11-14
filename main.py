from fastapi import FastAPI
from pydantic import BaseModel
from src.Statistics import statistics_generator
from src.CountryDefiner import identify_country_by_prefix
from src.FindAbonnent import find_abonnent
from src.ChartsCreation import chart_generation
from typing import List, Optional
import json

app = FastAPI(debug=True, port=8030)

class Filters(BaseModel):
    type: Optional[str] = None
    app: Optional[str] = None
    number: Optional[str] = None
    duration: Optional[float] = None
    timestamp: Optional[str] = None
    status: Optional[str] = None
    name: Optional[str] = None

class Call(BaseModel):
    type: Optional[str] = None
    app: Optional[str] = None
    number: Optional[str] = None
    duration: Optional[float] = None
    timestamp: Optional[str] = None
    status: Optional[str] = None
    name: Optional[str] = None

class CallHistory(BaseModel):
    call_history: List[Call]

@app.post("/")
def read_root(data: CallHistory):
    calls = data.model_dump().get("call_history")
    statistics = statistics_generator(calls)
    chart_generation(statistics)
    return statistics

@app.post("/filters/")
def filtered_data(filters: Filters):
    test_database_path = 'test_database.json'
    with open(test_database_path, 'r', encoding='utf-8') as file:
        test_database = json.load(file)
    with open('test_operator_database.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    abonnents = data["abonnents"]
    with open('converted_call_history.json', 'r', encoding='utf-8') as file:    
        data = json.load(file)
    calls = data["call_history"]
    abonnent = None
    country = None
    prefix = None
    if filters.get("phone_number") is not None:
        abonnent = find_abonnent(abonnents, filters.get("phone_number"))
    if abonnent:
        print(abonnent.get("phoneNumber", ""), "|", abonnent.get("lastName", ""), "|", abonnent.get("firstName", ""))
    if filters.get("phone_number") is not None:
        country = identify_country_by_prefix(filters.get("phone_number"))
    if country:
        # remaining_number = filters.get("phone_number")[len(prefix):]
        # operator = identify_operator_by_prefix(remaining_number, test_database.get("operator_prefixes").get(prefix))
        operator = "test"
        print(country,"|", operator)
    statistics = statistics_generator(calls, filters)
    return statistics