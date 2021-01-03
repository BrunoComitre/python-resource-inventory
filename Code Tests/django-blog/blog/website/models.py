from django.db import models


# Create your models here.

class Categories(models.TextChoices):  # Categorias do Django admin
    TC = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'
    CC = 'CC', 'Ciência da Computação'
    DS = 'CS', 'Ciência de Dados'

class Post(models.Model):  # Modelo de armazanamento on banco de dados
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.GR,
        )
    # deleted = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)
    
    
    def __str__(self):  # exibir o nome do titulo ao invés da informação do banco
        return self.title
    
    def full_name(self):
        return self.title + self.sub_title
    
    def get_category_label(self):
        return self.get_categories_display()
    
    full_name.admin_order_field = 'tilte'
    
class Contact(models.Model):  # Criando dados de formulário para contato
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):  # exibir o nome do titulo ao invés da informação do banco
        return self.name
