from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class author(models.Model):
    Aktif=models.BooleanField(default=1)
    Name= models.CharField(u'Name', max_length=250)
    Surname= models.CharField(u'Surname', max_length=250)
    Joined=models.DateField(u'Joined on', default=timezone.now)
    def __unicode__(self):
        #return self. Name
    	#return "Name:%s - Surname:%s" % (self. Name, self.Surname)
    	return "%s %s" % (self. Name, self.Surname)
    class Meta():
    	verbose_name_plural = "authors"
    	verbose_name = "author"
    	
class post(models.Model):
    postauthor= models.ForeignKey(author)
    publish=models.BooleanField(default=1)
    title= models.CharField(u'Title', max_length=250)
    content=models. TextField(u'Content', max_length=3500)
    created=models.DateField(u'Created on', default=timezone.now)
    #CATEGORY_CHOICES= ((MUSIC, 'Music'),(ECONOMICS,'Economics'),(UNSORTED, 'Unsorted'))
    #category=models.CharField(u'Category',max_length=250,choices=CATEGORY_CHOICES, default= UNSORTED)
    def __unicode__(self):
    	return self. title

    class Meta():
    	verbose_name_plural = "posts"
    	verbose_name = "post"
    	
#class category(models.Model):
   # categoryname= models.CharField(u'Category', max_length=250)
   # created=models.DateField(u'Created on', default=timezone.now)
   # def __unicode__(self):
        #return self. categoryname
    	
   # class Meta():
    	#verbose_name_plural = "category"
    	#verbose_name = "categories"