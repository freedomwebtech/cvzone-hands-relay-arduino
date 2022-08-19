#include <WiFi.h>
#include <PubSubClient.h>

const byte led_gpio = 32;
const byte led1_gpio = 4;
const byte led2_gpio = 18;
const byte led3_gpio = 5;

const char* ssid = "valorant";
const char* password =  "freedomtech";
const char* mqtt_server = "mqtt.fluux.io";
const int mqtt_port = 1883;
WiFiClient espClient;
PubSubClient client(espClient);
void setup() 
{
  
 
  pinMode(led_gpio, OUTPUT);
  pinMode(led1_gpio, OUTPUT);
  pinMode(led2_gpio, OUTPUT);
  pinMode(led3_gpio, OUTPUT);
  digitalWrite(led_gpio, HIGH);
  digitalWrite(led1_gpio, HIGH);
  digitalWrite(led2_gpio, HIGH);
  digitalWrite(led3_gpio, HIGH);            
  
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.print("Connected to WiFi :");
  Serial.println(WiFi.SSID());
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(MQTTcallback);
  while (!client.connected()) 
  {
    Serial.println("Connecting to MQTT...");
    if (client.connect("ESP8266"))
    {
      Serial.println("connected");
    }
    else
    {
      Serial.print("failed with state ");
      Serial.println(client.state());
      delay(2000);
    }
  }
  client.subscribe("test2");
}
void MQTTcallback(char* topic, byte* payload, unsigned int length) 
{
  Serial.print("Message received in topic: ");
  Serial.println(topic);
  Serial.print("Message:");
  String message;
  for (int i = 0; i < length; i++) 
  {
    message = message + (char)payload[i];
  }
  Serial.print(message);
  if (message == "oneon") 
  {
    
   digitalWrite(led_gpio, LOW);   
   
  }
   if (message == "oneoff") 
  { 

   digitalWrite(led_gpio, HIGH);    
   
  }
   if (message == "twoon") 
  {
    
   digitalWrite(led1_gpio, LOW);   
   
  }
   if (message == "twooff") 
  { 

   digitalWrite(led1_gpio, HIGH);    
   
  }
   if (message == "threeon") 
  {
    
   digitalWrite(led2_gpio, LOW);   
   
  }
   if (message == "threeoff") 
  { 

   digitalWrite(led2_gpio, HIGH);    
   
  }
   if (message == "fouron") 
  {
    
   digitalWrite(led3_gpio, LOW);   
   
  }
   if (message == "fouroff") 
  { 

   digitalWrite(led3_gpio,HIGH);    
   
  }
  
  
    
    
  Serial.println();
  Serial.println("-----------------------");
}
void loop() 
{
  
  client.loop();
}
