from pyramid.response import Response
from pyramid.view import view_config
import requests


@view_config(route_name='home')
def my_view(request):
    return Response(requests.get('http://www.example.org').text)
