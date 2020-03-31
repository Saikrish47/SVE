from django.db import models
from django.utils import timezone
from django.db.models import Q

from django.conf import settings

# Create your models here.
class BlogPostQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
                    Q(items__icontains=query)
                   
                    )

        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)


    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)

class Prime(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    # items_id = models.AutoField(primary_key=True)

    items = models.CharField(max_length=200,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)

   
    created_date = models.DateTimeField(default=timezone.now)

    saled = models.DateTimeField(blank=True, null=True)

    objects = BlogPostManager()



    def sell(self):
        self.saled = timezone.now()
        self.save()

    def get_absolute_url(self):
        # return f"/blog/post_detail{self.pk}"

        return reverse('detail', kwargs = {'pk':self.pk})



    def __str__(self):
        return self.items 

class Sold(models.Model):
    items = models.ForeignKey(Prime, on_delete = models.CASCADE,blank=True, null=True)
    quantity = models.IntegerField()
    time = models.DateField(blank=True, null=True)

 
    def __str__(self):
        return self.items.items
    

