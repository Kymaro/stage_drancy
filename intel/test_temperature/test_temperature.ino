#include <math.h>

const int B = 4275; //valeur moyenne de la thermistance
const int R0 = 100000; // R0=100k ohm

const int pinTemp = A0; //pin A0 qui reçoit la valeur du signal retour du capteur

void setup() {
  Serial.begin(9600);
}

void loop() {
  int entree = analogRead(pinTemp);
  Serial.println(entree);

  float R = 1024.0/entree -1.0;

  float temperature = 1.0/(log(R)/B+1/298.15)-273.15; // temperature sur echelle logarithmique en Kelvin ( d'ou le -273.15) voir datasheet

  Serial.print("temperature = ");
  Serial.println(temperature);

  delay(1000);
}
