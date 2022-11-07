from django.db import models

"""
TODO: work with Foreing keys? I understood that task was only about "dummy" numbers not Foreign key
"""
class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev_atributu_id = models.IntegerField()
    hodnota_atributu_id = models.IntegerField()


class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    products_ids = models.CharField(null=True, max_length=300)
    nazev = models.CharField(max_length=200, null=True)
    obrazek_id = models.IntegerField(null=True)
    attributes_ids = models.CharField(null=True, max_length=200)


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=256, default=False, null=True)
    cena = models.CharField(max_length=100, default=False, null=True)
    mena = models.CharField(max_length=100, default=False, null=True)
    is_published = models.BooleanField(default=False)
    published_on = models.DateTimeField(default=None, null=True)
    description = models.CharField(max_length=300, default=None)

    def __str__(self):
        return self.nazev


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    obrazek = models.CharField(max_length=256)

    def __str__(self):
        return self.obrazek


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.IntegerField()
    obrazek_id = models.IntegerField()
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev


class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=100)
    zobrazit = models.BooleanField(default=False)

    def __str__(self):
        return self.nazev


class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    hodnota = models.CharField(max_length=100)

    def __str__(self):
        return self.hodnota


class ProductAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.IntegerField()
    product = models.IntegerField()

    def __str__(self):
        return self.attribute
