from django.db import models

from data_ocean.models import DataOceanModel


class DrvRegion(DataOceanModel):
    code = models.IntegerField(unique=True)
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=30, unique=True)
    short_name = models.CharField(max_length=5, unique=True)
    capital = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        return self.name


class DrvDistrict(DataOceanModel):
    region = models.ForeignKey(DrvRegion, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DrvCouncil(DataOceanModel):
    region = models.ForeignKey(DrvRegion, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DrvAto(DataOceanModel):
    """
    ATO means "адміністративно-територіальна одиниця". Central Election Comission call that name a city, 
    a district in city, a town and a village
    """
    region = models.ForeignKey(DrvRegion, on_delete=models.CASCADE)
    district = models.ForeignKey(DrvDistrict, on_delete=models.CASCADE)
    council = models.ForeignKey(DrvCouncil, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class DrvStreet(DataOceanModel):
    region = models.ForeignKey(DrvRegion, on_delete=models.CASCADE)
    district = models.ForeignKey(DrvDistrict, on_delete=models.CASCADE)
    council = models.ForeignKey(DrvCouncil, on_delete=models.CASCADE)
    ato = models.ForeignKey(DrvAto, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    previous_name = models.CharField(max_length=100)
    number_of_buildings = models.IntegerField()
    
    def __str__(self):
        return self.name


class ZipCode(DataOceanModel):
    region = models.ForeignKey(DrvRegion, on_delete=models.CASCADE)
    district = models.ForeignKey(DrvDistrict, on_delete=models.CASCADE)
    council = models.ForeignKey(DrvCouncil, on_delete=models.CASCADE)
    ato = models.ForeignKey(DrvAto, on_delete=models.CASCADE)
    code = models.IntegerField()

    def __str__(self):
        return self.code


class DrvBuilding(DataOceanModel):
    region = models.ForeignKey(DrvRegion, on_delete=models.CASCADE)
    district = models.ForeignKey(DrvDistrict, on_delete=models.CASCADE)
    council = models.ForeignKey(DrvCouncil, on_delete=models.CASCADE)
    ato = models.ForeignKey(DrvAto, on_delete=models.CASCADE)
    street = models.ForeignKey(DrvStreet, on_delete=models.CASCADE)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    number = models.CharField(max_length=4)
    
    def __str__(self):
        return self.number