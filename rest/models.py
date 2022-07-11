from django.db import models



class RequestResponseRestapi(models.Model):
    request_response_id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=10)
    request_data = models.TextField()  # This field type is a guess.
    response_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    request_time = models.DateTimeField()
    response_time = models.DateTimeField(blank=True, null=True)
    time_different = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_response_restapi'
