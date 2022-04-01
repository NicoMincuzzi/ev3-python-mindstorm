# LEGO® MINDSTORMS Education EV3 MicroPython

For more [details](https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3).

## [Getting started with LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.com/ev3-micropython/)
This guide shows you how to get started writing MicroPython programs for your LEGO® MINDSTORMS® EV3 robots. You’ll learn to do so in three steps:

- Installation: First you’ll prepare your computer by collecting and installing the required tools.
- [EV3 Brick](https://pybricks.com/ev3-micropython/startbrick.html): Next, you’ll learn to work with the EV3 Brick.
- [Creating and running programs](https://pybricks.com/ev3-micropython/startrun.html): Finally, you’ll learn how to create and run a programs.

After you’ve run the first demo program, you’ll be ready to try out the example programs and start inventing your own programs.

## Installation
This page guides you through the steps to collect and install everything you need to start programming.

### What do you need?
The typical configuration of this equipment is summarized in Figure 1.

![overview_label](https://user-images.githubusercontent.com/48289901/150535115-0639dd63-8f1d-43e3-ad64-1b60470533f6.png)

### Preparing your computer
You’ll write your MicroPython programs using Visual Studio Code. Follow the steps below to download, install, and configure this application:

1. Download Visual Studio Code.
2. Follow the on-screen instructions to install the application.
3. Launch Visual Studio Code.
4. Open the extensions tab.
5. Install the EV3 MicroPython extension as shown in Figure 2.

![store_label](https://user-images.githubusercontent.com/48289901/150535555-1c69c7cd-2f06-42e2-bd5d-fb074faa447d.png)

### Preparing the microSD card
To make it possible to run MicroPython programs on your EV3 Brick, you’ll now learn how to install the required tools on your microSD card.

If the microSD card contains files you want to keep, make sure to create a backup of its contents first. See managing files on the EV3 to learn how to backup your previous MicroPython programs if necessary.

This process erases everything on your microSD card, including any previous MicroPython programs on it.

To install the MicroPython tools on your microSD card:

1. Download the [EV3 MicroPython microSD card image](https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3) and save it in a convenient location. This file is approximately 360 MB. You do not need to unzip the file.

2. Download and install a microSD card flashing tool such as Etcher.

3. Insert the microSD card into your computer or card reader.

4. Launch the flashing tool and follow the steps on your screen to install the file you have just downloaded. If you use Etcher, you can follow the instructions below, as shown in Figure 3.

    a. Select the EV3 MicroPython microSD card image file you have just downloaded.
    
    b. Select your microSD card. Make sure that the device and size correspond to your microSD card.
    
    c. Start the flashing process. This may take several minutes. Do not remove the card until the flashing process is complete.

![etcher_label](https://user-images.githubusercontent.com/48289901/150536607-9405f2f8-7065-4d44-9861-2cb9f57830ed.png)

### Updating the microSD card
To update the microSD card, download a new image file using the link above and flash it to the microSD card as described above. Be sure to back up any MicroPython programs you want to save.

You do not need to erase the contents of the microSD card first. This is done automatically when you flash the new image file.
