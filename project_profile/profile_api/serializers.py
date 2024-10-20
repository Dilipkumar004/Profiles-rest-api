from rest_framework import serializers

class HelloSerilizer(serializers.Serializer):
    """Serializers a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)