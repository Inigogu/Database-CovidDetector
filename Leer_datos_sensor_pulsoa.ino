long HR;
String dataToSend;
int miliseconds;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dataToSend.reserve(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  HR = analogRead(0);
  miliseconds=millis();
  dataToSend = "HR:";
  dataToSend+=HR;
  dataToSend+=";ML:";
  dataToSend+=miliseconds;
  Serial.println(dataToSend);
}
