#define RELAY_PIN 7

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH);  // Start with light OFF (relay HIGH)
  Serial.begin(9600);
  Serial.println("Arduino Ready");
  Serial.println("Initial state: Light is OFF (relay HIGH)");
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    // Log received command
    Serial.println("-------------------");
    Serial.print("Command received: ");
    Serial.println(command);

    // Execute command and log state change
    if (command == "ON") {
      digitalWrite(RELAY_PIN, LOW);   // Turn light ON (relay LOW)
      Serial.println("Action taken: Setting relay LOW");
      Serial.println("Result: Light is now ON");
    } else if (command == "OFF") {
      digitalWrite(RELAY_PIN, HIGH);  // Turn light OFF (relay HIGH)
      Serial.println("Action taken: Setting relay HIGH");
      Serial.println("Result: Light is now OFF");
    } else {
      Serial.println("Error: Unknown command");
    }
    Serial.println("-------------------");
  }
}