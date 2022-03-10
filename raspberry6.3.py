import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import datetime
from datetime import date
from openpyxl import load_workbook

def weatherSensor():
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4

    wb = load_workbook('/home/pi/Projects/weather.xlsx')
    sheet = wb['Sheet1']

    while True:
        today = date.today()
        now = datetime.datetime.now().time()
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            row = (today, now, temperature, "961.9", humidity)
            sheet.append(row)

            wb.save('/home/pi/Projects/weather.xlsx')
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity));
        else:
            print("Sensore failure. Check wiring.")
        time.sleep(3);

    if __name__ == "__main__":
        weatherSensor()

    if dif_humidity > 0.1 and dif_temperature > 0.1:
        row = (today, now, temperature, "961.9", humidity)
        sheet.append(row)

        wb.save('/home/pi/Projects/weather.xlsx')
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity));