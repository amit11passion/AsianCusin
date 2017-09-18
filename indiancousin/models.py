from django.db import models

class Menu(models.Model):
    menuname=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    logo=models.CharField(max_length=1000)
    def __str__(self):
        return self.menuname+" "+self.description

class  Menuitem(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE)
    itemname=models.CharField(max_length=200)
    itemingredient=models.CharField(max_length=400)
    itemprice=models.IntegerField(default=0)
    is_favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.itemname+" "+str(self.itemprice)