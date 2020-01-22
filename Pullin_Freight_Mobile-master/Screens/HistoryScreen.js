import React, { Component } from 'react';
import { StyleSheet, ActivityIndicator, ListView, ScrollView, Text, View, Alert, Modal, TouchableOpacity, RefreshControl, TouchableWithoutFeedback } from 'react-native';
import { AutoScaling } from 'aws-sdk/clients/all';

import Amplify, { Auth } from 'aws-amplify'

class HistoryScreen extends Component {
    navigationOptions = {
        title: 'History',
        /* No more header config here! */
    };

    constructor(props) {
        super(props);
        let ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
        this.state = {
            isLoading: true,
            dataSource: ds,
            username: Auth.user.username,

            modalVisible: false, 
            refreshing: false,
            bg_toggle: false,

            bill_id: '',
            shipper_name: '',
            broker_name: '',
            origin: '',
            destination: '',
            loads: '',
            rate_type: '',
            start_time: '',
            end_time: '',
            hours_worked: ''
        }
    }

    _onRefresh = () => {
        this.setState({refreshing: true});
        return fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getHistory.php', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username : this.state.username,
        })
        })
        .then((response) => 
            response.json())
        .then((responseJson) => {
            this.setState({
                isLoading: false,
                refreshing: false,
            })
            if (responseJson != null) {
                this.setState({
                    dataSource: this.state.dataSource.cloneWithRows(responseJson),
                });
            }
        })
        .catch((error) => {
            Alert.alert("Error: "+error);
        });
        }

    componentDidMount() {
        return fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getHistory.php', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username : this.state.username,
        })
        })
        .then((response) => 
            response.json())
        .then((responseJson) => {
            this.setState({
                isLoading: false,
            })
            if (responseJson != null) {
                this.setState({
                    dataSource: this.state.dataSource.cloneWithRows(responseJson),
                });
            }
        })
        .catch((error) => {
            Alert.alert("Error: "+error);
        });
    }

    toggleModal(visible) {
        this.setState({ 
            modalVisible: visible,
            bg_toggle: !this.state.bg_toggle,
        });
    }

    // called when the user clicks on a job
    onPress(job) {
        this.setState ({
            bill_id: job.bill_id,
            shipper_name: job.shipper_name,
            broker_name: job.broker_name,
            origin: job.origin,
            broker: job.broker_name,
            destination: job.destination,
            hours_loads: job.hours_loads,
            rate_type: job.rate_type,
            start_time: job.start_time,
            end_time: job.end_time
        });
        this.toggleModal(true);
    }

    ListViewItemSeparator = () => {
        return (
            <View
                style={{
                    height: 1,
                    backgroundColor: "#000",
                    marginBottom: 1,
                    paddingBottom: 1,
                    width: '100%',
                }}
            />
        );
    }

    render() {
        if (this.state.isLoading) {
            return (
                <View style={{flex: 1, paddingTop: 20}}>
                    <ActivityIndicator />
                </View>
            );
        }

        if (this.state.dataSource.getRowCount() != 0){
            return (
                <View style={[styles.MainContainer, this.state.bg_toggle && {backgroundColor: '#666'}]}>
                    <Text style={styles.pageTitle}>Bill History</Text>
                    <this.ListViewItemSeparator/>
                    <ListView
                        dataSource={this.state.dataSource}
                        renderSeparator={this.ListViewItemSeparator}
                        refreshControl={
                            <RefreshControl
                                refreshing={this.state.refreshing}
                                onRefresh={this._onRefresh}
                            />
                            }
                        renderRow={(rowData) => 
                            <TouchableOpacity onPress={() => this.onPress(rowData)}>
                                <View style={{width:'100%'}}>
                                    <Text 
                                        style={styles.titleText} 
                                    >
                                        Job on {rowData.date}  {rowData.origin}-{rowData.destination}
                                    </Text>
                                </View>
                                    
                            </TouchableOpacity>
                        }
                    />

                    <Modal 
                        animationType = {"slide"} 
                        transparent = {true}
                        visible = {this.state.modalVisible}
                        >
                        <TouchableWithoutFeedback onPress={() => this.toggleModal(!this.state.modalVisible)}>
                        <View style={styles.Modal_float}>
                            <ScrollView contentContainerStyle={styles.jobList}>
                                <Text style={{fontSize: 30, marginLeft: 12, marginBottom: '5%',  paddingTop: "5%", color: '#124E78'}}>Bill Detail</Text>
                                <View>
                                    <Text style={styles.TextStyle}>
                                        <Text style={{fontWeight: 'bold'}}>Shipper: </Text>
                                        <Text>  {this.state.shipper_name}</Text>
                                    </Text>
                                    <Text style={styles.TextStyle}>
                                        <Text style={{fontWeight: 'bold'}}>Broker: </Text>
                                        <Text>  {this.state.broker_name}</Text>
                                    </Text>
                                    <Text style={styles.TextStyle}>
                                        <Text style={{fontWeight: 'bold'}}>Origin:</Text>
                                        <Text>  {this.state.origin}</Text>
                                    </Text>
                                    <Text style={styles.TextStyle}>
                                        <Text style={{fontWeight: 'bold'}}>Destination:</Text>
                                        <Text>  {this.state.destination}</Text>
                                    </Text>
                                    <Text style={styles.TextStyle}>
                                        <Text style={{fontWeight: 'bold'}}>Rate Type:</Text>
                                        <Text>  {this.state.rate_type}</Text>
                                    </Text>
                                    <Text style={styles.TextStyle}>
                                        <Text style={{fontWeight: 'bold'}}>Loads/Hours:</Text>
                                        <Text>  {this.state.hours_loads}</Text>
                                    </Text>
                                    <Text style={styles.TextStyle}>
                                        <Text style={{fontWeight: 'bold'}}>Start Time:</Text>
                                        <Text>  {this.state.start_time}</Text>
                                    </Text>
                                    <Text style={styles.TextStyle}>
                                        <Text style={{fontWeight: 'bold'}}>End Time:</Text>
                                        <Text>  {this.state.end_time}</Text>
                                    </Text>
                                </View>
                            </ScrollView>
                        </View>
                    </TouchableWithoutFeedback>
                    </Modal>  
                </View>
            );
        } else {
            return (
                <View>
                    <ScrollView 
                        contentContainerStyle={styles.jobList}
                        refreshControl={
                            <RefreshControl
                                refreshing={this.state.refreshing}
                                onRefresh={this._onRefresh}
                            />
                        }
                    >
                        <Text style={{fontSize: 20, marginLeft: '5%'}}>History is empty!</Text>
                    </ScrollView>
                </View>
            );
        } 
    }
}

const styles = StyleSheet.create({
    MainContainer :{
        flex:1,
        paddingTop: 10,
        alignItems: "stretch",
        justifyContent: 'center',
        backgroundColor: '#ddd',
        margin: 0,
    },
    titleText: {
        fontSize: 20,
        paddingBottom: 5,
        paddingTop: '4%',
        textAlign: "center",
    },
    pageTitle: {
        fontSize: 27, 
        marginLeft: 12, 
        marginBottom: 3, 
        paddingBottom: 8,
        paddingTop: "2%",
        fontWeight: 'bold'
    },
    Modal_float: {
        height: '75%',
        width: '100%', 
        position: 'absolute', 
        bottom: 0,
        backgroundColor: 'rgb(245, 245, 245)',
        borderRadius: 4,
        borderTopLeftRadius: 30,
        borderTopRightRadius: 30,
    },
    jobList: {
        flex:1,
        paddingBottom: "10%",
        alignItems: 'center',
        paddingTop: '3%',
    },
    TextStyle:{
        paddingVertical: '1.5%',
        justifyContent: 'space-between',
        fontSize: 20,
        alignItems:'stretch',
    },

});

export default HistoryScreen;