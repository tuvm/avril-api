from rest_framework import viewsets
from src.products.serializers.product import ProductSerializer
from src.products.models.product import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
