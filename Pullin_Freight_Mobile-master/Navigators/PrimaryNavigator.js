import React from 'react';
import { View, Text, StyleSheet, Image, SafeAreaView, Animated, Easing, ScrollView, TouchableHighlight } from 'react-native';
import { createStackNavigator, createDrawerNavigator, DrawerItems } from 'react-navigation';

import Amplify, { Auth } from 'aws-amplify';
import AWSConfig from '../aws-exports';
Amplify.configure(AWSConfig)

import Tabs from './Tabs';
import JobsNavigator from './JobsNavigator';
import LoginScreen from '../Screens/LoginScreen';
import LogoutScreen from '../Screens/LogoutScreen';
import AccountScreen from '../Screens/AccountScreen';
import HistoryScreen from '../Screens/HistoryScreen';
import ExpirationScreen from '../Screens/ExpirationScreen';


const SidebarComponent = (props) => ( 
    <SafeAreaView>
        <View style={styles.sideBar}>
            <Text style={styles.headerTitle}>Hello {Auth.user.username}!</Text>
        </View>
        <DrawerItems {...props} />
    </SafeAreaView>
)

const DrawerNav = createDrawerNavigator({
    Jobs: {screen: JobsNavigator},
    History: {screen: HistoryScreen},
    Account: {screen: AccountScreen},
    Expiration: {screen: ExpirationScreen},
    LogOut: {screen: LogoutScreen}
},{
    gesturesEnabled: false,
    contentComponent: SidebarComponent,
    contentOptions: {
        activeTintColor: '#124E78',
        itemsContainerStyle: {
            marginVertical: 0,
        },
        iconContainerStyle: {
            opacity: 1
        },
    },
});

const styles = StyleSheet.create({
    sideBar: {
        height: 130, 
        backgroundColor: 'white', 
        alignItems: 'center', 
        justifyContent: 'center', 
        backgroundColor: '#124E78'
    },
    menu: {
        marginLeft: 10
    },
    headerTitle: {
        color:'white',
        marginTop: 20,
        fontSize: 25
    },
});

const DrawerStack = createStackNavigator({
    DrawerNavigator: {screen: DrawerNav}
}, {
    headerMode: 'float',
    navigationOptions: ({navigation}) => ({
        gesturesEnabled: false,
        headerStyle: {backgroundColor: '#124E78'},
        title: 'Pullin\' Freight',
        headerTintColor: 'white',
        headerLeft: 
        <TouchableHighlight 
            onPress={() => {navigation.openDrawer()}}
            underlayColor={'#124E78'}
            style={styles.menu}
        >
            <Image
                onClick = {() => {
                    navigation.openDrawer()
                }}
                style={{width: 35, height: 35}}
                source={require('../assets/icon.png')}
            />
        </TouchableHighlight>
        
        })
})

const LoginNavigator = createStackNavigator(
    {
        login: LoginScreen
    },{
        mode: 'modal',
        headerMode: 'none',
    }
)

const noTransitionConfig = () => ({
    transitionSpec: {
        duration: 0,
        timing: Animated.timing,
        easing: Easing.step0
    }
})

    // Manifest of possible screens
const PrimaryNavigator = createStackNavigator({
    LoginNavigator: { screen: LoginNavigator }, // for login/signup/forgot passowrd
    DrawerNavigator: { screen: DrawerStack } // for logged in users only
}, {
    // Default config for all screens
    headerMode: 'none',
    title: 'Main',
    initialRouteName: 'LoginNavigator',
    transitionConfig: noTransitionConfig,
    navigationOptions: {
        componentWillMount() {
            this.props.navigation.setParams({ auth: false });
        }
    }
}
);

export default PrimaryNavigator;