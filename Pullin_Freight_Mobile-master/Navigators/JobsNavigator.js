import React from 'react';
import { View, Text, StyleSheet, Image, SafeAreaView, Animated, Easing, ScrollView } from 'react-native';
import { createStackNavigator } from 'react-navigation';

import JobsScearchScreen from '../Screens/JobsScearchScreen';
import DetailsScreen from '../Screens/DetailsScreen';
import JobInProgressScreen from '../Screens/JobInProgressScreen';
import BillOfLadingScreen from '../Screens/BillOfLadingScreen';

const JobsNavigator = createStackNavigator({
    Jobs: JobsScearchScreen,
    BillOfLading: BillOfLadingScreen,
}, {
    mode: 'modal',
    headerMode: 'none',
    cardStyle:{
    }
})

export default JobsNavigator;