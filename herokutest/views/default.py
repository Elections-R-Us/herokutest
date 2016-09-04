import os

from pyramid.response import Response
from pyramid.view import view_config
from googleapiclient.errors import HttpError
import googleapiclient.discovery as discovery
from pprint import pformat


SEATTLE_UNIVERSITY_ADDRESS = '901 12th Avenue Seattle WA'


@view_config(route_name='home', renderer='templates/test_api.jinja2')
def my_view(request):
    civicinfo_service = discovery.build(
        'civicinfo',
        'v2',
        developerKey=os.environ.get('APIKEY')
    )
    elections = civicinfo_service.elections()
    info_query = elections.voterInfoQuery(
        address=request.params.get('address', SEATTLE_UNIVERSITY_ADDRESS)
    )
    try:
        formatted_response = pformat(info_query.execute())
    except HttpError:
        return Response('bad address?')
    return {'response': formatted_response}
