import json
from google.cloud import bigquery

with open('config.json') as f:
    data = f.read()
config = json.loads(data)

SELECT_STMT = """
select flight, sum(total_no_of_words)  as total_no_of_words
from `{dataset}.{table}`
group by flight
""".format(dataset=config["DATASET"],
           table=config["TABLE"])

bigquery_client = bigquery.Client(config["PROJECT"],)

def get_flight_message_aggregation(request):
    query_job = bigquery_client.query(SELECT_STMT)

    response = [{"flight":row["flight"],
                 "total_no_of_words": row["total_no_of_words"]} for row in query_job]
    return json.dumps(response)