const int photoPin = A0;
const int potPin = A1;
int photoValue;
int potValue;
void setup() {
  Serial.begin(9600);
  int threshold = 600;
}

void loop() {
  photoValue = analogRead(photoPin);
  potValue = analogRead(potPin);
  //Serial.print("Photoresistor");
  //Serial.println(photoValue);
  Serial.print("Potentiometer");
  Serial.println(potValue);
  delay(1000);
  switch(potValue){
  case 0 ... 150:
    //RED
    Serial.println("RED");
    break;
  case 151 ... 300:
    Serial.println("ORANGE");
    break;
  case 301 ... 450:
    Serial.println("YELLOW");
    break;
  case 451 ... 600:
    Serial.println("GREEN");
    break;
  case 601 ... 750:
    Serial.println("CYAN");
    break;
  case 751 ... 900:
    Serial.println("BLUE");
    break;
  case 901 ... 1024:
    Serial.println("MAGENTA");
    break;
  }
}
