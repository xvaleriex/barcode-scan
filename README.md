# barcode-scan
Python app that gets a barcode via http request (via Google Cloud Function) and gets product info from Open Food Facts API.
Result is parsed and written in a list using second cloud func, available via url link.

WIP: Currently, addidng a database to a solution.

### Prerequisites

- Google Cloud Project
- [Python dev enviroment set up](https://cloud.google.com/python/setup)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/)

### To run:
> gcloud beta functions deploy main --runtime python37 --trigger-http

>curl -X POST <func url> -H "Content-Type:application/json" -d '{"barcode": "737628064502"}'      

