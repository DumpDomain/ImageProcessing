const int led=13;
int value;

void setup() 
   { 
      Serial.begin(9600); 
      pinMode(LED_BUILTIN, OUTPUT);
      digitalWrite (LED_BUILTIN, LOW);
   }
 
void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
     
     if (value == '1')
        digitalWrite (LED_BUILTIN, HIGH);
      
     
     else if (value == '0')
        digitalWrite (LED_BUILTIN, LOW);
   }
