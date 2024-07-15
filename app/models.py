from django.db import models

# Create your models here.
class main(models.Model):
    name= models.CharField(max_length=20)     
    def __str__(self):
        
        return self.name
    
class category(models.Model):
    main_id = models.ForeignKey(main,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="category")
    def __str__(self):
        return self.name
   

class sub_category(models.Model):
    cat_id = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="sub_category")
    def __str__(self):
        return self.name

   

class product(models.Model):
    sub_id = models.ForeignKey(sub_category,on_delete=models.CASCADE)
    cat_id = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    review= models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    detailss = models.TextField()
    image = models.ImageField(upload_to="product")
    def __str__(self):
        return self.name

   





