import json
import os

def rearrange_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    formatted_results = []

    for item in data:
        formatted_item = {
            "id": item.get("id", ""),
            "company": item.get("company", ""),
            "positionName": item.get("positionName", ""),
            "jobType": item.get("jobType", []),
            "location": item.get("location", ""),
            "salary": item.get("salary", None),
            "postingDateParsed": item.get("postingDateParsed", ""),
            "url": item.get("url", ""),
            "externalApplyLink": item.get("externalApplyLink", ""),
            "companyDescription": item.get("companyDescription", ""),
            "description": item.get("description", "")
        }
        formatted_results.append(formatted_item)

    with open(filename, "w") as file:
        json.dump(formatted_results, file, indent=4)

# Iterate through each JSON file in the current directory
for filename in os.listdir():
    if filename.endswith(".json"):
        rearrange_json(filename)
