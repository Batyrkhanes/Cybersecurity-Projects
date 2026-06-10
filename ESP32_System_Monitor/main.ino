#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include <ArduinoJson.h>

#define TFT_SCK   18
#define TFT_MOSI  21
#define TFT_CS    5
#define TFT_DC    2
#define TFT_RST   4
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCK, TFT_RST);

struct SystemData {
  int cpu;
  String ram;
  float gpu;
  String disk;
  float down;
  float up;
} sysData;

void setup() {
  Serial.begin(115200);
  delay(100);

  tft.begin();
  tft.setRotation(1);
  tft.fillScreen(ILI9341_BLACK);

  sysData = {0, "0/0GB", 0, "0/0GB", 0, 0};

  updateDisplay();
}

void drawCard(int x, int y, int w, int h, int r, const char *title, const char *value) {
  tft.fillRoundRect(x, y, w, h, r, ILI9341_DARKGREY);
  tft.drawRoundRect(x, y, w, h, r, ILI9341_WHITE);
  tft.setTextColor(ILI9341_CYAN);
  tft.setTextSize(2);
  tft.setCursor(x + 8, y + 10);
  tft.print(title);
  tft.setTextColor(ILI9341_WHITE);
  tft.setTextSize(2);
  tft.setCursor(x + 8, y + 30);
  tft.print(value);
}

void updateCardValue(int x, int y, int w, const char *value) {
  tft.fillRect(x + 4, y + 24, w - 8, 20, ILI9341_DARKGREY);
  tft.setTextColor(ILI9341_WHITE);
  tft.setTextSize(2);
  tft.setCursor(x + 8, y + 30);
  tft.print(value);
}

void updateDisplay() {
  const int h = 64;
  const int r = 14;

  char cpu_str[16], gpu_str[16], down_str[16], up_str[16];
  
  sprintf(cpu_str, "%d%%", sysData.cpu);
  sprintf(gpu_str, "%d%%", (int)sysData.gpu);
  sprintf(down_str, "%.1fMB", sysData.down);
  sprintf(up_str, "%.1fMB", sysData.up);

  // Row 1: CPU, RAM
  drawCard(10, 10, 70, h, r, "CPU", cpu_str);
  drawCard(85, 10, 235, h, r, "RAM", sysData.ram.c_str());

  // Row 2: GPU, DOWN, UP
  drawCard(10, 86, 95, h, r, "GPU", gpu_str);
  drawCard(110, 86, 125, h, r, "DOWN", down_str);
  drawCard(240, 86, 110, h, r, "UP", up_str);

  // Row 3: DISK
  drawCard(40, 162, 260, h, r, "DISK", sysData.disk.c_str());
}

void updateValuesOnly() {
  const int h = 64;

  char cpu_str[16], gpu_str[16], down_str[16], up_str[16];
  
  sprintf(cpu_str, "%d%%", sysData.cpu);
  sprintf(gpu_str, "%d%%", (int)sysData.gpu);
  sprintf(down_str, "%.1fMB", sysData.down);
  sprintf(up_str, "%.1fMB", sysData.up);

  updateCardValue(10, 10, 70, cpu_str);
  updateCardValue(85, 10, 235, sysData.ram.c_str());
  updateCardValue(10, 86, 95, gpu_str);
  updateCardValue(110, 86, 125, down_str);
  updateCardValue(240, 86, 110, up_str);
  updateCardValue(40, 162, 260, sysData.disk.c_str());
}

void loop() {
  //parcing JSON data
  static unsigned long lastUpdate = 0;
  
  if (Serial.available()) {
    String json = Serial.readStringUntil('\n');
    
    StaticJsonDocument<256> doc;
    DeserializationError error = deserializeJson(doc, json);

    if (error == DeserializationError::Ok) {
      sysData.cpu = doc["cpu"] | 0;
      sysData.ram = String((const char*)doc["ram"]);
      sysData.gpu = doc["gpu"] | 0;
      sysData.disk = String((const char*)doc["disk"]);
      sysData.down = doc["down"] | 0.0;
      sysData.up = doc["up"] | 0.0;

      if (millis() - lastUpdate >= 3000) {
        updateValuesOnly();
        lastUpdate = millis();
        Serial.println("✓");
      }
    }
  }
}
