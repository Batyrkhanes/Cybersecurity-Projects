# Esp32 Wi-Fi Scanner
<p align="center">
  <img src="../Screenshots/logo.png" width="500">
</p>

This project is an ESP32-based Wi-Fi monitoring and analysis tool designed for basic cybersecurity research.

It monitors wireless activity in real time, visualizes graph, and detect anomalies such as packet overflow. Tje system provides key metrics including packet count, packets per second (PPS), and signal strength (RSSI).

Additionaly, it scans nearby Wi-Fi networks and displays detailed information such as MAC addresses, encryption types (WPA2, etc.), signal strength (RSSI), and a simple risk assessment (low, high). 

This project demonstrates fundamental concepts of traffic analysis, wireless monitoring, and anomaly detection.

--- 

## 📸 Device Overview

<p align="center">
  <img src="../Screenshots/Esp32-WScanner.jpeg" width="400">
  <img src="../Screenshots/Esp32_WScanner_inside.jpeg" width="400">
</p>

---

## 🧩 Components
- ESP32 board
- USB cable
- TFT display
- 4 buttons
- Jumper Wires
- Buzzer
- 4 small breadboards
- resistor 200 ohm (for display)
- Power supply (powerbank, etc.)
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
