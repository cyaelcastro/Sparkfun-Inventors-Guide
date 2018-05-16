const int ledPin = LED_BUILTIN;
int potPin = A0;
int potValue;
void setup() {
  pinMode(ledPin,OUTPUT);
  Serial.begin(9600);  

}

void loop() {
  potValue = 2*analogRead(potPin);
  Serial.println(potValue);
  digitalWrite(ledPin,HIGH);
  delay(potValue);
  digitalWrite(ledPin,LOW);
  delay(potrValue);
  

}
