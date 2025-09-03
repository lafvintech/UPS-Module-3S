.. __Upload Code:

Upload Code
==========================

Download the code by clicking this link: `Download Code <https://codeload.github.com/lafvintech/UPS-Module-3S/zip/refs/heads/main>`_
   
The downloaded compressed package contains code, flash_download_tool, and driver installation.


+------+------+
| UPS  | RPi  |
+======+======+
| 5V   | 5V   |
+------+------+
| GND  | GND  |
+------+------+
| SCL  | SCL  |
+------+------+
| SDA  | SDA  |
+------+------+

1. Connect the Raspberry Pi to the UPS Module 3S according to the GPIO pinout above, and be sure to wire up the power terminals as well.

   .. image:: /Tutorial/img/LB004_A2.jpg

2. 
.. code-block:: text

   Open a terminal on the Raspberry Pi and enter:

   .. code-block:: console

      sudo raspi-config

   to launch the configuration interface.
