import React from 'react';
import { Dimensions, View, Text, StyleSheet, Alert, Platform, TextInput, TouchableOpacity, ScrollView, ActivityIndicator, KeyboardAvoidingView} from 'react-native';

import Amplify, { Auth } from 'aws-amplify';
import Moment from 'moment';
class ExpirationScreen extends React.Component {

static navigationOptions = {
    title: 'Expiration',
};
  
constructor(props) {
    super(props)
    this.state = {
        isLoading: true,

        fname: '',
        lname: '',
        email: '',
        phone: '',
        address: '',
        number: '',
        expire: '',
        insurance: '',
        drug: '',
        dir: '',
        carb: '',
        mcp: '',
        special: '',
        username: Auth.user.username,
    }
}

componentDidMount() {
   // http://303.itpwebdev.com/~taixianz/getAccount.php
    fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getAccount.php', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username : this.state.username,
    })
    })  .then((response) => response.json())
        .then((responseJson) => {
            // Alert.alert(responseJson[0].username);
            this.setState({
                isLoading: false,
                fname: responseJson[0].first_name,
                lname: responseJson[0].last_name,
                email: responseJson[0].email,
                phone: responseJson[0].phone_number,
                address: responseJson[0].address,
                number: responseJson[0].license_number,
                expire: responseJson[0].license_expire,
                special: responseJson[0].special_expire
            });
        })
        .catch((error) => {
            console.error(error);
        });

    fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getExpiration.php', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: this.state.username,
        })
    })  .then((response) => response.json())
        .then((responseJson) => {
           // Alert.alert(responseJson);
            this.setState({
                insurance: responseJson[0].insurance,
                drug: responseJson[0].drug_test,
                dir: responseJson[0].dir,
                carb: responseJson[0].carb,
                mcp: responseJson[0].mpc,
            });
        })
        .catch((error) =>{
            console.error(error);
        });
}


render() {
    var driver_date = new Date(this.state.license_expire);
    var insurance_date = new Date(this.state.insurance);
    var drug_date = new Date(this.state.drug);
    var dir_date = new Date(this.state.dir);
    var carb_date = new Date(this.state.carb);
    var mcp_date = new Date(this.state.mcp);
    var special_date = new Date(this.state.special);
    var currentTime = new Date();
    var sixWeeks = 1000 * 60 * 60 * 24 * 45; //revised to 45 days
    var warning = <Text style={styles.textDisplay}>No Action Needed</Text>
    var driver_button, insurance_button, drug_button, dir_button, carb_button, mcp_button, special_button;
    if (driver_date - currentTime > sixWeeks) {
        driver_button = <Text style={styles.textDisplay}>{Moment(this.state.license_expire).format('MMMM Do YYYY')}</Text>
    }else {
        warning = <Text style={[styles.textWarning, {fontSize: 20}]}>Renewal Required</Text>
        driver_button = <Text style={styles.textWarning}>{Moment(this.state.license_expire).format('MMMM Do YYYY')}</Text>
    }
    if (insurance_date - currentTime > sixWeeks) {
        insurance_button = <Text style={styles.textDisplay}>{Moment(this.state.insurance).format('MMMM Do YYYY')}</Text>
    }else {
        warning = <Text style={[styles.textWarning, {fontSize: 20}]}>Renewal Required</Text>
        insurance_button = <Text style={styles.textWarning}>{Moment(this.state.insurance).format('MMMM Do YYYY')}</Text>
    }
    if (drug_date - currentTime > sixWeeks) {
        drug_button = <Text style={styles.textDisplay}>{Moment(this.state.drug).format('MMMM Do YYYY')}</Text>
    }else {
        warning = <Text style={[styles.textWarning, {fontSize: 20}]}>Renewal Required</Text>
        drug_button = <Text style={styles.textWarning}>{Moment(this.state.drug).format('MMMM Do YYYY')}</Text>
    }
    if (dir_date - currentTime > sixWeeks) {
        dir_button = <Text style={styles.textDisplay}>{Moment(this.state.dir).format('MMMM Do YYYY')}</Text>
    }else {
        warning = <Text style={[styles.textWarning, {fontSize: 20}]}>Renewal Required</Text>
        dir_button = <Text style={styles.textWarning}>{Moment(this.state.dir).format('MMMM Do YYYY')}</Text>
    }
    if (carb_date - currentTime > sixWeeks) {
        carb_button = <Text style={styles.textDisplay}>{Moment(this.state.carb).format('MMMM Do YYYY')}</Text>
    }else {
        warning = <Text style={[styles.textWarning, {fontSize: 20}]}>Renewal Required</Text>
        carb_button = <Text style={styles.textWarning}>{Moment(this.state.carb).format('MMMM Do YYYY')}</Text>
    }
    if (mcp_date - currentTime > sixWeeks) {
        mcp_button = <Text style={styles.textDisplay}>{Moment(this.state.mcp).format('MMMM Do YYYY')}</Text>
    }else {
        warning = <Text style={[styles.textWarning, {fontSize: 20}]}>Renewal Required</Text>
        mcp_button = <Text style={styles.textWarning}>{Moment(this.state.mcp).format('MMMM Do YYYY')}</Text>
    }
    if (this.state.special == '9999-12-31') {
        special_button = <Text style={styles.textDisplay}>is not applicable</Text>
    }else if (special_date - currentTime > sixWeeks) {
        special_button = <Text style={styles.textDisplay}>{Moment(this.state.special).format('MMMM Do YYYY')}</Text>
    }else {
        warning = <Text style={[styles.textWarning, {fontSize: 20}]}>Renewal Required</Text>
        special_button = <Text style={styles.textWarning}>{Moment(this.state.special).format('MMMM Do YYYY')}</Text>
    }
    if (this.state.isLoading) {
        return (
            <View style={{flex: 1, paddingTop: 20}}>
                <ActivityIndicator />
            </View>
        );
    }

    return ( 
            <View style={styles.MainContainer}>
                <Text style={styles.title}>Expiration</Text>
                <ScrollView contentContainerStyle={styles.container}>
                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>Registration</Text>
                        {special_button}
                    </View>

                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>Driver's Licence</Text>
                        {driver_button}
                    </View>

                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>Insurance</Text>
                        {insurance_button}
                    </View>

                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>Drug Test</Text>
                        {drug_button}
                    </View>

                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>DIR</Text>
                        {dir_button}
                    </View>

                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>CARB</Text>
                        {carb_button}
                    </View>

                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>MCP</Text>
                        {mcp_button}
                    </View>

                    <View style={styles.textView}>
                        {warning}
                    </View>
                </ScrollView>
        </View>  
    
    );
}
}

