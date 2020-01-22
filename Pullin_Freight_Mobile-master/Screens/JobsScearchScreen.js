import React, { Component } from 'react';
import { Dimensions, StyleSheet, ActivityIndicator, ListView, ScrollView, Text, View, Alert, Modal, TouchableOpacity, RefreshControl } from 'react-native';
import CardView from 'react-native-cardview';


import { AutoScaling } from 'aws-sdk/clients/all';

import Amplify, { Auth } from 'aws-amplify';

class JobsScearchScreen extends Component {
    navigationOptions = {
        title: 'Home',
        /* No more header config here! */
    };
    constructor(props) {
        super(props);
        let today_ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
        let future_ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
        this.state = {
            isLoading: true,
            today_dataSource: today_ds,
            future_dataSource: future_ds,
            modalVisible: false, 
            username: Auth.user.username,
            refreshing: false,
        }
    }

    _onRefresh = () => {
        this.setState({refreshing: true});
        fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getTodayJobs.php', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username : this.state.username,
            })
            })  
            .then((response) => response.json())
            .then((responseJson) => {
                // Alert.alert(responseJson)
                this.setState({
                    isLoading: false,
                    refreshing: false,
                    today_dataSource: this.state.today_dataSource.cloneWithRows(responseJson),
                });
            })
            .catch((error) => {
                Alert.alert("Error: "+error);
            });

        fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getFutureJobs.php', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username : this.state.username,
            })
            })  
            .then((response) => response.json())
            .then((responseJson) => {
                this.setState({
                    isLoading: false,
                    future_dataSource: this.state.future_dataSource.cloneWithRows(responseJson),
                });
            })
            .catch((error) => {
                Alert.alert("Error: "+error);
            });
      }

    componentDidMount() {
        fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getTodayJobs.php', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username : this.state.username,
            })
            })  
            .then((response) => response.json())
            .then((responseJson) => {
                this.setState({
                    isLoading: false,
                    today_dataSource: this.state.today_dataSource.cloneWithRows(responseJson),
                });
            })
            .catch((error) => {
                Alert.alert("Error: "+error);
            });

        fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getFutureJobs.php', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username : this.state.username,
            })
            })  
            .then((response) => response.json())
            .then((responseJson) => {
                this.setState({
                    isLoading: false,
                    future_dataSource: this.state.future_dataSource.cloneWithRows(responseJson),
                });
            })
            .catch((error) => {
                Alert.alert("Error: "+error);
            });
    }

    ListViewItemSeparator = () => {
        return (
            <View
                style={{
                    height: .5,
                    width: "100%",
                    backgroundColor: "#000",
                }}
            />
        );
    }


    acceptedJob(event) {
        fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/updateJobStatus.php', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            job_id: event,
            accept: true
        })
        }).then((response) => response.json())
        .then((responseJson) => {
            // Showing response message coming from server after inserting records.
            //Alert.alert(responseJson);
            this.componentDidMount();
            this.render();
        }).catch((error) => {
            console.error(error);
        });
    }

    declinedJob(event) {
        fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/updateJobStatus.php', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            job_id: event,
            accept: false
        })
        }).then((response) => response.json())
        .then((responseJson) => {
            // Showing response message coming from server after inserting records.
            //Alert.alert(responseJson);
            this.componentDidMount();
            this.render();
        }).catch((error) => {
            console.error(error);
        });
    }

    // called when the user clicks on a job
    onPress(job) {
        this.props.navigation.navigate(
            'BillOfLading',
            {job},
        )
    }

    render() {
        if (this.state.isLoading) {
            return (
                <View style={{flex: 1, paddingTop: 20}}>
                    <ActivityIndicator />
                </View>
            );
        }

        if (this.state.today_dataSource.getRowCount() != 0 || this.state.future_dataSource.getRowCount() != 0){
            return (
                <View style={styles.MainContainer}>
                    <ScrollView
                        refreshControl={
                            <RefreshControl
                            refreshing={this.state.refreshing}
                            onRefresh={this._onRefresh}
                            />
                        }>
                        <Text style={[styles.title, {paddingTop: "5%"}]}>Today</Text>
                        <ListView
                            dataSource={this.state.today_dataSource}
                            renderRow={(rowData) => 
                                <TouchableOpacity onPress={() => this.onPress(rowData)}>
                                    <View style={styles.cardContainer}>
                                        <CardView
                                            cardElevation={10}
                                            cardMaxElevation={13}
                                            cornerRadius={10}
                                            style={styles.cardStyle}
                                        >
                                            <View style={styles.jobContainer}>
                                                <Text style={styles.rowTitle} >
                                                    Job #{rowData.job_id} : {rowData.origin}
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Shipper:   
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.shipper_name}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Broker:   
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.broker_name}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        From:   
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.start_date}, {rowData.start_time}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Destination:  
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.destination}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Type:  
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.pay_type}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Comment: 
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>{  rowData.comments}</Text>
                                                </Text>
                                                { rowData.status == 'pending' ?
                                                    <View style={{flexDirection: 'row'}}>
                                                        <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityAccept} value= {rowData.job_id} onPress={() => this.acceptedJob(rowData.job_id)} >
                                                            <Text style={styles.TextStyle}> Accept</Text>
                                                        </TouchableOpacity>
                                                        <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityDecline}  value= {rowData.job_id} onPress={() => this.declinedJob(rowData.job_id)}>
                                                            <Text style={styles.TextStyle}>Decline</Text>
                                                        </TouchableOpacity>
                                                    </View> : null
                                                }
                                            </View>
                                        </CardView>
                                    </View>
                                </TouchableOpacity>
                            }
                        />                          
                        <Text style={styles.title}>Future</Text>
                        <ListView
                            dataSource={this.state.future_dataSource}
                            renderRow={(rowData) => 
                                <TouchableOpacity onPress={() => this.onPress(rowData)}>
                                    <View style={styles.cardContainer}>
                                        <CardView
                                            cardElevation={10}
                                            cardMaxElevation={13}
                                            cornerRadius={10}
                                            style={styles.cardStyle}
                                        >
                                            <View style={styles.jobContainer}>
                                                <Text style={styles.rowTitle} >
                                                    Job #{rowData.job_id} : {rowData.origin}
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Shipper:   
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.shipper_name}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        From:   
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.start_date}, {rowData.start_time}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Destination:  
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.destination}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Type:  
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>  {rowData.pay_type}</Text>
                                                </Text>
                                                <Text style={styles.line}>
                                                    <Text style={styles.rowViewTitle}>
                                                        Comment: 
                                                    </Text>
                                                    <Text style={styles.rowViewDetail}>   {rowData.comments}</Text>
                                                </Text>
                                                { rowData.status == 'pending' ?
                                                    <View style={{flexDirection: 'row'}}>
                                                        <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityAccept} value= {rowData.job_id} onPress={() => this.acceptedJob(rowData.job_id)} >
                                                            <Text style={styles.TextStyle}> Accept</Text>
                                                        </TouchableOpacity>
                                                        <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityDecline}  value= {rowData.job_id} onPress={() => this.declinedJob(rowData.job_id)}>
                                                            <Text style={styles.TextStyle}>Decline</Text>
                                                        </TouchableOpacity>
                                                    </View> : <Text style={styles.TextStyle}>rowData.status</Text>
                                                }
                                               
                                            </View>
                                        </CardView>
                                    </View>
                                </TouchableOpacity>
                            }
                        />
                    </ScrollView>
    
                </View>
            );
        } else {
            return (
                <View style={styles.MainContainer}>
                    <ScrollView 
                        contentContainerStyle={styles.jobList}
                        refreshControl={
                            <RefreshControl
                            refreshing={this.state.refreshing}
                            onRefresh={this._onRefresh}
                            />
                        }
                    >
                        <Text style={styles.nojob}>No Jobs Available!</Text>
                    </ScrollView>
                    
                </View>
            );
        }
    }
}

