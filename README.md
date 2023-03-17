# ITI_GP_Cruise_Control_System
Our target is to design a medical App for measuring the percentage of oxygen in the blood. Based on that we operate the oxygen device remotely. 
### This operation consists of sub_processes as the following:
1. measure the percentage of oxygen using sensor Max 30100 
2. send readings and contact with the oxygen device using Wi-Fi 
3. use "Blynk" App of phones to interface remotely with the ventilator.
### components:
1. NodeMCU
2. Max 30100 Pulse Oximeter Sensor
3. Blynk App 

“Adaptive Cruise Control with Infotainment System”
Features:
1) Infotainment System using QT
2) Cruise control (Normal & Adaptive).
3) Automatic Emergency Braking (AEB)
4) Light System using led matrix.
5) Voice command using IOT

Used Technologies:
-       STM32F401CC microcontroller (Arm M4 based microprocessor)
-       Raspberry pi 3 (B+)
-       LCD touch screen
-       Ultrasonic sensor
-       DC motors & Motor Driver
Used IDEs:
-       Qt
-       Eclipse
-       Google home APP
Description:
1-    General view of the system:
Since safety is valuable and human nature tends to be more comfortable and make life easier,
Our System is designed to help vehicles maintain a safe following distance and stay within the speed limitations.
It includes both Normal Cruise Control (NCC) and Adaptive Cruise Control (ACC) types.
NCC type; in this mode the car maintains its speed and the user can't accelerate the car above the maintained speed but can deaccelerate the car's speed. If an object is at a distance that is close to the car, an alarm is fired to alert the driver. Also, In case of critical Distance, the car is immediately stops using Automatic Emergency Braking (AEB) system.
              ACC Type, in this mode also the car maintains its speed and the user can't accelerate the car above the maintained speed but can deaccelerate the car's speed. But the difference here is that the Driver has some ranges of Distance to choose the preferred Distance between his vehicle and the vehicle ahead to adapt the car speed to it.
If a car ahead is slowing down or getting close, the user's car also slows down so it keeps the selected distance between the two cars until it stops, if the other car ahead got so close. Once the car in front starts moving again and the sensor not detecting obstacles ahead, so the car starts accelerating again until it reaches the lately maintained speed on ACC mode.
Also, here, in case of critical Distance, the car is immediately stops using the Automatic Emergency Braking (AEB) system.
