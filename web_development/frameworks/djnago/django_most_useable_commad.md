--run django project

``` 1. python manage.py runserver 8000 ```

--database migrate (for multiple database)

``` 2. python manage.py makemigrations ```
``` 3. python manage.py migrate --database='database_name' ```

--query in multiple database using ORM (example)

``` 4. data1 = ModelName.objects.using('database_name').get(id=pk) ```
``` 5. data1 = ModelName.objects.using('database_name').filter(last_modified=date) ```

-- exclude items by ORM

``` 6. data = ModelName.objects.filter(field1='value1').exclude(field2='value2') ```

--- select_related and prefetch_related

```
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, releted_name=book_set) 

```

``` 7. author = Author.objects.select_related('book').get(pk=author_id)```
``` 7. authors = Author.objects.all().prefetch_related('book_set')```


