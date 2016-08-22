from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=64)

class ContractedService(models.Model):
    service_name = models.CharField(max_length=64)
    contract_id = models.IntegerField(blank=True, null=True)
