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

2. Open a terminal on the Raspberry Pi and enter:

   .. code-block:: console

      sudo raspi-config

   to launch the configuration interface.

   .. image:: /Tutorial/img/P1.png
   .. image:: /Tutorial/img/P2.png

   Select Interface Options → I2C → Yes.

   .. image:: /Tutorial/img/P3.png
   .. image:: /Tutorial/img/P4.png
   .. image:: /Tutorial/img/P5.png
   .. image:: /Tutorial/img/P6.png

3. After enabling I2C, download  the example code.
   
   Enter the following command:

   .. code-block:: console

      git clone https://github.com/lafvintech/UPS-Module-3S.git

   .. image:: /Tutorial/img/P7.png
   .. image:: /Tutorial/img/P8.png

   After downloading the code, you can usually enter this command to go straight into and run the power-monitoring program.

    .. code-block:: console

      cd UPS-Module-3S/Code/
      sudo python3 PowerWatch.py
   
   If you didn’t download it to this directory, you can also locate the file using the :command:`cd` and :command:`ls` commands.

   .. image:: /Tutorial/img/P9.png
   
   Among them, item **sudo python3 PowerWatch.py** is the command used to run the Python program.

   .. image:: /Tutorial/img/P10.png
   
   After running the program, it will display the battery level, power, voltage, and current.

   .. image:: /Tutorial/img/P11.png

.. note::

   1. **Current sign convention**  
      Positive values indicate the battery is **charging**; negative values indicate the battery is **discharging**.

   2. **UPS charging & protection features**  
      - **Balanced charging**: As the battery nears full capacity, the charge rate automatically slows.  
      - **Low-voltage protection**: If the battery voltage drops too low, the UPS shuts down to preserve battery health.

   3. **Accuracy disclaimer**  
      All displayed values are approximate and intended for reference only.

   4. **Runtime on battery**  
      Without an external power adapter, actual run-time depends entirely on the connected battery’s capacity and condition.