#define LED_PIN 8
#define BUTTON 6

boolean is_on = false;
boolean is_already_pressed = false;
unsigned long pressedTime = 0;
#define TURN_OFF_THRESHOLD_IN_MILLIS 2000

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void turnOn() {
    Serial.println("on");
    digitalWrite(LED_PIN, HIGH);
    is_on = true;
}

void turnOff() {
    Serial.println("off");
    digitalWrite(LED_PIN, LOW);
    is_on = false;
}    

void loop() {
  int is_pressed = !digitalRead(BUTTON);
  if (is_already_pressed && is_pressed == LOW) {
    is_already_pressed = false;
    pressedTime = 0;
  } else if (!is_already_pressed && is_pressed == HIGH) {
    is_already_pressed = true;
    if (!is_on) {
      turnOn();
    } else {
      pressedTime = millis();
    }
  }
  if (is_on && is_pressed && pressedTime > 0 && millis() - pressedTime > TURN_OFF_THRESHOLD_IN_MILLIS) {
    turnOff();
  }
}
