import json
import sys

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


doc = """
query submissions($match_id: Int!) {
  progress(
    where: {
      match_id: { _eq: $match_id }
      user: { name: { _neq: "admin" } }
    }
    order_by: { user: { name: asc } }
  ){
    match_id
    user { name }
    budget
    submitted
    evaluated
    scored
    created_at
    updated_at
    evaluation_started_at
    evaluation_finished_at
    scoring_started_at
    scoring_finished_at
    scores
  }
}
"""
var = {"match_id": int(sys.argv[1])}

transport = RequestsHTTPTransport(
    url="https://opthub-api.herokuapp.com/v1/graphql",
    verify=True,
    retries=2,
    headers={"x-hasura-admin-secret": "atrIhKym3BoRVy"},
)
client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)
results = client.execute(document=gql(doc), variable_values=var)
print(json.dumps(results, indent=2))
