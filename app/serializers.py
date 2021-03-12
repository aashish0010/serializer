from rest_framework import serializers

class HomeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    roll = serializers.IntegerField()
    address = serializers.CharField(max_length=100)