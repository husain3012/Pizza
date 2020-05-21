from django.db import models
from django.contrib.postgres.fields import ArrayField


class Receipt(models.Model):
    username = models.CharField(max_length=64)

    def __repr__(self):
        return f'Receipt;- {self.id} -- {self.username}'


class Toppings(models.Model):
    name = models.CharField(max_length=64)

    def __repr__(self):
        return f'Topping = {self.name}'


class Pizza(models.Model):
    type = models.CharField(max_length=64)
    subtype = models.CharField(max_length=64)
    size = models.CharField(max_length=1, choices=[('L', 'Large'), ('S', "Small")])
    price = models.FloatField()

    def __repr__(self):
        return f'PIZZA, {self.type}, {self.subtype}, {self.size}'


class SubsPlatters(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=1, choices=[('L', 'Large'), ('S', "Small")])
    price = models.FloatField()

    def __repr__(self):
        return f'Subs/Dinner Platter {self.name} {self.size} {self.price}'


class SaladsPasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __repr__(self):
        return f'Salads/Pasta {self.name} {self.price}'


class FinalSalads(models.Model):
    salads = models.ForeignKey(SaladsPasta, related_name='order')
    user = models.ForeignKey(Receipt, blank=True)

    def __repr__(self):
        return f'Order Salads:- {self.salads.name}'


class FinalSubs(models.Model):
    subs = ArrayField(models.ForeignKey(SubsPlatters, related_name='order'))
    user = models.ForeignKey(Receipt, blank=True)

    def __repr__(self):
        return f'Order Subs:- {self.subs.name}'


class FinalPizza(models.Model):
    pizza = models.ForeignKey(Pizza, related_name='order')
    topping = ArrayField(models.ForeignKey(Toppings, related_name='order'), blank=True)
    user = models.ForeignKey(Receipt, blank=True)

    def __repr__(self):
        return f"Order Pizza:- {self.pizza.type} {self.topping.name}"



