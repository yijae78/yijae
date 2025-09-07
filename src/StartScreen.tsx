import React from 'react';
import { StyleSheet, View, Text, TouchableOpacity, Alert } from 'react-native';

interface StartScreenProps {
  onStart?: () => void;
}

export const StartScreen: React.FC<StartScreenProps> = ({ onStart }) => {
  const handleStart = () => {
    if (onStart) {
      onStart();
    } else {
      Alert.alert('Start button pressed');
    }
  };

  return (
    <View style={styles.container} accessible accessibilityLabel="Start screen">
      <Text style={styles.title}>Study App</Text>
      <TouchableOpacity
        style={styles.button}
        onPress={handleStart}
        accessibilityLabel="Start learning"
      >
        <Text style={styles.buttonText}>Start</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#007bff',
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 4,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
  },
});

export default StartScreen;
