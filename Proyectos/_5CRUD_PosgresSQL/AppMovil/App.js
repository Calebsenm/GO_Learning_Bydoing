import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, Modal, TextInput } from 'react-native';

export default function App() {
  const [data, setData] = useState([]);
  const [editing, setEditing] = useState(false);
  const [editedItem, setEditedItem] = useState({});
  const [modalVisible, setModalVisible] = useState(false);
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [email, setEmail] = useState('');

  useEffect(() => {
    fetch('http://localhost:2080/api/datos')
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error(error));
  }, []);

  const editItem = (item) => {
    setEditing(true);
    setEditedItem(item);
    setName(item.Name);
    setAge(item.Age);
    setEmail(item.Gmail);
    setModalVisible(true);
  };

  const saveItem = () => {
    const updatedData = data.map((item) => {
      if (item.Id === editedItem.Id) {
        return {
          ...item,
          Name: name,
          Age: age,
          Gmail: email,
        };
      } else {
        return item;
      }
    });
    setData(updatedData);
    setModalVisible(false);
  };

  const renderItem = ({ item }) => (
    <TouchableOpacity onPress={() => editItem(item)}>
      <View style={styles.item}>
        <Text style={styles.name}>{item.Name}</Text>
        <Text style={styles.age}>{item.Age}</Text>
        <Text style={styles.email}>{item.Gmail}</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={data}
        renderItem={renderItem}
        keyExtractor={(item) => item.Id }
        contentContainerStyle={{ paddingBottom: 20 }}
      />

      <Modal visible={modalVisible} animationType="slide">
        <View style={styles.modalContent}>
          <Text style={styles.modalTitle}>Editar contacto</Text>
          <TextInput
            style={styles.input}
            placeholder="Nombre"
            value={name}
            onChangeText={setName}
          />
          <TextInput
            style={styles.input}
            placeholder="Edad"
            value={age}
            onChangeText={setAge}
          />
          <TextInput
            style={styles.input}
            placeholder="Correo electrónico"
            value={email}
            onChangeText={setEmail}
          />
          <TouchableOpacity style={styles.button} onPress={saveItem}>
            <Text style={styles.buttonText}>Guardar</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={() => setModalVisible(false)}>
            <Text style={styles.buttonText}>Cancelar</Text>
          </TouchableOpacity>
        </View>
      </Modal>
    </View>
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 10,
  },
  item: {
    flexDirection: 'row',
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
    backgroundColor: '#e6f7ea', // add a vibrant green color
    borderRadius: 10, // add rounded corners
    marginVertical: 5, // add vertical margin
  },
  name: {
    flex: 1,
    fontWeight: 'bold',
    fontSize: 16,
    color: '#0d47a1', // add a vibrant blue color
  },
  age: {
    width: 50,
    textAlign: 'center',
    fontSize: 16,
    color: '#0d47a1', // add a vibrant blue color
  },
  email: {
    flex: 2,
    fontSize: 14,
    color: '#757575', // add a gray color
  },
});
