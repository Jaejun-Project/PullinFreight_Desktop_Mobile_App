import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView, Dimensions, Image } from 'react-native';

import PrimaryNavigator from './Navigators/PrimaryNavigator'

console.disableYellowBox = true;

export default class App  extends React.Component {
    render() {
        return (
            <PrimaryNavigator />
        )
    }
}