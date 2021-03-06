from .models import Size, Product, Category, Customer, Ordered, OrderedProduct, Location, Topping, ToppingsCollection, OrderedTopping
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class GetOrderedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordered
        fields = "__all__"


class OrderedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordered
        # fields = "__all__"
        exclude = ["customer"]

    def create(self, validated_data):
        customer = self.context.get("customer")
        order = Ordered.objects.create(
            OrderId=validated_data["OrderId"], customer=customer, destination=validated_data["destination"],
            logistics=validated_data["logistics"], total=validated_data["total"])
        order.save()
        return order


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = ["id", "name",
                  "quantity", "price", "size", "product"]

    def create(self, validated_data):
        purchaseId = self.context.get("purchaseId")
        # toppings = self.context.get("toppings")

        Product = OrderedProduct.objects.create(name=validated_data["name"],
                                                quantity=validated_data["quantity"], price=validated_data["price"],
                                                size=validated_data["size"],
                                                purchaseId=purchaseId, product=validated_data["product"])
        Product.save()
        # for item in toppings:
        #     Product.toppings.add(int(item))
        # return Product


class OrderedToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedTopping
        fields = ["id", "name",
                  "quantity", "price", "topping"]

    def create(self, validated_data):
        purchaseId = self.context.get("purchaseId")
        # toppings = self.context.get("toppings")

        Product = OrderedTopping.objects.create(name=validated_data["name"],
                                                quantity=validated_data["quantity"], price=validated_data["price"],
                                                purchaseId=purchaseId, topping=validated_data["topping"])
        Product.save()


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = "__all__"


class ToppingsCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToppingsCollection
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "last_login", "is_active",
                   "is_superuser", "groups", "user_permissions"]
