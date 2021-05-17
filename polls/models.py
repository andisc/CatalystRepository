from django.db import models

# Create your models here.
class Stocks(models.Model):
    stock_ticker = models.CharField(primary_key=True, max_length=10)
    stock_name = models.CharField(max_length=200)
    last_price = models.DecimalField(max_digits = 10, decimal_places = 4)
    volume = models.IntegerField()
    exchange = models.CharField(max_length=20, null=True)
    sector = models.CharField(max_length=20, null=True)
    industry = models.CharField(max_length=250, null=True)
    businessSummary = models.CharField(max_length=4000, null=True)
    related_stock = models.CharField(max_length=10, null=True)
    active  = models.IntegerField(default=1)

    class Meta:
        db_table="Stocks"
        verbose_name_plural="Stocks"

    def __str__(self):
        return self.stock_name

class Stocks_Articles(models.Model):
    id=models.AutoField(primary_key=True)
    stock_ticker = models.ForeignKey(Stocks, to_field='stock_ticker', on_delete=models.CASCADE)
    article_text = models.CharField(max_length=500, null=True)
    article_link = models.CharField(max_length=500, null=True)
    article_date = models.DateField(null=True, blank=True)
    creation_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table="Stocks_Articles"
        verbose_name_plural="Stocks_Articles"

    def __str__(self):
        return self.article_text


class Processing_Control(models.Model):
    id_control=models.AutoField(primary_key=True)
    initial_creation_datetime = models.DateTimeField(null=True, blank=True)
    final_creation_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table="Processing_Control"
        verbose_name_plural="Processing_Control"

    def __str__(self):
        return self.id_control


class Logging(models.Model):
    id_log=models.AutoField(primary_key=True)
    id_control = models.ForeignKey(Processing_Control, to_field='id_control', on_delete=models.CASCADE)
    log_state = models.CharField(max_length=20, null=True)
    log_message = models.CharField(max_length=500, null=True)
    creation_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table="Logging"
        verbose_name_plural="Logging"

    def __str__(self):
        return self.id_log


class PreMarketStocks(models.Model):
    stock_ticker = models.CharField(primary_key=True, max_length=10)
    stock_name = models.CharField(max_length=200)
    last_price = models.DecimalField(max_digits = 10, decimal_places = 4)
    grow_price = models.DecimalField(max_digits = 10, decimal_places = 4)
    grow_price_sinal = models.CharField(max_length=1, null=True)
    grow_percentage = models.DecimalField(max_digits = 10, decimal_places = 4)
    active  = models.IntegerField(default=1)
    updated_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table="PreMarketStocks"
        verbose_name_plural="PreMarketStocks"

    def __str__(self):
        return self.stock_name


class MessagesContacts(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    createddate = models.DateTimeField(auto_now_add=True)
    modifiedddate = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="MessagesContacts"
        verbose_name_plural = "MessagesContacts"

