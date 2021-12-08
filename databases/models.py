from django.db import models


class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    country_of_citizenship = models.CharField(max_length=50)
    country_of_residence = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=20)
    created_ad = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Passenger'


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    flight_id = models.IntegerField()
    status = models.CharField(max_length=20)
    booking_platform = models.CharField(max_length=20)
    created_ad = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Booking'


class FlightManifest(models.Model):
    id = models.IntegerField(primary_key=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)
    # Flight table არ არის სურათზე

    class Meta:
        db_table = 'FlightManifest'


class Baggage(models.Model):
    id = models.IntegerField(primary_key=True)
    weight_in_k = models.FloatField() # decimal(4,2)
    created_ad = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    booking_id = models.ForeignKey(Booking, related_name='productToProductColors', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Baggage'


class BoardingPass(models.Model):
    id = models.IntegerField(primary_key=True)
    qr_code = models.CharField(max_length=65535)
    created_ad = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'BoardingPass'

