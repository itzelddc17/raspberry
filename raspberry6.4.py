import RPi.GPIO as GPIO
import time
import adafruit_dht
from board import *
import datetime
from datetime import date
from openpyxl import load_workbook

def weatherSensor():

    SENSOR_PIN = D19
    dth11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)

    wb = load_workbook('/home/pi/dso/session06/weather.xlsx')
    sheet = wb['Hoja1']

    while True:

        today = date.today()
        now = datetime.datetime.now().time()
        temperature = dht11.temperature
        humidity = dth11.humidity

        if humidity is not None and temperature is not None:
            print(f"Humidity= {humidity:.2f}")
            print(f"Temperature= {temperature:.2f}ºC")
            row = (today, now, temperature, "961.9", humidity)
            sheet.append(row)

            wb.save('/home/pi/dso/session06/weather.xlsx')
        else:
            print("Sensore failure. Check wiring.");
        time.sleep(0.5);

if __name__ == "__main__":
    weatherSensor()

