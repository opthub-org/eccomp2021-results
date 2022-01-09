import json
import sys

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

d = """
query submissions($ts: timestamptz="%s+9:00") {
  submissions_tutorial: solutions_aggregate(
    where: {
      _and: [{match_id: {_gte: 41}}, {match_id: {_lt: 43}}]
      owner: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  submissions: solutions_aggregate(
    where: {
      _and: [{match_id: {_gte: 43}}, {match_id: {_lt: 47}}]
      owner: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  submissions_sop: solutions_aggregate(
    where: {
      _and: [{match_id: {_gte: 43}}, {match_id: {_lt: 45}}]
      owner: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  submissions_mop: solutions_aggregate(
    where: {
      _and: [{match_id: {_gte: 45}}, {match_id: {_lt: 47}}]
      owner: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  players_tutorial: progress_aggregate(
    distinct_on: user_id
    where: {
      _and: [{match_id: {_gte: 41}}, {match_id: {_lt: 43}}]
      user: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  players: progress_aggregate(
    distinct_on: user_id
    where: {
      _and: [{match_id: {_gte: 43}}, {match_id: {_lt: 47}}]
      user: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  players_sop: progress_aggregate(
    distinct_on: user_id
    where: {
      _and: [{match_id: {_gte: 43}}, {match_id: {_lt: 45}}]
      user: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  players_mop: progress_aggregate(
    distinct_on: user_id
    where: {
      _and: [{match_id: {_gte: 45}}, {match_id: {_lt: 47}}]
      user: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  matches_tutorial: progress_aggregate(
    where: {
      _and: [{match_id: {_gte: 41}}, {match_id: {_lt: 43}}]
      user: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  matches: progress_aggregate(
    where: {
      _and: [{match_id: {_gte: 43}}, {match_id: {_lt: 47}}]
      user: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  matches_sop: progress_aggregate(
    where: {
      _and: [{match_id: {_gte: 43}}, {match_id: {_lt: 45}}]
      user: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }

  matches_mop: progress_aggregate(
    where: {
      _and: [{match_id: {_gte: 45}}, {match_id: {_lt: 47}}]
      user: {name: {_neq: "admin"}}
      created_at: {_lte: $ts}
    }
  ){
    aggregate{count}
  }
}
""" % sys.argv[1]

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
results = client.execute(gql(d))
print(json.dumps(results, indent=2))
