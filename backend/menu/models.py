from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, 
                             on_delete=models.CASCADE,
                             related_name='categories')
    url = models.URLField()
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', 
                               on_delete=models.CASCADE, 
                               null=True, 
                               blank=True)
    
    def __str__(self):
        return f'{self.parent}, {self.name}'
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    
class Page(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'