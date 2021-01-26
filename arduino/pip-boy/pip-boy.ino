#include <math.h>
#include <RotaryEncoder.h>
#include <SoftwareSerial.h>

// Debounce tracking
unsigned long debounceDelay = 50;

// We refer to the buttons by their pin number, so we use more array elements than strictly necessary.
int buttonStates[14] = {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH};
unsigned long lastDebounceTimes[14] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

const int buttonPinRotary = 8;
const int buttonPinArchives = 4;
const int buttonPinClose = 5;
const int buttonPinStatus = 11;
const int buttonPinAutomaps = 12;

// For optional comms as an alternative to USB. See sendEvent() below.
SoftwareSerial raspberry(39, 13); // RX, TX

int rotaryPosition = 0;
const int rotaryDataPin = 7;
const int rotaryClockPin = 6;
RotaryEncoder encoder(rotaryDataPin, rotaryClockPin);

const int potentiometerPins[8] = {A7, A6, A5, A4, A3, A2, A1, A0};
int potentiometerSavedValues[2] = {0, 0};

void setup() {
  pinMode(buttonPinAutomaps, INPUT);
  pinMode(buttonPinStatus, INPUT);
  pinMode(buttonPinClose, INPUT);
  pinMode(buttonPinArchives, INPUT);
  pinMode(buttonPinRotary, INPUT);
  pinMode(rotaryDataPin, INPUT);
  pinMode(rotaryClockPin, INPUT);

  // Initialize pot values to avoid having them send events on startup
  potentiometerSavedValues[0] = analogRead(potentiometerPins[0]);
  potentiometerSavedValues[1] = analogRead(potentiometerPins[1]);

  // Make sure serial comms give a chance to upload a new sketch after reset
  delay(500);

  // start serial port at 9600 bps:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // Open line to the Raspberry Pi GPIO pins
  raspberry.begin(9600);
}

/**
 *
 */
void loop() {
  checkRotary();

  checkButtonPress(buttonPinRotary);
  checkButtonPress(buttonPinArchives);
  checkButtonPress(buttonPinClose);
  checkButtonPress(buttonPinStatus);
  checkButtonPress(buttonPinAutomaps);

  checkPotValue(0);
  checkPotValue(1);
}

/**
 *
 */
void checkRotary() {
  encoder.tick();
  int newPos = encoder.getPosition();

  if (newPos != rotaryPosition) {
    int diff = newPos - rotaryPosition;
    rotaryPosition = newPos;
    sendEvent("rot " + String(diff));
  }
}

/**
 *
 */
void checkButtonPress(int pin) {
  int reading = digitalRead(pin);

  if (reading == LOW) {
    if (buttonStates[pin] == HIGH) {
      if ((millis() - lastDebounceTimes[pin]) > debounceDelay) {
        sendEvent('B' + String(pin));
        buttonStates[pin] = LOW;
      }
    }
  } else {
    lastDebounceTimes[pin] = millis();
    buttonStates[pin] = HIGH;
  }
}

/**
 *
 */
void checkPotValue(int potIndex) {
  int reading = analogRead(potentiometerPins[potIndex]);

  if (abs(reading - potentiometerSavedValues[potIndex]) > 3 ) {
    potentiometerSavedValues[potIndex] = reading;
    sendEvent("pot " + String(potIndex) + " " + reading);
  }
}

/**
 *
 */
void sendEvent(String event) {
 Serial.print(event + "\n");

 // This sends the serial event on pin 13 as well. My original idea
 // was to use the Raspberry Pi GPIO pins for the serial communication, 
 // but the Pi's default serial pins are blocked by the LCD connector,
 // and I didn't feel like going digging for solutions to that.
 raspberry.println(event + "\n");
}
