from django.db import models


# class Applications(models.Model):
#     application_id= models.AutoField(primary_key=True)
#     code = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     accessKeyId = models.CharField(max_length=100)
#     accessKeySecret = models.CharField(max_length=100)
#     webhookAuthToken = models.CharField(max_length=100)
#     isActive = models.BooleanField()

class Order(models.Model):
    orderId= models.AutoField(primary_key=True)
    # amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price in INR')
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.CharField(max_length=100) 
    note = models.CharField(max_length=200)
    payerName = models.CharField(max_length=200)
    payerEmail = models.CharField(max_length=100)
    payeePhoneCountryCode = models.CharField(max_length=100)
    payeePhoneNumber = models.CharField(max_length=50)
    payeeBankAccountHolderName = models.CharField(max_length=200)
    payeeBankAccountNumber = models.CharField(max_length=200)
    payeeBankAccountIfsc = models.CharField(max_length=200)
    payeeBankAccountType = models.CharField(max_length=200)
    payeeBankAccountPaymentGatewayBeneficiaryIdentifier = models.CharField(max_length=200)
    paymentCollectionWebhookUrl = models.CharField(max_length=200)
    paymentTransferWebhookUrl = models.CharField(max_length=200)
    accessToken = models.CharField(max_length=200)
    paymentGatewayCode = models.CharField(max_length=200)
    paymentGatewayOrderIdentifier = models.CharField(max_length=200)
    paymentGatewayWebhookRequestParameters = models.CharField(max_length=200)
    isActive = models.BooleanField()
    
    def __str__(self):
        return self.orderId



# class Payments(models.Model):
#     paymentId = models.AutoField(primary_key=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL)
#     direction = models.CharField(max_length=200)
#     amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price in INR')
#     datetime = models.DateTimeField(default=timezone.now, editable=False)
#     referenceIdentifier = models.CharField(max_length=200)
#     paymentModeCode = models.CharField(max_length=200)
#     paymentGatewaySettlementStatus = models.CharField()
#     paymentGatewayProperties  = models.JSONField()
#     isActive = models.BooleanField()













