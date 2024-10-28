from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from knifeapi.models import Knife


class KnifeView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            knife = Knife.objects.get(pk=pk)
            serialized = KnifeSerializer(knife, many=False)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Knife.DoesNotExist:
            return Response(
                {"message": "Knife not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        knives = Knife.objects.all()
        serialized = KnifeSerializer(knives, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class KnifeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Knife
        fields = (
            "id",
            "userId",
            "name",
            "price",
            "typeId",
            "description",
        )
