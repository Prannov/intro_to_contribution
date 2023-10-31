#include <Arduino.h>
// #include <SimpleFOC.h>

void tempSense(){
  float bitVal = analogRead(A_TEMPERATURE);
  float temp = (1000./19.)*(3.3/1023.)*bitVal-30.5263; //10bit // @25degree Celcius V=1.055 // (0,-48.6842)(1023,125)
  Serial.println(temp);

}
void setup() {
  Serial.begin(115200);
  // pinMode(A_TEMPERATURE,INPUT);
}

void loop() {

  tempSense();

  // float bitVal = analogRead(A_TEMPERATURE);
  // float temp = (1000./19.)*(3.3/1023.)*bitVal-30.5263; //10bit // @25degree Celcius V=1.055 // (0,-48.6842)(1023,125)
  // Serial.print(bitVal);
  // Serial.print("\t");
  // Serial.println(temp);

  // float temp = map(analogRead(A_TEMPERATURE),0,4095,-49,125);
  // float temp = map(analogRead(A_TEMPERATURE),0,1023,125,-49);
  // float temp = (76.32/1023.)*bitVal-48.68 ;  
  // float temp = ((float)analogRead(A_TEMPERATURE) / 1024.0 * 3300.0 - 1055.0) / 22.7 + 25.0;
  // float temp1 = (1000/19)*(3.3/255)*bitVal-30.5263;  //8bit
  // float temp22 = (1000./19.)*(3.3/4095.)*bitVal-48.6842; //10bit // @25degree Celcius V=1.4
  // float temp3 = (1000/19)*(3.3/4095)*bitVal-30.5263; //12bitB

  // Serial.print(temp1);
  // Serial.print("\t");
  // Serial.println(temp22);
  // Serial.print("\t");
  // Serial.println(temp3);


}
