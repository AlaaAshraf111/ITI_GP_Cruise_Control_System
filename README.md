# ITI_GP_Cruise_Control_System
### Features:
1. Infotainment System using QT
2. Cruise control (Normal & Adaptive).
3. Automatic Emergency Braking (AEB)
4. Light System using led matrix.
5. Voice command using IOT

### Used Technologies:
1. STM32F401CC microcontroller (Arm M4 based microprocessor)[GPIO - RCC - NVIC - TIMER - SYSTICK - USART]
2. Raspberry pi 3 (B+)
3. Ultrasonic sensor
4. DC motors & Motor Driver
### Used IDEs:
 - Qt
 - Eclipse
 - Google home APP
### Description:
####    General view of the system:
Since safety is valuable and human nature tends to be more comfortable and make life easier,
Our System is designed to help vehicles maintain a safe following distance and stay within the speed limitations.
It includes both Normal Cruise Control (NCC) and Adaptive Cruise Control (ACC) types.
NCC type; in this mode the car maintains its speed and the user can't accelerate the car above the maintained speed but can deaccelerate the car's speed. If an object is at a distance that is close to the car, an alarm is fired to alert the driver. Also, In case of critical Distance, the car is immediately stops using Automatic Emergency Braking (AEB) system.
###
ACC Type, in this mode also the car maintains its speed and the user can't accelerate the car above the maintained speed but can deaccelerate the car's speed. But the difference here is that the Driver has some ranges of Distance to choose the preferred Distance between his vehicle and the vehicle ahead to adapt the car speed to it.
If a car ahead is slowing down or getting close, the user's car also slows down so it keeps the selected distance between the two cars until it stops, if the other car ahead got so close. Once the car in front starts moving again and the sensor not detecting obstacles ahead, so the car starts accelerating again until it reaches the lately maintained speed on ACC mode.
Also, here, in case of critical Distance, the car is immediately stops using the Automatic Emergency Braking (AEB) system.
