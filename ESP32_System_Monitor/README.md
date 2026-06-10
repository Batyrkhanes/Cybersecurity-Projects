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
- GPIO 23 → SDI (TFT Display)
- GPIO 2 → DC (TFT Display)
- GPIO 4 → RESET (TFT Display)
- GPIO 5 → CS (TFT Display)
- GND → GND (TFT Display)
- 3v3 → VCC (TFT Display)
- GPIO 15 → Buzzer
- GND → Buzzer
- GND → one leg of each button (left, right, up, down, center)
- GPIO 27 → left button
- GPIO 26 → right button
- GPIO 23 → up button
- GPIO 33 → down button
- GPIO 25 → center button

## ⚠️ Disclaimer
This tool is developed for educational purposes and cybersecurity research. It should only be used on networks you own or have permission to analyze.
