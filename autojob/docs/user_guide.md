
# Webscraper

## Apify Token

The webscraper needs an Apify token to function. Create an Apify account for free [here](https://console.apify.com/sign-up) and you will get $5 in free credit every month. A run of the Indeed Scraper actor by Misceres has a rate of $5.00 / 1,000 results, which from my usage costs $0.50 for 100 job post results. You can find your API token on the [Integrations page](https://console.apify.com/account/integrations) in the Apify Console under 'Personal API tokens'.

The Apify token is used in the the JSON file located in the utils directory:

```
Autojob/autojob/src/utils/apify_api_token.json
```

The file has the structure:

```json
{
    "API_TOKEN": "replace_this_with_your_API_token"
}
```

Replace the "replace_this_with_your_API_token" string with your Apify API token, obviously.


## Webscraper Settings

[Source](https://apify.com/misceres/indeed-scraper/input-schema)

The configuration settings for the webscraper component are located in:

```
/Autojob/autojob/src/utils/webscraper_settings.json
```

It has the following structure:

```json
{
  "Webscraper_Settings": {
    "RUN_INPUT": {
      "position": "string (Any combination of positions or keywords for search. If Start URLs are used, search position is disabled.)",
      "country": "Enum (Country codes based on the ISO 3166-1 alpha-2 standard. Default value of this property is 'US'.)",
      "location": "string (Any combination of city, zip code, or locality for search.)",
      "maxItems": "integer (Limit of detail/product pages to be scraped.)",
      "parseCompanyDetails": "boolean (If true, will also navigate to the company page of each job posting to scrape company info not available directly on the job posting page. Default value of this property is 'false'.)",
      "saveOnlyUniqueItems": "boolean (If true, only unique items will be scraped. Default value of this property is 'true'.)",
      "followApplyRedirects": "boolean (If true, will follow redirects of Indeed's externalApplyLink and output the final one. Default value of this property is 'true'.)",
      "maxConcurrency": "integer (Specifies the maximum number of concurrent tasks or requests the Apify Actor will execute simultaneously. Be nice to the website; don't go over 10.)"
    },
    "SCHEDULE_OPTION": "string",
    "SCHEDULED_TIME": "string",
    "SCHEDULED_DAY": "string",
    "SCHEDULED_PERIOD": "string"
  }
}
```

### Input Schema

#### Positions/keywords for search
- **Variable name:** position
- **Data type:** string
- **Requirement:** Optional

Any combination of positions or keywords for search. If Start URLs are used, search position is disabled.

#### Country for search
- **Variable name:** country
- **Data type:** Enum
- **Requirement:** Optional

Country codes based on the ISO 3166-1 alpha-2 standard. Default value of this property is "US".

#### Location for search
- **Variable name:** location
- **Data type:** string
- **Requirement:** Optional

Any combination of city, zip code, or locality for search.

#### Max items
- **Variable name:** maxItems
- **Data type:** integer
- **Requirement:** Optional

Limit of detail/product pages to be scraped.

#### Scrape company details
- **Variable name:** parseCompanyDetails
- **Data type:** boolean
- **Requirement:** Optional

If true, will also navigate to the company page of each job posting to scrape company info not available directly on the job posting page. Default value of this property is "false".

#### Save Only Unique Items
- **Variable name:** saveOnlyUniqueItems
- **Data type:** boolean
- **Requirement:** Optional

If true, only unique items will be scraped. Default value of this property is "true".

#### Follow redirects for apply link
- **Variable name:** followApplyRedirects
- **Data type:** boolean
- **Requirement:** Optional

If true, will follow redirects of Indeed's externalApplyLink and output the final one. Default value of this property is "true".

#### Max concurrency
- **Variable name:** maxConcurrency
- **Data type:** integer
- **Requirement:** Optional

Specifies the maximum number of concurrent tasks or requests the Apify Actor will execute simultaneously.Be nice to the website; don't go over 10.
config
