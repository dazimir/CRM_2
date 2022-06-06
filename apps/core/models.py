from django.db import models
from django.db.models import QuerySet

class Research(models.Model):
    organization = models.ForeignKey(
        "core.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_researches',
        db_index=True,
        null=True,
        blank=False
    )

    @property
    def statement_history(self):
        return self.research_statement_history.all()


class Customer(models.Model):
    first_name = models.CharField('Имя',
        max_length=255, null=False, blank=True
    )
    last_name = models.CharField('Фамилия',
        max_length=255, null=False, blank=True
    )
    email = models.EmailField('Email',
        max_length=255, null=False, blank=True
    )
    phone = models.EmailField('Телефон',
        max_length=255, null=False, blank=True
    )


    organization = models.ForeignKey(
        "core.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_customers',
        null=True,
        blank=False
    )


    @property
    def orders(self):
        return self.customers_orders.all()


class Order(models.Model):
    organization = models.ForeignKey(
        "core.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_orders',
        null=True,
        blank=False
    )
    customer = models.ForeignKey(
        "core.Customer",
        on_delete=models.deletion.SET_NULL,
        related_name='customers_orders',
        null=True,
        blank=False
    )

    @property
    def statement_history(self):
        return self.order_statement_hisory.all()


class Organization(models.Model):
    last_name = models.CharField('Фамилие',
        max_length=255, null=False, blank=True
    )

    first_name = models.CharField('Имя',
        max_length=255, null=False, blank=True
    )

    patronymic = models.CharField('Отчество',
        max_length=255, null=False, blank=True
    )

    email = models.CharField('Email',
        max_length=255, null=True, blank=True
    )

    phone = models.CharField('Телефон',
        max_length=255, null=False, blank=True
    )


    @property
    def researches(self) -> QuerySet[Research]:
        return self.organization_researches.all()

    @property
    def customers(self) -> QuerySet[Customer]:
        return self.organization_customers.all()

    @property
    def orders(self) -> QuerySet[Order]:
        return self.organization_customers.all()



class Statement(models.Model):
    research = models.ForeignKey(
        "core.Research",
        on_delete=models.deletion.SET_NULL,
        related_name='research_statement_history',
        db_index=True,
        null=True,
        blank=False
    )

    order = models.ForeignKey(
        "core.Order",
        on_delete=models.deletion.SET_NULL,
        related_name='order_statement_history',
        db_index=True,
        null=True,
        blank=False
    )
