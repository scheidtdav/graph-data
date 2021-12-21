import graphene

from schemas.location import Location


class Query(graphene.ObjectType):
    location = graphene.Field(Location)


def generate_schema():
    return graphene.Schema(query=Query)
