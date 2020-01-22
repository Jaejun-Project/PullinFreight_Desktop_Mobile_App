import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity} from 'react-native';

export default class JobInProgressScreen extends React.Component {

    onPress(finishedJob) {
        this.props.navigation.navigate(
            'BillOfLading',
            {finishedJob},
        )
    }

    render() {
        const { navigation } = this.props;
        const type = this.props.navigation.state.params.acceptedJob.type;
        const date = this.props.navigation.state.params.acceptedJob.start_date;
        const start_time = navigation.state.params.acceptedJob.start_time;
        const end_time = navigation.state.params.acceptedJob.end_time;
        const destination = this.props.navigation.state.params.acceptedJob.destination;

        return (
            <View style={styles.container}>
                <Text>
                    "{JSON.stringify(type)}" on            
                    {JSON.stringify(start_time)}-{JSON.stringify(end_time)}, {JSON.stringify(date)}
                    , is in Progress</Text>
                    <TouchableOpacity onPress={()=> this.onPress(this.props.navigation.state.params.job)} >
                    <Text style={styles.text}>
                        Submit your bill of lading
                    </Text>
                </TouchableOpacity>
            </View>
        );
    }
}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        fontSize: 20,
        paddingRight: 10,
        paddingTop: 10,
        paddingBottom: 10,
    },
});