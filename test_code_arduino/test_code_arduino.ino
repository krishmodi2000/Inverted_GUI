
void setup() 
{
  Serial.begin(9600);
}

void loop() {
  Serial.write("#3265,3253,3256,3257,3269,3222,3291,3259,3263,3265,3236,3275,3196,3375,3263,3488,3515,-5305,3515,-5305,5711,21,21,7,100\n");  //send the string "hello" and return the length of the string.

  delay(3000);

  
  Serial.write("#3345,3653,3126,3877,3659,3912,3451,3639,3223,3115,3756,3285,3936,3025,3643,3738,3165,-5125,3515,-5985,5761,21,21,15,98\n");  //send the string "hello" and return the length of the string.

  delay(3000);
}

/*
char userInput;

void setup(){

  Serial.begin(9600);                        //  setup serial

}

void loop(){

if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'D')
      {
            Serial.println("#3265,3253,3256,3257,3269,3222,3291,3259,3263,3265,3236,3275,3196,3375,3263,3488,3515,-5305,3515,-5305,5711,21,21,7,100\n");            
            
      } // if user input 'D' 
  } // Serial.available
} // Void Loop
*/
