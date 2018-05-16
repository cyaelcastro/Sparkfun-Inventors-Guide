const int ledPin = LED_BUILTIN;
const int photoPin = A0;
const int threshold = 600;
int photoValue;

void setup() {
  pinMode(ledPin,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  photoValue = analogRead(photoPin);
  Serial.println(photoValue);
  if (photoValue < threshold){
    digitalWrite(ledPin,HIGH);
  }else{
    digitalWrite(ledPin,LOW);
  }
  delay(1000);
}
