from django.db import models
from django.db.models import QuerySet


class Authentication(models.Model):
    user_nickname = models.CharField('Никнейм', max_length=50)
    user_name = models.CharField('Имя оператора', max_length=50)
    user_lastname = models.CharField('Фамилие оператора', max_length=50)
    user_patronymic = models.CharField('Отчество оператора', max_length=50)
    user_birthday = models.DateField('Дата рождения')
    user_registration = models.DateField('Дата регистрации пользователя')
    user_phone = models.CharField('Телефон оператора', max_length=12)
    user_email = models.EmailField()
    user_photo = models.ImageField(upload_to='static', height_field=None, width_field=None, max_length=100)
    user_rang = models.IntegerField()


class Task(models.Model):
    title = models.CharField('Название задачи', max_length=50)
    task = models.TextField('описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'







# class Customer(models.Model):
#     first_name = models.CharField('Имя',
#         max_length=255, null=False, blank=True
#     )
#     last_name = models.CharField('Фамилия',
#         max_length=255, null=False, blank=True
#     )
#     email = models.EmailField('Email',
#         max_length=255, null=False, blank=True
#     )
#     phone = models.EmailField('Телефон',
#         max_length=255, null=False, blank=True
#     )





# class Research(models.Model):
#     organization = models.ForeignKey(
#         "core.Organization",
#         on_delete=models.deletion.SET_NULL,
#         related_name='organization_researches',
#         db_index=True,
#         null=True,
#         blank=False
#     )
#
#     @property
#     def statement_history(self):
#         return self.research_statement_history.all()



    # def __str__(self):
    #     return self.Customer

#     class Meta:
#         verbose_name = 'Задача'
#         verbose_name_plural = 'Задачи'
#
#     organization = models.ForeignKey(
#         "core.Organization",
#         on_delete=models.deletion.SET_NULL,
#         related_name='organization_customers',
#         null=True,
#         blank=False
#     )
#
#
#     @property
#     def orders(self):
#         return self.customers_orders.all()
#
#
# class Order(models.Model):
#     organization = models.ForeignKey(
#         "core.Organization",
#         on_delete=models.deletion.SET_NULL,
#         related_name='organization_orders',
#         null=True,
#         blank=False
#     )
#     customer = models.ForeignKey(
#         "core.Customer",
#         on_delete=models.deletion.SET_NULL,
#         related_name='customers_orders',
#         null=True,
#         blank=False
#     )
#
#     @property
#     def statement_history(self):
#         return self.order_statement_hisory.all()
#
#
# class Organization(models.Model):
#     last_name = models.CharField('Фамилие',
#         max_length=255, null=False, blank=True
#     )
#
#     first_name = models.CharField('Имя',
#         max_length=255, null=False, blank=True
#     )
#
#     patronymic = models.CharField('Отчество',
#         max_length=255, null=False, blank=True
#     )
#
#     email = models.CharField('Email',
#         max_length=255, null=True, blank=True
#     )
#
#     phone = models.CharField('Телефон',
#         max_length=255, null=False, blank=True
#     )
#
#
#     @property
#     def researches(self) -> QuerySet[Research]:
#         return self.organization_researches.all()
#
#     @property
#     def customers(self) -> QuerySet[Customer]:
#         return self.organization_customers.all()
#
#     @property
#     def orders(self) -> QuerySet[Order]:
#         return self.organization_customers.all()
#
#
#
# class Statement(models.Model):
#     research = models.ForeignKey(
#         "core.Research",
#         on_delete=models.deletion.SET_NULL,
#         related_name='research_statement_history',
#         db_index=True,
#         null=True,
#         blank=False
#     )
#
#     order = models.ForeignKey(
#         "core.Order",
#         on_delete=models.deletion.SET_NULL,
#         related_name='order_statement_history',
#         db_index=True,
#         null=True,
#         blank=False
#     )
