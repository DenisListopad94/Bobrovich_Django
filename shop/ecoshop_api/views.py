from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from django.shortcuts import render, HttpResponse
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import VendorApi, ShipperApi
from .serializers import VendorApiSerializer, ShipperApiSerializer
from .paginations import BaseSetPagination

# def get_vendors(request):
#     vendors = VendorApi.objects.all()
#     return HttpResponse('ok')


# class VendorsList(APIView):
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         vendors = [
#             {'name': vendor.name, 'address': vendor.address, 'email': vendor.email, 'phone': vendor.phone}
#             for vendor in VendorApi.objects.all()
#         ]
#         return Response(vendors)
#
#     def post(self, request, format=None):
#         serializer = VendorApiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorsList(ListCreateAPIView):
    queryset = VendorApi.objects.all()
    serializer_class = VendorApiSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['name', 'address']
    ordering_fields = '__all__'
    ordering = ['name']
    search_fields = ['name', 'address']


class VendorDetail(APIView):

    def get_object(self, pk):
        try:
            return VendorApi.objects.get(pk=pk)
        except Exception:
            raise Http404

    def get(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorApiSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorApiSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vendor = self.get_object(pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ShippersList(ListAPIView):
#     queryset = ShipperApi.objects.all()
#     serializer_class = ShipperApiSerializer


class ShippersList(ListCreateAPIView):
    queryset = ShipperApi.objects.all()
    serializer_class = ShipperApiSerializer
    pagination_class = BaseSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'address']
    ordering_fields = ['name', 'address']


# class ShipperDetail(RetrieveModelMixin,
#                     UpdateModelMixin,
#                     DestroyModelMixin,
#                     GenericAPIView):
#     queryset = ShipperApi.objects.all()
#     serializer_class = ShipperApiSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class ShipperDetail(RetrieveUpdateDestroyAPIView):
    queryset = ShipperApi.objects.all()
    serializer_class = ShipperApiSerializer



