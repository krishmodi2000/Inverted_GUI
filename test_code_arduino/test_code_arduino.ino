/*
void setup() 
{
  Serial.begin(9600);
}

void loop() {
  Serial.write(45); // send a byte with the value 45

  int bytesSent = Serial.write("3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,62.8560,-7651.0400,2400.0000,2400.0000,2400.0000,2400.0000,2400.0000,100\n");  //send the string "hello" and return the length of the string.

  delay(10000);
} 
*/

char userInput;

void setup(){

  Serial.begin(9600);                        //  setup serial

}

void loop(){

if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'D')
      {
            Serial.println("3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,3.9285,62.8560,-7651.0400,2400.0000,2400.0000,2400.0000,2400.0000,2400.0000,100\n");            
            
      } // if user input 'D' 
  } // Serial.available
} // Void Loop
