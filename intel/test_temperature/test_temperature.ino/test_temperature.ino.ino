#include <math.h>

const int B = 4275; //valeur moyenne de la thermistance
const int R0 = 100000; // R0=100k ohm

const int pinTemp = A0; //pin A0 qui reçoit la valeur du signal retour du capteur

const int pinLum = A1; // pin A1 pour le capteur de lumière. Le but n'est pas de définir une luminosité précise mais juste de déterminer un seuil pour lequel on peut dire que la lumière d'une pièce est allumée. Les valeurs sont à définir arbitrairement.

void setup() {
  Serial.begin(9600);
}

void loop() {
  int entree_temp = analogRead(pinTemp);
  int entree_lum = analogRead(pinLum);

  float R = 1024.0/entree_temp -1.0;

  float temperature = 1.0/(log(R)/B+1/298.15)-273.15; // temperature sur echelle logarithmique en Kelvin ( d'ou le -273.15) voir datasheet

  Serial.print("temperature = ");
  Serial.println(temperature);

  Serial.println(entree_lum);

  delay(1000);
}
