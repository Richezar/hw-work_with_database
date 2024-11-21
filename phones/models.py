from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f"{self.id}; {self.name}; {self.price}; {self.image}; {self.release_date}; {self.lte_exists}; {self.slug}"
