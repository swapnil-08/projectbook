from django.db import models

# Create your models here.
#app name- book ,model name - book 

class BookActiveManager(models.Manager): #custom manager
    def get_queryset(self):
        return super(BookActiveManager, self).get_queryset().filter(is_deleted="N")

class BookInactiveManager(models.Manager): #custom manager
    def get_queryset(self):
        return super(BookInactiveManager, self).get_queryset().filter(is_deleted="Y")


class Book(models.Model):
	#id is created by django default
	#columns will generate for below fields
	name = models.CharField(max_length =100)
	author = models.CharField(max_length =100)
	qty = models.IntegerField()
	price = models.FloatField() 
	is_published = models.BooleanField(default=False)
	is_deleted = models.CharField(max_length=1,default="N") # y- data dleted n- data preserved
	#columns will generate for below fileds
	
	active_objects = BookActiveManager()
	inactive_objects = BookInactiveManager()
	objects = models.Manager()
	
	def __str__(self):
		return f"{self.id}--{self.name}--{self.author}"

		
	class Meta:
		db_table = "book_info"
# appname_modelname = small case
#create table book (id int unique AUTO_INCREMENT ,name varchar(100),author)

