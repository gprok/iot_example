from django.db import models

class Sensor(models.Model):
    sensor_id = models.IntegerField()
    datetime_added = models.DateTimeField()
    value = models.IntegerField()

    def __str__(self) -> str:
        return "ID: " + str(self.sensor_id) + ", " + str(self.datetime_added)


