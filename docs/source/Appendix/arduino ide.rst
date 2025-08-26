.. __arduino_ide:

Arduino IDE
=======================

Download the Arduino IDE 2.x.x
-------------------------------

#. Visit `Download Arduino IDE <https://www.arduino.cc/en/software>`_ page.

#. Download the IDE for your OS version.

   .. image:: /Tutorial/img/Install_Arduino_IDE_1.png

Windows
^^^^^^^^

#. Double click the ``arduino-ide_xxxx.exe`` file to run the downloaded file.

#. Read the License Agreement and agree it.

   .. image:: /Tutorial/img/Install_Arduino_IDE_2.png

#. Choose installation options.

   .. image:: /Tutorial/img/Install_Arduino_IDE_3.png

#. Choose install location. It is recommended that the software be installed on a drive other than the system drive.

   .. image:: /Tutorial/img/Install_Arduino_IDE_4.png

#. Then Finish. 

   .. image:: /Tutorial/img/Install_Arduino_IDE_5.png

MacOS
^^^^^^^^

Double click on the downloaded ``arduino_ide_xxxx.dmg`` file and follow the 
instructions to copy the **Arduino IDE.app** to the **Applications** folder, you will see the Arduino IDE installed successfully after a few seconds.

.. image:: /Tutorial/img/Install_Arduino_IDE_6.png
    :width: 800

Linux
"""""""

For the tutorial on installing the Arduino IDE 2.0 on a Linux system, please 
refer `Linux-Install Arduino IDE <https://docs.arduino.cc/software/ide-v2/tutori
als/getting-started/ide-v2-downloading-and-installing#linux>`_

Open the IDE
^^^^^^^^^^^^^

#. When you first open Arduino IDE 2.0, it automatically installs the Arduino AVR Boards, built-in libraries, and other required files.

   .. image:: /Tutorial/img/Install_Arduino_IDE_7.png

#. In addition, your firewall or security center may pop up a few times asking you if you want to install some device driver. Please install all of them.

   .. image:: /Tutorial/img/Install_Arduino_IDE_8.png

#. Now your Arduino IDE is ready!

.. note::
   In the event that some installations didn't work due to network issues or other 
   reasons, you can reopen the Arduino IDE and it will finish the rest of the 
   installation. The Output window will not automatically open after all installations 
   are complete unless you click Verify or Upload.

Installing ESP32 Add-on in Arduino IDE
--------------

   .. image:: /Tutorial/img/核心包.png

①Search for esp32 and select 1.0.6 click the INSTALL button for esp32 by 
Espressif Systems.

   .. image:: /Tutorial/img/ESP106.png

②Installing,this will take a while

   .. image:: /Tutorial/img/ESP1062.png

③Successfully installed platform esp32: 1.0.6

   .. image:: /Tutorial/img/ESP1063.png

Import library function file
--------------

What are Libraries?
^^^^^^^^
Libraries are a collection of code that makes it easy for you to connect to a sensor, display, module, etc. For example, the built-in LiquidCrystal library makes it easy to talk to character LCD displays. There are hundreds of additional libraries
available on the Internet for download. The built-in libraries and some of these additional libraries are listed in the reference. To use the additional libraries, you will need to install them.

How to Install a Libraries
^^^^^^^^
Libraries are often distributed as a ZIP file or folder. The name of the folder is the name of the library. Inside the folder will be a .cpp file, a .h file and often a keywords.txt file, examples folder, and other files required by the library. you can install   3rd party libraries in the IDE. Do not unzip the downloaded library, leave it as is.
In the Arduino IDE, navigate to Sketch > Include Library. At the top of the drop down list, select the option to "Add .ZIP Library''.

   .. image:: /Tutorial/img/L1.png
You will be prompted to select the library you would like to add. Navigate to the .zip file's  location and open it

   .. image:: /Tutorial/img/L2.png
.. note::
   **For demonstration only—add the ZIP library only if your project actually needs it.**

1. Return to **Sketch → Include Library → Add .ZIP Library…**  
2. The new library will now appear at the bottom of the drop-down list and is ready for use in your sketch.  
3. The ZIP archive is automatically extracted into the **libraries** folder inside your Arduino sketches directory.

.. important::
   The library itself is immediately usable, but its examples will **not** appear under **File → Examples** until you **restart the Arduino IDE**.

   .. image:: /Tutorial/img/L3.png