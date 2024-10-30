from rest_framework.viewsets import ViewSet
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from ..models import Knife, BladeType, Mod


class KnifeSerializer(serializers.ModelSerializer):
    # Make `bladeTypeId` and `mods` fields writable by accepting their primary keys
    bladeTypeId = serializers.PrimaryKeyRelatedField(queryset=BladeType.objects.all())
    mods = serializers.PrimaryKeyRelatedField(queryset=Mod.objects.all(), many=True)

    class Meta:
        model = Knife
        fields = ["id", "userId", "name", "price", "bladeTypeId", "description", "mods"]
        # No need for `depth=1` here since fields are managed explicitly


class KnifeView(ViewSet):
    permission_classes = [permissions.AllowAny]
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
            knife = serializer.save()
            # Set the many-to-many `mods` field after saving the instance
            knife.mods.set(serializer.validated_data["mods"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update an existing knife."""
        try:
            knife = Knife.objects.get(pk=pk)
            serializer = KnifeSerializer(knife, data=request.data, partial=True)
            if serializer.is_valid():
                knife = serializer.save()
                # Update many-to-many field if `mods` is included in the request
                if "mods" in serializer.validated_data:
                    knife.mods.set(serializer.validated_data["mods"])
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
