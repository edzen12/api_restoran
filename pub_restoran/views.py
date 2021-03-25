from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    response = Response({
        'foods': reverse('foods-list', request=request, format=format),
        'departments': reverse('departments-list', request=request, format=format),
    })
    return response
