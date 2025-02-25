class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(vehicle):
    pass
schoolbus=bus("innova",180,12)    
print("bus name:",schoolbus.name,",max_speed:",schoolbus.max_speed,",mileage:",schoolbus.mileage)