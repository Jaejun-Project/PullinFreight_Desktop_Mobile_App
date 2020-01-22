import React from 'react';
import { View, Text, StyleSheet, Image, Alert} from 'react-native';

import Amplify, { Auth } from 'aws-amplify'

import Tabs from '../Navigators/Tabs'

export default class LoginScreen extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isAuthenticated: false
        }
    }
    authenticate(isAuthenticated) {
        this.setState({ isAuthenticated })
    }

    render() {
        // if (this.state.isAuthenticated) {
        //     this.setState=({
        //         isAuthenticated : false
        //     })
        //     this.props.navigation.navigate("DrawerNavigator")
        //     return (
        //     <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        //         <Text>Hello {Auth.user.username}!</Text>
        //         <Text>{auth}</Text>
        //     </View>
        //     )
        // }
        if (this.state.isAuthenticated) {
                this.setState({
                    isAuthenticated: false
                })
                this.props.navigation.navigate("DrawerNavigator")
                console.log(this.state.isAuthenticated)
        }

        // if (this.state.isAuthenticated) {
        //     Auth.currentAuthenticatedUser()
        //     //.then(user => Alert.alert(user))
        //     .catch(err => console.log(err));

        //     let attr = Auth.user.attributes;
        //     return (
        //         <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        //             <Text>Hello {Auth.user.username}!</Text>
        //             <Text>Hello {Auth.user.password}!</Text>
        //             <Text>Hello {Auth.user.phone_number}!</Text>
        //         </View>
        //     )
        // }
        return (
            <View style={styles.container}>
            <Tabs
                screenProps={{
                    authenticate: this.authenticate.bind(this)
                }}
            />
            </View>
        );
    }
}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },
});