from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from ..models import Knife


class KnifeSerializer(serializers.ModelSerializer):
    # Nested serializers for foreign key and many-to-many fields
    blade_type = serializers.StringRelatedField(source="bladeTypeId", read_only=True)
    mods = serializers.StringRelatedField(many=True)  # List of mods by name


class KnifeView(ViewSet):
    """
    A ViewSet for listing, retrieving, creating, updating, and deleting Knife instances.
    """

    def list(self, request):
        """Get a list of all knives."""
        knives = Knife.objects.all()
        serializer = KnifeSerializer(knives, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Get a single knife by ID."""
        try:
            knife = Knife.objects.get(pk=pk)
            serializer = KnifeSerializer(knife)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Knife.DoesNotExist:
            return Response(
                {"message": "Knife not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """Create a new knife."""
        serializer = KnifeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update an existing knife."""
        try:
            knife = Knife.objects.get(pk=pk)
            serializer = KnifeSerializer(knife, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Knife.DoesNotExist:
            return Response(
                {"message": "Knife not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        """Delete a knife by ID."""
        try:
            knife = Knife.objects.get(pk=pk)
            knife.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Knife.DoesNotExist:
            return Response(
                {"message": "Knife not found"}, status=status.HTTP_404_NOT_FOUND
            )

    class Meta:
        model = Knife
        fields = ["id", "userId", "name", "price", "blade_type", "description", "mods"]
        depth = 1  # Expands the `mods` field to show related details if necessary
