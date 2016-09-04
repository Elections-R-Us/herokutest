import os

from pyramid.response import Response
from pyramid.view import view_config
import googleapiclient.discovery as discovery


@view_config(route_name='home')
def my_view(request):
    civicinfo_service = discovery.build(
        'civicinfo',
        'v2',
        developerKey=os.environ.get('APIKEY')
    )
    elections = civicinfo_service.elections()
    info_query = elections.voterInfoQuery(address=request.params['address'])
    return Response(str(info_query.execute()))
