from django.shortcuts import render
from .models import character
from rest_framework.views import APIView
from rest_framework.response import Response


class CharacterList(APIView):
    def get(self, request, format=None):

        data = []

        characters = character.objects.all()

        for x in characters:
            data.append({"name": x.name})

        return Response(data)
