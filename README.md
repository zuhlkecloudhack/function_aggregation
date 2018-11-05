HTTP Cloud function
-------------------

```
virtualenv cloud-function
source cloud-function/bin/activate
pip install -r requirements.txt
```



Deploy function:

```
gcloud beta functions deploy get_flight_message_aggregation \
    --source=./  \
    --region=europe-west1 \
    --runtime python37 \
    --trigger-http

```

```
curl https://europe-west1-cloud-hackathon-zeus.cloudfunctions.net/get_flight_message_aggregation
```
