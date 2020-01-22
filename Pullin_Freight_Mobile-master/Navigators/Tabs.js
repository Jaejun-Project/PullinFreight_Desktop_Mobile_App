import { TabNavigator, Image } from 'react-navigation';
import React from 'react';
import SignInScreen from '../Screens/SignInScreen';
import PasswordForgotScreen from '../Screens/PasswordForgotScreen';
import Ionicons from 'react-native-vector-icons/Ionicons';



const config = {
    SignIn: { screen: SignInScreen, navigationOptions: (tintColor) => ({
            tabBarLabel: 'Sign In',
            tabBarIcon: ({ focused,tintColor }) => (
                <Ionicons
                name={focused ? 'ios-person' : 'ios-person'}
                size={30}
                style={{ color: tintColor }}
                />
                )
        })
    },
    ForgotPassword: { screen: PasswordForgotScreen , navigationOptions: () => ({
            tabBarLabel: 'Forgot Password',
            tabBarIcon: ({ focused,tintColor }) => (
                <Ionicons
                name={focused ? 'ios-ios-help' : 'ios-ios-help-outline'}
                size={30}
                style={{ color: tintColor }}
                />
                )            
        })
	}
}

export default TabNavigator(config)