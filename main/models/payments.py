from django.db import models
import logging
import traceback

from . import Ip_whitelist

#gloabal parameters for site
class Payments(models.Model):

    email =  models.EmailField(max_length = 250)                    #email of payee
    amount = models.DecimalField(decimal_places=2, max_digits=5)     #payment amount
    memo = models.CharField(max_length = 250,default = "")           #momo recorded about payment
    
    ip_whitelist = models.ForeignKey(Ip_whitelist,on_delete=models.CASCADE,related_name="ip_whitelist")

    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.email} {self.amount} {self.memo}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-timestamp']