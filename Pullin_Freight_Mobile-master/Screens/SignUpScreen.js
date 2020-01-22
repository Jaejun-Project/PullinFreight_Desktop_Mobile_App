import React from 'react';
import { TextInput, Button, StyleSheet, Text, View, Alert, TouchableOpacity, Image } from 'react-native';

import Amplify, { Auth } from 'aws-amplify';
import AWSConfig from '../aws-exports';
Amplify.configure(AWSConfig);

export default class SignUpScreen extends React.Component {
  state = {
    username: '',
    password: '',
    email: '',
    confirmationCode: ''
  }

onChangeText(key, value) {
    this.setState({
        [key]: value
    })
}

createNewUser = () => {
    fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/newUser.php', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: this.state.username
    })
    }).then((response) => response.json())
        .then((responseJson) => {
            // Showing response message coming from server after inserting records.
            Alert.alert(responseJson);
        }).catch((error) => {
            console.error(error);
    });
}

signUp() {
    if (this.state.username == '' || this.state.password == '' || this.state.email == '') {
        Alert.alert('Please fill out all the fields!')
    } else {
        Auth.signUp({
            username: this.state.username,
            password: this.state.password,
            attributes: {
                email: this.state.email,
            }
            })
            .then(() => {Alert.alert('sign up successful! Please wait for the verification code')})
            .catch(err => {Alert.alert(err.message)})
    }
}

confirmSignUp() {
    Auth.confirmSignUp(this.state.username, this.state.confirmationCode)
    .then(() => Alert.alert('This account is now confirmed!'))
    .then(() => this.createNewUser())
    .catch(err => {Alert.alert(err.message)})
}

render() {
    return (
    <View style={styles.container}>
        <Image
            style={styles.logo}
            source={require('../assets/logo_white.png')}
        />
        <TextInput
            placeholderTextColor = '#eee'
            onChangeText={value => this.onChangeText('username', value)}
            autoCapitalize = 'none'
            style={styles.input}
            placeholder='username'
        />
        <TextInput
            placeholderTextColor = '#eee'
            onChangeText={value => this.onChangeText('password', value)}
            style={styles.input}
            secureTextEntry={true}
            placeholder='password'
        />
        <TextInput
            placeholderTextColor = '#eee'
            onChangeText={value => this.onChangeText('email', value)}
            autoCapitalize = 'none'
            style={styles.input}
            placeholder='email'
        />
        <TouchableOpacity 
            onPress={this.signUp.bind(this)} 
            style={styles.btn}
        >
            <Text style={styles.text}>Sign Up</Text>
        </TouchableOpacity>
        {/* <Button title="Sign Up" onPress={this.signUp.bind(this)} /> */}
        <TextInput
            placeholderTextColor = '#eee'
            onChangeText={value => this.onChangeText('confirmationCode', value)}
            style={styles.bottom_input}
            placeholder='confirmation Code'
        />
        {/* <Button title="Confirm Sign Up" onPress={this.confirmSignUp.bind(this)} /> */}
        <TouchableOpacity 
            onPress={this.confirmSignUp.bind(this)} 
            style={styles.btn}
        >
            <Text style={styles.text}>Signup Confirmation</Text>
        </TouchableOpacity>
    </View>
    );
}
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        justifyContent: 'center',
        backgroundColor: '#124E78',
        alignItems: 'center',
        paddingTop: 50,
    },
    logo: {
        height: 165,
        width: '65%',
        marginBottom: '10%'
    },
    input: {
        height: 35,
        width: '85%',
        borderBottomWidth: 1,
        borderBottomColor: '#fff',
        color: '#fff',
        margin: 10,
        fontSize: 17
    },
    bottom_input: {
        height: 40,
        width: '80%',
        borderBottomWidth: 1,
        borderBottomColor: '#fff',
        color: '#fff',
        marginTop: '10%',
        fontSize: 17
    },
    btn: {
        color: "#fff",
        marginTop: 30,
        marginBottom: 40
    },
    text: {
        color: 'white',
        fontSize: 25,
    },
});