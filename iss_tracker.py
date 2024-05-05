import requests
from convert24 import convert24
from datetime import datetime
import smtplib

HOST = 
MY_EMAIL = 
PASSWORD = 
MY_LAT = 
MY_LONG = 

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

def issOverhead() -> bool:
    #Get Data for ISS coordinates
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    #Set position variables
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if ((MY_LAT-5) <= iss_latitude <= (MY_LAT+5)) and ((MY_LONG-5) <= iss_longitude <= (MY_LONG+5)):
        return True
    return False

def currSky() -> bool:
    curr_time = datetime.now()
    curr_hour = curr_time.hour
    response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Sun rise and Sunset hours
    # sunrise = int(convert24(data["results"]["sunrise"]).split(":")[0])
    # sunset= int(convert24(data["results"]["sunset"]).split(":")[0])

    #Last light hour
    last_light = int(convert24(data["results"]["last_light"]).split(":")[0])
    
    if curr_hour >= last_light:
        return True
    return False

if issOverhead() and currSky():
    with smtplib.SMTP(HOST, port=587) as connection:
        connection.starttls() #Secures the connection
        connection.login(user=MY_EMAIL, password=PASSWORD)
        #Send mail
        connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:The ISS is over head!\n\nLOOK UP!!!"
                        )
    print("Mail sent")
else:
  print("Mail NOT sent")
