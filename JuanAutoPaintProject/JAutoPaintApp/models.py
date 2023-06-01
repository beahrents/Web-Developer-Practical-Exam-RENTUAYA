from django.db import models

# Create your models here.

class car(models.Model):
   plate_num = models.CharField(max_length=10)
   curr_color = models.CharField(max_length=10)
   target_color = models.CharField(max_length=10)
   objects = models.Manager()

   def getPlateNum(self):
    return self.plate_num
    
    def getCurrColor(self):
        return self.curr_color

    def getTargetColor(self):
        return self.target_color

    def __str__(self):
        return str(self.pk) + ": " + self.plate_num + ": " + self.curr_color + ": " + self.target_color