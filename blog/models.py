from django.db import models

from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()

	def __unicode__(self):
		return self.name

class Entry(models.Model):
	blog = models.ForeignKey(Blog, on_delete="CASCADE")
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateTimeField()
	authors = models.ManyToManyField(Author)

	def __unicode__(self):
		return self.headline


class Categoria(models.Model):
	nome = models.CharField( max_length=128)

class Produto(models.Model):
	nome = models.CharField( max_length=128 )
	valor = models.DecimalField( max_digits=10,
	decimal_places=2, blank=True, null=True )
	categoria = models.ForeignKey(Categoria, on_delete="CASCADE")
