# barcode-scan
To run:
> gcloud beta functions deploy main --runtime python37 --trigger-http
>curl -X POST <func url> -H "Content-Type:application/json" -d '{"barcode": "737628064502"}'      

