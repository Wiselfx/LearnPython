distance_mi = 3
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False

if bool(distance_mi) == False:
    print('False')
elif distance_mi <= 1 and is_raining == False:
    print('True')
elif 1 < distance_mi <= 6 and has_bike == False and is_raining == True:
    print('False')
elif distance_mi <= 6 and has_bike == False and is_raining == False:
    print('False')
elif distance_mi <= 6 and has_bike == True and is_raining == False:
    print('True')
elif distance_mi >= 6 and (has_ride_share_app == True or has_car == True):
    print('True')
else:
    print('False')
