import React from 'react';
import { TextInput, TouchableOpacity, StyleSheet, Text, View, Alert, Image, KeyboardAvoidingView  } from 'react-native';

import { Auth } from 'aws-amplify'

export default class SignInScreen extends React.Component {
    state = {
        username: '',
        password: '',
        confirmationCode: '',
        user: {}
    }
    onChangeText(key, value) {
        this.setState({
            [key]: value
        })
    }
    signIn() {
        const { username, password } = this.state
        Auth.signIn(username, password)
        .then(user => {
            this.setState({ user })
            console.log('successful sign in!')
            this.props.screenProps.authenticate(true)
        })
        // .catch(err => console.log('error signing in!: ', err))
        .catch(err => {Alert.alert(err.message)})
    }
    render() {
        return (
            <KeyboardAvoidingView style={styles.container} behavior="padding" enabled>
                <Image
                    style={styles.logo}
                    source={require('../assets/logo_white.png')}
                />
                <Text style={styles.text}>Pullin Freight</Text>
                <TextInput
                    placeholderTextColor = '#eee'
                    autoCapitalize = 'none'
                    onChangeText={value => this.onChangeText('username', value)}
                    style={styles.input}
                    placeholder='Username'
                />
                <TextInput
                    placeholderTextColor = '#eee'
                    autoCapitalize = 'none'
                    onChangeText={value => this.onChangeText('password', value)}
                    style={styles.input}
                    secureTextEntry={true}
                    placeholder='Password'
                />
                <TouchableOpacity 
                    onPress={this.signIn.bind(this)} 
                    style={styles.btn}
                >
                    <Text style={styles.text}>Sign In</Text>
                </TouchableOpacity>
            </KeyboardAvoidingView>
        );
    }
    }

    const styles = StyleSheet.create({
        logo: {
            height: 200,
            width: '80%',
            marginBottom: '25%'
        },
        container: {
            flex: 1,
            backgroundColor: '#fff',
            justifyContent: 'center',
            backgroundColor: '#124E78',
            alignItems: 'center',
        },
        input: {
            height: 40,
            width: '85%',
            borderBottomWidth: 1,
            borderBottomColor: '#fff',
            color: '#fff',
            margin: 10,
            fontSize: 17
        },
        btn: {
            color: "#fff",
            marginTop: 30,
        },
        text: {
            color: 'white',
            fontWeight: 'bold',
            fontSize: 30,
        },
    });