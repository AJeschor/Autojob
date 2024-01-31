# autojob/src/webscraper/webscraper_actor.py

import json
import os
import time
from apify_client import ApifyClient

class WebscraperActor:
    def __init__(self, output_directory):
        """
        Initializes a WebscraperActor instance.

        Parameters:
        - output_directory (str): The directory to save the scraped results.
        """
        # Initialize WebscraperActor with an output directory.
        self.RUN_INPUT = {}
        # Initialize RUN_INPUT for Apify actor run.
        self.client = ApifyClient(json.load(open("src/utils/apify_api_token.json", "r"))["APIFY_API_TOKEN"])
        # Create an ApifyClient instance using the API token from the configuration file.
        self.output_directory = os.path.abspath(output_directory)

    def run_actor_once(self):
        """
        Run the Apify actor once without considering the webcrawler_state.
        """
        # Run the Apify actor once.
        self.run_apify_actor()

    def run_apify_actor(self):
        """
        Runs the Apify actor and saves the formatted results to a JSON file.
        """
        # Run the Apify actor and fetch the results.
        formatted_results = []
        run = self.client.actor("misceres/indeed-scraper").call(run_input=self.RUN_INPUT)
        
        # Iterate through the dataset items obtained from the actor run.
        for raw_item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
            # Format the raw data into a structured dictionary.
            formatted_item = {
                "id": raw_item.get("id", ""),
                "company": raw_item.get("company", ""),
                "positionName": raw_item.get("positionName", ""),
                "jobType": raw_item.get("jobType", []),
                "location": raw_item.get("location", ""),
                "salary": raw_item.get("salary", None),
                "postingDateParsed": raw_item.get("postingDateParsed", ""),
                "url": raw_item.get("url", ""),
                "externalApplyLink": raw_item.get("externalApplyLink", ""),
                "companyDescription": raw_item.get("companyInfo", {}).get("companyDescription", ""),
                "description": raw_item.get("description", "")
            }
            formatted_results.append(formatted_item)

        # Get the current date and time for generating a unique output filename.
        current_datetime = time.strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = os.path.join(self.output_directory, f"results_{current_datetime}.json")

        # Write the formatted results to a JSON file.
        with open(output_filename, "w") as file:
            json.dump(formatted_results, file, indent=4)
