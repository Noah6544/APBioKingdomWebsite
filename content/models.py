from django.db import models

class Domain(models.Model):
    title = models.CharField(max_length=150,primary_key=False,default="",null=True)
    description = models.TextField(max_length=10000,primary_key=False,default="")
    characteristics = models.TextField(max_length=10000,primary_key=False,default="")
    divergent_event = models.TextField(max_length=10000,primary_key=False,default="")
    cell_type = models.TextField(max_length=10000,primary_key=False,default="")
    body_plan = models.TextField(max_length=10000,primary_key=False,default="")
    metabolism = models.TextField(max_length=10000,primary_key=False,default="")
    circulatory = models.TextField(max_length=10000,primary_key=False,default="")
    respiratory = models.TextField(max_length=10000,primary_key=False,default="")
    reproduction = models.TextField(max_length=10000,primary_key=False,default="")
    examples = models.TextField(max_length=10000,primary_key=False,default="")
    vocabulary = models.TextField(max_length=10000,primary_key=False,default="")
    keytraits = models.TextField(max_length=10000,primary_key=False,null=True)



    def __str__(self):
        return self.title

#these are the subheadings that each kingdom will have the information to fill out if that makes sense....
class Subheading(models.Model):
    Domain = models.ForeignKey(Domain, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=150,default="common subheading")
    content = models.TextField(max_length=10000,default='content for this subheading')


    def __str__(self):
        return self.title

class Images(models.Model):
    Domain = models.ForeignKey(Domain,on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=150,primary_key=False,default="",null=True)
    caption = models.TextField(max_length = 1000,primary_key=False,default='pictures caption',blank=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)


    def __str__(self):
        return self.title