from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import VendorApi, ShipperApi


class VendorApiSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return VendorApi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


class ShipperApiSerializer(ModelSerializer):
    class Meta:
        model = ShipperApi
        fields = ['name', 'address', 'email', 'phone']
