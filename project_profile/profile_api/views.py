from rest_framework.views import APIView  #imports the api view classes
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
                'Uses HTTP methods as function (get, post, patch, put, delete)',
                'Is similar to a traditional Django view',
                'Gives you the most control over you application logic',
                'Is mapped manually to URLs',
        ]

        return Response({"message":"DKS","an_apiview":an_apiview})