import React, { Component } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Alert } from 'react-native';

class DetailsScreen extends Component {

    onPress(acceptedJob) {
        this.driverAcceptsJob();
        this.props.navigation.navigate(
            'JobInProgress',
            {acceptedJob},
        )
    }

    driverAcceptsJob = () =>{
        fetch('http://303.itpwebdev.com/~taixianz/pairUserJob.php', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            job_id: this.props.navigation.state.params.job.job_id,
            driver_id: 2,
        })
        }).then((response) => response.json())
            .then((responseJson) => {
                // Showing response message coming from server after inserting records.
                console.log(responseJson);
                Alert.alert(responseJson);
            }).catch((error) => {
                console.error(error);
            });
    }
  
    render() {
        const shipper_id = this.props.navigation.state.params.job.shipper_id;
        const broker_id = this.props.navigation.state.params.job.broker_id;
        const type = this.props.navigation.state.params.job.type;
        const date = this.props.navigation.state.params.job.start_date;
        const start_time = this.props.navigation.state.params.job.start_time;
        const end_time = this.props.navigation.state.params.job.end_time;
        const origin = this.props.navigation.state.params.job.origin;
        const destination = this.props.navigation.state.params.job.destination;
        const status = this.props.navigation.state.params.job.status;

        return (
            <View>
                <View >
                    <Text>Job Details</Text>
                    <Text>Shipper ID: {JSON.stringify(shipper_id)}</Text>
                    <Text>Type: {JSON.stringify(type)}</Text>
                    <Text>origin: {JSON.stringify(origin)}</Text>
                    <Text>Destination: {JSON.stringify(destination)}</Text>
                    <Text>Time: {JSON.stringify(start_time)}-{JSON.stringify(end_time)}, {JSON.stringify(date)}</Text>
                    <Text>Job Status: {JSON.stringify(status)}</Text>
                    <TouchableOpacity onPress={()=> this.props.navigation.goBack()} >
                        <Text style={styles.text}>
                            Return to job search
                        </Text>
                    </TouchableOpacity>
                    <TouchableOpacity onPress={()=> this.onPress(this.props.navigation.state.params.job)} >
                        <Text style={styles.text}>
                            Accept this this job
                        </Text>
                    </TouchableOpacity>
                </View>
            </View>
            
        );
    }
}

const styles = StyleSheet.create({
    MainContainer :{
        // Setting up View inside content in Vertically center.
        flex:1,
        margin: 10

    },
    rowViewContainer: {
        fontSize: 20,
        paddingRight: 10,
        paddingTop: 10,
        paddingBottom: 10,
    },
    text: {
        fontSize: 20,
        borderWidth: 1,
        padding: 25,
        borderColor: 'black',
        backgroundColor: '#124E78',
        alignItems: 'center',
        color: 'white'
    }
});

export default DetailsScreen;