const styles = StyleSheet.create({
    MainContainer :{
        justifyContent: 'center',
        flex:1,
        margin: 0,
        backgroundColor: '#ddd',
    },
    rowTitle: {
        textAlign: 'center',
        fontSize: 23,
        paddingBottom: 5,
        paddingTop: 2,
        color: '#124E78',
        // fontWeight: 'bold',
    },
    title: {
        fontSize: 25, 
        marginLeft: 12, 
        marginBottom: 3, 
        paddingBottom: 8,
        fontWeight: 'bold' 
    },
    line: {
        paddingLeft: 10,
        height: 22,
    },
    rowViewTitle: {
        paddingLeft: 7,
        fontSize: 16,
        fontWeight: 'bold',
    },
    rowViewDetail: {
        fontSize: 16,
        // marginBottom: 3
    },
    Modal_float: {
        height: "50%",
        width: "100%", 
        position: 'absolute', 
        top: '50%', 
        backgroundColor: 'rgba(128, 128, 128, 0.1)'
    },
    dimBackGround: {
        backgroundColor: 'rgba(0, 0, 0, 0.6)'
    },
    listItem: {
        backgroundColor: '#222'
    },
    cardStyle:{
        backgroundColor: '#fff',
        marginBottom: 25,
        marginTop: 0,
        width: '90%',
        height: 'auto'
    },
    cardContainer: {
        flex: 1,
        alignItems: 'center',
    },
    jobContainer: {
        padding: 10,
    },
    nojob: {
        paddingTop: Dimensions.get('window').height * 0.4,
        textAlign: 'center',
        color: 'red',
        fontSize: 30,  
        marginLeft: '5%'
    },
    TextStyle:{
      color:'#fff',
      textAlign:'center',
      fontSize: 19
    },
    TouchableOpacityAccept: {
        paddingTop:10,
        paddingBottom:10,
        borderRadius:5,
        marginBottom:7,
        marginRight:5,
        width: '30%',
        backgroundColor: 'rgb(0,128,0)'
    },
    TouchableOpacityDecline: {
        paddingTop:10,
        paddingBottom:10,
        borderRadius:5,
        marginBottom:7,
        width: '30%',
        backgroundColor: 'rgb(139,0,0)'
    }
});

export default JobsScearchScreen;