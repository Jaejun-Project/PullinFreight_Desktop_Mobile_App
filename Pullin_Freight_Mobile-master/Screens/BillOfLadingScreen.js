import React from 'react';
import { View, Text, StyleSheet, Alert, Platform, TextInput, TouchableOpacity, ScrollView, DatePickerIOS, Image} from 'react-native';
import DateTimePicker from 'react-native-modal-datetime-picker';

import Amplify, { Auth } from 'aws-amplify'

let _time = new Date();
class BillOfLadingScreen extends React.Component {

static navigationOptions = {
    title: 'Bill Of Lading',
};
  
constructor(props) {
    super(props)
    this.state = {
        bill_number: '',
        chosenStartTime : this.str_process(_time),
        chosenEndTime : this.str_process(_time),
        hours_loads: 0,
        username: Auth.user.username,
        isStartDateTimePickerVisible: false,
        isEndDateTimePickerVisible: false,
        
        job_id: this.props.navigation.state.params.job.job_id,
        broker_name: this.props.navigation.state.params.job.broker_name,
        shipper_name: this.props.navigation.state.params.job.shipper_name,
        pay_type: this.props.navigation.state.params.job.pay_type,
        rate: this.props.navigation.state.params.job.rate,
        date: this.props.navigation.state.params.job.start_date,
        start_time: this.props.navigation.state.params.job.start_time,
        origin: this.props.navigation.state.params.job.origin,
        destination: this.props.navigation.state.params.job.destination,
        comments: this.props.navigation.state.params.job.comments,
    }
}

str_process = (dateTime) => {
    let hour = '';
    let min = '';

    if (dateTime.getHours() < 10) {
        hour = "0" + dateTime.getHours().toString();
    } else {
        hour = dateTime.getHours().toString();
    }

    if (dateTime.getMinutes() < 10) {
        min = "0" + dateTime.getMinutes().toString();
    } else {
        min = dateTime.getMinutes().toString();
    }
    return hour + ":" + min;
}

/* Funcion to handle start date time picker input */
_showStartDateTimePicker = () => this.setState({ isStartDateTimePickerVisible: true });

_hideStartDateTimePicker = () => this.setState({ isStartDateTimePickerVisible: false });

_handleStartDatePicked = (time) => {
    this.setState({chosenStartTime: this.str_process(time)});
    this._hideStartDateTimePicker();
};

/* Funcion to handle end date time picker input */
_showEndDateTimePicker = () => this.setState({ isEndDateTimePickerVisible: true });

_hideEndDateTimePicker = () => this.setState({ isEndDateTimePickerVisible: false });

_handleEndDatePicked = (time) => {
    this.setState({chosenEndTime: this.str_process(time)});
    this._hideEndDateTimePicker();
};


submitBillOfLading = () => {
    fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/submitBill.php', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            bill_number : this.state.bill_number,   
            start_time : this.state.chosenStartTime,
            end_time : this.state.chosenEndTime,
            hours_loads: this.state.hours_loads,
            job_id: this.state.job_id,
            broker_name: this.state.broker_name,
            shipper_name: this.state.shipper_name,
            user_name: this.state.user_name,
            pay_type: this.state.pay_type,
            rate: this.state.rate,
            date: this.state.date,
            origin: this.state.origin,
            destination: this.state.destination,
            comments: this.state.comments,
            username: this.state.username,
            broker_name: this.state.broker_name
        })
        }).then((response) => response.json())
        .then((responseJson) => {
            this.props.navigation.navigate(
                'History'
            )
        }).catch((error) => {
            console.error(error);
        });
}
  
