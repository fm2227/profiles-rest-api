from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Return a list of api view features"""
        an_apiview = [
            'uses HTTP method as function(get,post,path,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
