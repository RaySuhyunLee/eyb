#define LED_PIN 8
#define BUTTON 6

boolean is_on = false;
boolean is_already_pressed = false;

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void changeState() {
  if (is_on) {
    Serial.println("off");
    digitalWrite(LED_PIN, LOW);
    is_on = false;
  } else {
    Serial.println("on");
    digitalWrite(LED_PIN, HIGH);
    is_on = true;
  }
}

void loop() {
  int is_pressed = !digitalRead(BUTTON);
  if (is_already_pressed && is_pressed == LOW) {
    is_already_pressed = false;
  } else if (!is_already_pressed && is_pressed == HIGH) {
    is_already_pressed = true;
    changeState();
  }
}
