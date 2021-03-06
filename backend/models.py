from django.db import models


class Size(models.Model):
    """Model definition for Size."""

    size = models.CharField(verbose_name="size", max_length=150)
    price = models.IntegerField(verbose_name="price")

    class Meta:
        """Meta definition for Size."""

        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        """Unicode representation of Topping."""
        return f'{self.size}-{self.price}'


class Topping(models.Model):
    """Model definition for Topping."""

    topping = models.CharField(verbose_name="topping", max_length=150)
    price = models.IntegerField(verbose_name="price")

    class Meta:
        """Meta definition for Topping."""

        verbose_name = 'Topping'
        verbose_name_plural = 'Toppings'
        ordering = ['topping']

    def __str__(self):
        """Unicode representation of Topping."""
        return f'{self.topping}-{self.price}'


class ToppingsCollection(models.Model):
    """Model definition for ToppingsCollection."""

    # TODO: Define fields here
    name = models.CharField(verbose_name="name", max_length=150)
    toppings = models.ManyToManyField(
        Topping, verbose_name="toppings", related_name="toppings", blank=True)

    class Meta:
        """Meta definition for ToppingsCollection."""

        verbose_name = 'ToppingsCollection'
        verbose_name_plural = 'ToppingsCollections'

    def __str__(self):
        """Unicode representation of ToppingsCollection."""
        return self.name


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(verbose_name='name', max_length=200)
    image = models.ImageField(verbose_name="image", default="image")
    # flavour = models.CharField(
    #     verbose_name="flavour", max_length=200, blank=True, default="null")
    # toppings = models.ManyToManyField(
    #     Topping, verbose_name="toppings", related_name="toppings", blank=True)
    description = models.TextField(verbose_name="description")
    price = models.IntegerField(verbose_name="price", blank=True, default=0)
    multipleSIzes = models.ManyToManyField(
        Size, verbose_name="multiplesizes", related_name="multiplesizes", blank=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(verbose_name="name", max_length=150)
    products = models.ManyToManyField(
        Product, verbose_name="products", blank=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Customer(models.Model):
    """Model definition for Customer."""

    fullName = models.CharField(verbose_name="full name", max_length=250)
    email = models.EmailField(verbose_name="email", max_length=254)
    address = models.CharField(verbose_name="address", max_length=256)
    phoneNumber = models.CharField(verbose_name="phone Number", max_length=50)

    class Meta:
        """Meta definition for Customer."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        """Unicode representation of Customer."""
        return self.fullName


class Ordered(models.Model):
    OrderId = models.CharField(verbose_name='Order Id', max_length=50)
    customer = models.ForeignKey(
        Customer, verbose_name="customer", on_delete=models.CASCADE, related_name='customer')
    total = models.IntegerField(verbose_name="total", default=1)
    logistics = models.IntegerField(verbose_name="total", default=0)
    destination = models.CharField(
        verbose_name="destination", max_length=150, default="null")
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.OrderId

    class Meta:
        managed = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created']


class OrderedProduct(models.Model):
    name = models.CharField(verbose_name="name", max_length=156)
    # flavour = models.CharField(verbose_name="flavour",
    #                            max_length=156, default="null")
    # toppings = models.ManyToManyField(
    #     Topping, verbose_name="toppings", related_name="orderedtoppings", blank=True)

    quantity = models.IntegerField(verbose_name="quantity", default=0)
    price = models.IntegerField()
    size = models.CharField(max_length=50, blank=True, default="", null=True)
    purchaseId = models.ForeignKey(
        Ordered, verbose_name="purchase id", on_delete=models.CASCADE, related_name='purchaseId')
    product = models.ForeignKey(
        Product, verbose_name="product", on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'OrderedProduct'
        verbose_name_plural = 'OrderedProducts'


class OrderedTopping(models.Model):
    name = models.CharField(verbose_name="name", max_length=156)
    quantity = models.IntegerField(verbose_name="quantity", default=0)
    price = models.IntegerField()
    purchaseId = models.ForeignKey(
        Ordered, verbose_name="purchase id", on_delete=models.CASCADE, related_name='purchaseIdTopping')
    topping = models.ForeignKey(
        Topping, verbose_name="topping", on_delete=models.CASCADE, related_name='orderedtopping')

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'OrderedTopping'
        verbose_name_plural = 'OrderedToppings'


class Location(models.Model):
    """Model definition for Location."""
    location = models.CharField(verbose_name="location", max_length=150)
    price = models.IntegerField(verbose_name="price")

    # TODO: Define fields here

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ["location"]

    def __str__(self):
        """Unicode representation of Location."""
        return self.location
