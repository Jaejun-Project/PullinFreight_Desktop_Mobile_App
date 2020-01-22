import React from 'react';
import { TextInput, TouchableOpacity, StyleSheet, Text, View, Alert, Image, KeyboardAvoidingView } from 'react-native';

import { Auth } from 'aws-amplify'

export default class PasswordForgotScreen extends React.Component {
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
    forgotPassword() {
        if (this.state.username == '') {
            Alert.alert('Please fill out all the fields!')
        }else {
            Auth.forgotPassword(this.state.username)
            .then(() => {Alert.alert('Please check your email for verificaiton code')})
            .catch(err => console.log(err));
        }
    }
    submitForgotPassword() {
        if (this.state.username == '' || this.state.veriCode == '' || this.state.password == '') {
            Alert.alert('Please fill out all the fields!')
        }else {
            // Collect confirmation code and new password, then
            Auth.forgotPasswordSubmit(this.state.username, this.state.veriCode, this.state.password)
                .then(() => {Alert.alert('Password changed successfully. Please try logging in')})
                .catch(err => console.log(err));
        }
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
                <TouchableOpacity 
                    onPress={this.forgotPassword.bind(this)} 
                    style={styles.btn}
                >
                <Text style={styles.text}>Forgot Password</Text>
                </TouchableOpacity>
                <TextInput
                    placeholderTextColor = '#eee'
                    onChangeText={value => this.onChangeText('username', value)}
                    autoCapitalize = 'none'
                    style={styles.input}
                    placeholder='Username'
                />
                <TextInput
                    placeholderTextColor = '#eee'
                    onChangeText={value => this.onChangeText('password', value)}
                    style={styles.input}
                    secureTextEntry={true}
                    placeholder='New Password'
                />
                <TextInput
                    placeholderTextColor = '#eee'
                    onChangeText={value => this.onChangeText('veriCode', value)}
                    style={styles.input}
                    placeholder='Confirmation Code'
                />
                <TouchableOpacity 
                    onPress={this.submitForgotPassword.bind(this)} 
                    style={styles.btn}
                >
                <Text style={styles.text}>Change Password</Text>
                </TouchableOpacity>
            </KeyboardAvoidingView>
        );
    }
    }

    const styles = StyleSheet.create({
        logo: {
            width: 150, 
            height: 100
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
            fontSize: 25,
        },
    });