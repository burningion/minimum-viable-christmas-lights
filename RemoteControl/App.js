import React, {useState, useEffect } from 'react';
import { StyleSheet, Text, View, Button, Alert } from 'react-native';

export default function App() {
  const [currentState, setCurrentState] = useState(0);

  const handlePress = e => {
    const newState = (currentState == 'ON') ? 'OFF' : 'ON'
    const data = {'state': newState}

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    }
    fetch('http://192.168.1.44:8050/state', requestOptions)
      .then(response => response.json())
      .then(res => setCurrentState(res.state))
  }

  useEffect(() => {
    fetch('http://192.168.1.44:8050/state').then(res => res.json()).then(data => {
      setCurrentState(data.state);
    })
  }, []);

  return (
    <View style={styles.container}>
      <Text>Lights are currently {currentState} </Text>
      <Button title="Toggle Lights" onPress={handlePress} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