const styles = StyleSheet.create({
    title: {
        fontSize: 27, 
        marginLeft: 12, 
        marginBottom: 3, 
        paddingBottom: 8,
        paddingTop: "2%",
        fontWeight: 'bold'
    },
    MainContainer :{
        flex: 1,
        paddingTop: '3%',
        backgroundColor: '#eee'
    },
    container: {
        width: Dimensions.get('window').width * 0.7,
        borderColor: '#fff',
        paddingLeft: '7%'
        // justifyContent: 'space-around',
    },
    TextInputView: {
        alignItems: 'flex-end',
        width: '70%'
    },
    TextInputStyleClass: {
        textAlign: 'center',
        width: '100%',
        marginBottom: 7,
        height: 30,
        borderWidth: 1,
        borderColor: 'rgb(128, 128, 128)',
        borderRadius: 5 ,
    },
    TouchableOpacityStyle: {
        marginLeft: 'auto',
        marginRight: 'auto',
        paddingTop:10,
        paddingBottom:10,
        borderRadius:5,
        marginBottom:7,
        width: '90%',
        backgroundColor: '#124E78'
    },
    TextStyle:{
        color:'#fff',
        textAlign:'center',
    },
    rowViewContainer: {
        fontSize: 20,
        paddingRight: 10,
        paddingTop: 10,
        paddingBottom: 10,
    },
    pageTitle:{
        fontSize: 20, 
        textAlign: 'center', 
        marginBottom: 7
    },
    textView: {
        flex: 1, 
        flexDirection: 'row', 
        marginVertical: 5
    },
    textTitle: {
        height: 30, 
        paddingTop: 9, 
        paddingRight: 5,
        fontWeight: 'bold', 
        fontSize: 17,
    },
    textDisplay: {
        height: 30,
        paddingTop: 9,
        paddingLeft: 5,
        fontWeight: 'bold',
        fontSize: 17,
        color: 'green'
    },
    textWarning: {
        height: 30,
        paddingTop: 9,
        paddingLeft: 5,
        fontWeight: 'bold',
        fontSize: 17,
        color: 'red'
    }
});

export default ExpirationScreen;