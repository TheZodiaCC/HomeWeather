# HomeWeather

### Build with:
- Raspberry Pi Zero W
- Grove Temp&Humi Sensor (SHT31)
- Grove Base Hat for RPi Zero
- DFROBOT Power Boost & Charger Module (MP2636)
- Adafruit LC709203F Battery monitor
- 3.7V Li-Pol battery

### Installation
1. Connect modules to RPi, for LC709203F follow 
```
https://learn.adafruit.com/adafruit-lc709203f-lipo-lipoly-battery-monitor/python-circuitpython`
```

2. Build docker image
```
sudo docker build -t homeweather .
```

4. Run docker container with access to GPIO
```
sudo docker run --privileged -d \
-p 8080:8080 \
-v <path_to_logs_file_on_rpi>:/HomeWeather/logs \
-v /etc/timezone:/etc/timezone:ro \
-v /etc/localtime:/etc/localtime:ro \
--name homeweather homeweather
```

4. Set container reboot
```
sudo docker update --restart unless-stopped homeweather
```