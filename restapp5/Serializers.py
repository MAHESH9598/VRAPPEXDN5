from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.Serializer):
    class Meta:
        model=Product
        fields=('pid','pname','pcost','pmfdt','pexpdt')