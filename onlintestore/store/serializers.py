from rest_framework import serializers

from .models import Category, HistoryOfChanges, Product


class ChangeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryOfChanges
        fields = ("date_of_change", "old_quantity", "new_quantity")


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ("name", "description", "category", "price", "quantity")


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "category", "price", "quantity")


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    change_history = ChangeHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "category",
            "price",
            "quantity",
            "change_history",
        )


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("name", "description", "product_count")

    def get_product_count(self, obj):
        return obj.product_set.count()
