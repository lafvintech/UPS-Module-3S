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
   .. code-block:: console

   $ sudo raspi-config

   .. image:: /Tutorial/img/图片1.png
   .. image:: /Tutorial/img/图片2.png
   .. image:: /Tutorial/img/图片3.png

3. Connect Hardware  
   Use a USB cable to connect the **ESP32 DEVKIT V1** board to your computer.

   .. image:: /Tutorial/img/ESP32实物连接.png

4. Select Board  
   **Tools → Board → ESP32 → DOIT ESP32 DEVKIT V1**

      .. image:: /Tutorial/img/图片4.png

5. Select Port  
   **Tools → Port → (choose the correct COM port)**  
   *If the COM port does not appear, install the CP2101 driver for Windows.*
   
      .. image:: /Tutorial/img/图片5.png

6. Upload  
   
      .. image:: /Tutorial/img/下载键.png
   Click the **Upload** button to flash the code to your board.
   
      .. image:: /Tutorial/img/图片6.png