render() {
    return (
        <View style={styles.MainContainer}>
            <Text style={{fontSize: 25, marginBottom: 15, marginBottom: 20, fontWeight: 'bold'}}> Bill of Lading Form </Text>
            <ScrollView>
                <View style={styles.container}>
                    <View style={{flex: 1, flexDirection: 'row'}}>
                        <Text style={{height: 30, paddingTop: 9, fontWeight: 'bold', fontSize: 16}}>Bill No.   </Text>
                        <TextInput
                            placeholder="Bill number"
                            onChangeText={ TextInputValue => this.setState({ bill_number : TextInputValue }) }
                            underlineColorAndroid='transparent'
                            style={styles.TextInputStyleClass}
                        />
                    </View>
                    
                    <View style={{flex: 1, flexDirection: 'row', marginVertical: 10, justifyContent: 'space-between'}}>
                        <Text>
                            <Text style={{fontWeight: 'bold', fontSize: 16}}>
                                Start Time:   
                            </Text>
                            <Text style={{fontSize: 16}}>  {this.state.chosenStartTime.toString()}</Text>
                        </Text>
                        <TouchableOpacity 
                            onPress={this._showStartDateTimePicker}
                            underlayColor={'#fff'}
                        >
                            <Image
                                style={{width: 25, height: 25, marginLeft: '10%'}}
                                source={require('../assets/calendar.png')}
                            />
                        </TouchableOpacity>
                        <DateTimePicker
                            isVisible={this.state.isStartDateTimePickerVisible}
                            onConfirm={this._handleStartDatePicked}
                            onCancel={this._hideStartDateTimePicker}
                            is24Hour={false}
                            mode={'time'}
                        />  
                    </View>
                    
                    <View style={{flex: 1, flexDirection: 'row', marginVertical: 10, justifyContent: 'space-between'}}>
                        <Text>
                            <Text style={{fontWeight: 'bold', fontSize: 16}}>
                                End Time: 
                            </Text>
                            <Text style={{fontSize: 16}}>  {this.state.chosenEndTime.toString()}</Text>
                        </Text>
                        <TouchableOpacity 
                            onPress={this._showEndDateTimePicker}
                            underlayColor={'#fff'}
                        >
                            <Image
                                style={{width: 25, height: 25, marginLeft: '10%'}}
                                source={require('../assets/calendar.png')}
                            />
                        </TouchableOpacity>
                        <DateTimePicker
                            isVisible={this.state.isEndDateTimePickerVisible}
                            onConfirm={this._handleEndDatePicked}
                            onCancel={this._hideEndDateTimePicker}
                            is24Hour={false}
                            mode={'time'}
                        />
                    </View>
                      
                    <View style={{flex: 1, flexDirection: 'row', marginVertical: 5}}>
                        <Text style={{height: 30, paddingTop: 9, fontWeight: 'bold', fontSize: 16}}>Hours/Loads    </Text>
                        <TextInput
                            keyboardType={'numeric'}
                            placeholder= "Hours or Loads"
                            onChangeText={ TextInputValue => this.setState({ hours_loads : TextInputValue }) }
                            underlineColorAndroid='transparent'
                            style={styles.TextInputStyleSmall}
                        />
                    </View>
                </View>         
            </ScrollView>
            <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityStyle} onPress={this.submitBillOfLading} >
                <Text style={styles.TextStyle}> Submit Bill of Lading </Text>
            </TouchableOpacity>
            <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityStyle} onPress={()=> this.props.navigation.goBack()} >
                <Text style={styles.TextStyle}>
                    Return to job search
                </Text>
            </TouchableOpacity>
        </View>  
    );
    }
}

const styles = StyleSheet.create({
    MainContainer :{
        flex:1,
        backgroundColor: '#fff',
        height: '100%',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: 0,
        margin: 0,
        paddingTop: 20,
        paddingBottom: 30,
    },
    container: {
        alignItems: 'flex-start',
        borderColor: '#fff',
        paddingLeft: '10%'
        // justifyContent: 'space-around',
    },
    TextInputStyleClass: {
        textAlign: 'center',
        width: '70%',
        marginBottom: 7,
        height: 33,
        borderWidth: 1,
        borderColor: 'rgb(128, 128, 128)',
        borderRadius: 5 ,
    },
    TextInputStyleSmall: {
        textAlign: 'center',
        width: '40%',
        marginBottom: 7,
        height: 33,
        borderWidth: 1,
        borderColor: 'rgb(128, 128, 128)',
        borderRadius: 5 ,
    },
    TouchableOpacityStyle: {
        paddingTop:10,
        paddingBottom:10,
        borderRadius:5,
        marginBottom:7,
        width: '80%',
        backgroundColor: '#124E78'
    },
    TextStyle:{
      color:'#fff',
      textAlign:'center',
      fontSize: 19
    },
    rowViewContainer: {
      fontSize: 20,
      paddingRight: 10,
      paddingTop: 10,
      paddingBottom: 10,
    }
});

export default BillOfLadingScreen;