# badSnake_RasPi
A bad version of Snake utilising the sence HAT module for the RaspberryPi.

___

## Inspiration

I made a version of snake (in Java) during my free time at my internship last summer, since I had an unexpectedly large ammount of it. I had to write it in a text editor due me not beeing allowed to install third-party software on the conpany notebook. The result was, of course, not very polished and included a some bugs, missing documentation and a very s1mple UI (just the termial, using numbers as to display the game). It looked like this:

![grafik](https://user-images.githubusercontent.com/108017809/193322182-3744fd3b-91e5-4238-999e-eb7ec76c04ca.png)

1 is the snakes Body, 2 is the head, and 7 is the apple. 

I later remembered that I had purchased a raspberryPi and senceHat module some time ago, and that the game would work nicely on it. I just had to rewrite the game in Python and utilise the SenseHat API. I dont yet know how to do ... stuff, but I know that I might have to significantly change the code and logic for it to work. 

## Functionality

The badsnake.py file will run on the RasPi with the Sence HAT equiped. The LED-Array will display the game and the Joystick will accept inputs.
When an input is detected, the programm will calculate the next frame and display it on the LED-Array. I think Im poing to use the sense.set_pixels method to 
display the Frame, but since I am very much a newbie when it comes to python and using lists, il will write a function to convert an Array to a list (so I can use Arras and only convert to a list when i need to display the frame). The Snake and apple will be coloured differently. 

## The Sence HAT module

The Sence HAT (Hardware Attached on Top) module is an add-on for the RaspberryPi. 
It has an 8×8 RGB LED matrix, a five-button joystick and includes multible sensors.

## The SenseHat API

The SenseHat API has multible functions to address the LED panel and to detect inputs from the Joystick. 

## Update 2022-01-10

Testing the LED matrix using the set_pixels() method:

![grafik](https://user-images.githubusercontent.com/108017809/193408028-e49ad06e-1df0-4ea1-994d-22ca694958ae.png)


## Sources

https://www.raspberrypi.com/products/sense-hat/

https://pythonhosted.org/sense-hat/api/

https://www.raspberrypi.com/news/introducing-raspberry-pi-hats/
