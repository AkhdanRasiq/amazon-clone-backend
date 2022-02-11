from django.db import models

class ProductModel(models.Model):
  id      = models.BigAutoField(primary_key=True)
  title   = models.CharField(max_length=100, blank=False, null=False)
  price   = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=False)
  rating  = models.PositiveSmallIntegerField(blank=False, null=False)
  imgUrl  = models.TextField(blank=False, null=False)

  def __str__(self):
    return "{}".format(self.title)
