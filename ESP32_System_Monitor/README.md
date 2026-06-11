# Esp32 System Monitor
<p align="center">
  <img src="../../Screenshots/Esp32-SMonitor.jpeg" width="500">
</p>

A real-time system monitor that collects hardware statistics from a PC (Windows/Linux) using Python, C++ and visualizes them on an ESP32-based TFT display.
It shows CPU usage, RAM usage, GPU load, disk usage, and network upload/download speed in a simple dashboard UI.


---

## 🧩 Components
- ESP32 board
- USB cable
- TFT display
- Jumper Wires
- resistor 200 ohm (for display)
- Laptop/PC
- Arduino IDE

## 🔌GPIO Pinout
- 3v3 with 200ohm → LED (TFT Display)
- GPIO 18 → SCK (TFT Display)
- GPIO 21 → SDI (TFT Display)
- GPIO 2 → DC (TFT Display)
- GPIO 4 → RESET (TFT Display)
- GPIO 5 → CS (TFT Display)
- GND → GND (TFT Display)
- 3v3 → VCC (TFT Display)

---

## 📚 Used Libraries
### Arduino Libraries (main.ino)
- [`SPI`](https://www.arduino.cc/reference/en/libraries/spi/) — used to communicate with displays, sensors, and other SPI-compatible devices.
- [`Adafruit_GFX`](https://github.com/adafruit/Adafruit-GFX-Library) — providing functions for drawing text, lines, shapes, and images on displays.
- [`Adafruit_ILI9341`](https://github.com/adafruit/Adafruit_ILI9341) — supports screen initialization, drawing operations, color management, and display configuration.
- [`ArduinoJson`](https://arduinojson.org/) — library for parsing and generating JSON data on microcontrollers.

### Python Libraries (script.py)
- [`psutil`](https://pypi.org/project/psutil/) — provides information about CPU usage, memory consumption, disk activity, network statistics, running processes, and system performance.
- [`time`](https://docs.python.org/3/library/time.html) — used for delays, timestamps, and periodic monitoring tasks.
- [`subprocess`](https://docs.python.org/3/library/subprocess.html) — allows running shell commands and capturing their output.
- [`json`](https://docs.python.org/3/library/json.html) — python standard library for encoding and decoding JSON data.
- [`pySerial`](https://pyserial.readthedocs.io/en/latest/) (`serial`) — Library for serial communication between Python and external devices such as Arduino, ESP32, and microcontrollers.

## ⚙️ How to Install

To run this project, install the required Python and Arduino libraries.

### Python Libraries (script.py)

📦 ***psutil***
```bash
pip install psutil
```

📦 ***pySerial***
```bash
pip install pyserial
```

<br>

### Arduino Libraries (main.ino)

Install the following libraries using the **Arduino IDE Library Manager**:

📦 ***Adafruit GFX Library***
```text
Tools → Manage Libraries → Search "Adafruit GFX Library"
```

📦 ***Adafruit ILI9341***
```text
Tools → Manage Libraries → Search "Adafruit ILI9341"
```

📦 ***ArduinoJson***
```text
Tools → Manage Libraries → Search "ArduinoJson"
```

## 🚀 How to Run the Project
After installing all required libraries, download **main.ino** on ESP32 and execute **script.py** on your PC/Laptop.

## ⚠️ Disclaimer
This tool is developed for educational purposes and cybersecurity research. It should only be used on networks you own or have permission to analyze.
