import graphene
from graphene.types import Scalar
from graphql.language import ast


class Location(graphene.ObjectType):
    latitude = graphene.Decimal(description='Latitude')
    longitude = graphene.Decimal(description='Longitude')
    address = graphene.String(description='Navigatable Address')
    descriptor = graphene.String(description='Description of the location')

    def resolve_latitude(self, info):
        return 0

    def resolve_longitude(self, info):
        return 0

    def resolve_address(self, info):
        return 'Buxtehuder Str. 17a, 12345 Loltown'

    def resolve_descriptor(self, info):
        return 'Ne location amk'
