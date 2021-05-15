from book.models import Book
# to run python file on db_shell use below command
# exec(open("D:\\Django\\demo\\book\\db_shell.py").read())
'''
#all data
all_data = Book.objects.all()
print(all_data)
# print("-" * 50)

#single data
sid = 1
b2 = Book.objects.get(id=sid)
print(b2)
# print("-" * 50)

#create data
b3 = Book.objects.create(name= "Thor", author = "Odin",qty = 12,price = 435 )
print(b3.id)
# print("-" * 50)


#update data
sid =2
b4 = Book.objects.get(id= sid)
b4.name = "DSEFD"
b4.author = "aDDSSWW"
b4.qty = 79
b4.save()
# print("-" * 50)



# #delete data
sid =5
b5 = Book.objects.get(id =sid)
b5.delete()
'''
# all_data = Book.objects.all()
# # print(all_data)
# for book in all_data:

# 	print('----Details for ID number:- ',book.id)
# 	print('Book Name :- ',book.name)
# 	print('Book Author :- ',book.author)
# 	print('Quantity :- ',book.qty)
# 	print('Price per book :- ',book.price)


#  for updating and deleting records:
# for book in all_data:
# 	book.qty = 15
# 	book.save()
# 	book.delete()

# all_data = Book.objects.all().values('id','name','qty')
# for i in all_data:
# 	print(list(all_data))

# all_data = Book.objects.all().values_list()
# # print(all_data)
# for i in all_data:
# 	print(i[0])
# import random
# for i in range(1,36):
# 	b = Book(name=chr(random.randint(65,90))*5, author = 'abc', qty=random.randint(1,50) , price=random.randint(200,900))
# 	b.save()
# gt,gte,,lt,lte
# i = insensitive

# books = Book.objects.filter(name__istartswith='J').values('id','name')
# for i in books :
# 	print(i)
# b = Book.objects.all()[0:5]
# print(b)
# Book.objects.bulk_create([(name= "Thor0", author = "Odin",qty = 12,price = 435 ),
# (name= "Thor1", author = "Odin",qty = 152,price = 435 ),
# (name= "Thor2", author = "Odin",qty = 52,price = 435 ),
# (name= "Thor3", author = "Odin",qty = 122,price = 435 )
# (name= "Thor4", author = "Odin",qty = 112,price = 435 )
# ])


# Book.objects.bulk_create([
# Book(name= "Thor0", author = "Odin0",qty = 12,price = 435 ),
# Book(name= "Thor1", author = "Odin1",qty = 152,price = 435 ),
# Book(name= "Thor2", author = "Odin2",qty = 52,price = 435 ),
# Book(name= "Thor3", author = "Odin3",qty = 122,price = 435 )]) 