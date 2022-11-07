from rest_framework import serializers
from ukol.models import *


class AttributeNameSerializer(serializers.Serializer):
    nazev = serializers.CharField()
    zobrazit = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return AttributeName.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = AttributeName
        fields = "__all__"


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nazev = serializers.CharField()
    cena = serializers.CharField()
    mena = serializers.CharField()
    is_published = serializers.BooleanField(default=False)
    published_on = serializers.DateTimeField(allow_null=True)
    description = serializers.CharField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Product
        fields = "__all__"


class AttributeValueSerializer(serializers.Serializer):
    hodnota = serializers.CharField()
    id = serializers.IntegerField()

    def create(self, validated_data):
        return AttributeValue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = AttributeValue
        fields = "__all__"


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    obrazek = serializers.CharField()

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Image
        fields = "__all__"


class ProductImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    obrazek_id = serializers.IntegerField()
    product = serializers.IntegerField()
    nazev = serializers.CharField()

    def create(self, validated_data):
        return ProductImage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = ProductImage
        fields = "__all__"


class AttributeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nazev_atributu_id = serializers.IntegerField()
    hodnota_atributu_id = serializers.IntegerField()

    def create(self, validated_data):
        return Attribute.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Attribute
        fields = "__all__"


class CatalogSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    products_ids = serializers.ListField(
        child=serializers.IntegerField(), allow_null=True
    )
    obrazek_id = serializers.IntegerField(allow_null=True)
    nazev = serializers.CharField(allow_null=True)
    attributes_ids = serializers.ListField(
        child=serializers.IntegerField(), allow_null=True
    )

    def create(self, validated_data):
        return Catalog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Catalog
        fields = ["id", "products_ids"]


class AttributeValueSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    hodnota = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        return AttributeValue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = AttributeValue
        fields = "__all__"


class ProductAttributesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    attribute = serializers.IntegerField(allow_null=True)
    product = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        return ProductAttributes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = ProductAttributes
        fields = "__all__"
