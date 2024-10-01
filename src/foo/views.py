from django.shortcuts import render
from rest_framework import generics, serializers
from foo.models import FooFile


class FooFileSerializer(serializers.HyperlinkedModelSerializer):
    fname = serializers.FileField(use_url=False, required=False)
    fsize = serializers.ReadOnlyField(source="fname.size")

    class Meta:
        model = FooFile
        fields = ("fname", "fsize")


class FooFileList(generics.ListCreateAPIView):
    http_method_names = ["get", "post"]
    serializer_class = FooFileSerializer
    queryset = FooFile.objects.all()
