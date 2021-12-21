import os

from schemas.schema import generate_schema
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

try:
    path = os.environ["STARLETTE_BASE_URL"]
except KeyError:
    path = "/"

try:
    is_debug = os.environ["DEBUG"]
except KeyError:
    is_debug = True

schema = generate_schema()
app = Starlette(debug=is_debug)

app.mount(path, GraphQLApp(schema, on_get=make_graphiql_handler()))
