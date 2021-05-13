import sys

import phonenumbers
from phonenumbers import phonenumber, timezone, carrier, geocoder
#take user phone number
user_phone_num = sys.argv[1]

#Object of phone number
phone_number = phonenumbers.parse(user_phone_num)
#Get timezone of phone number
timezone = timezone.time_zones_for_number(phone_number)
#network provider
Carrier = carrier.name_for_number(phone_number, 'en')
#get the estimated location of a particular number
Region = geocoder.description_for_number(phone_number, 'en')

print(phone_number)
print(timezone)
print(Carrier)
print(Region)
