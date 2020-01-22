import React from 'react'
import {View, Text, TouchableOpacity, StyleSheet, Alert } from 'react-native';

import { Auth } from 'aws-amplify'


export default class LogoutScreen extends React.Component {
    static navigationOptions = {
        title: 'Log out',
    };

    logout = () => {
        try{
            Auth.signOut()
                .then(data => console.log(data))
            console.log('successful sign out!'),
            this.props.navigation.navigate("LoginNavigator")
        } catch(err) {
            Alert.alert("Error occured during logging out! " + err);
        }
    }

    render() {
        console.log('props; ', this.props)
        return (
        <View style={styles.container}>
            <TouchableOpacity
                onPress={this.logout}
            >
                <Text style={{fontWeight: 'bold', fontSize: 40, color: '#124E78'}}>Sign Out</Text>
            </TouchableOpacity>
        </View>
        )
    }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  }
})