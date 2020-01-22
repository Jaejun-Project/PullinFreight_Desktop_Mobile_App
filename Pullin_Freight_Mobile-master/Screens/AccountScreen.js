import React from 'react';
import { Dimensions, View, Text, StyleSheet, Alert, Platform, TextInput, TouchableOpacity, ScrollView, ActivityIndicator, KeyboardAvoidingView, Keyboard, TouchableWithoutFeedback} from 'react-native';

import Amplify, { Auth } from 'aws-amplify';
import AWSConfig from '../aws-exports';
Amplify.configure(AWSConfig);
import Modal from "react-native-modal";

class AccountScreen extends React.Component {

static navigationOptions = {
    title: 'Account',
};

_toggleModal = () =>
    this.setState({ isModalVisible: !this.state.isModalVisible });
  
_togglePasModal = () =>
    this.setState({ isPasswordVerifcaitonVisible: !this.state.isPasswordVerifcaitonVisible});
constructor(props) {
    super(props)
    this.state = {
        isLoading: true,
        isModalVisible: false,
        isPasswordVerifcaitonVisible: false,
        verifcationCode: 0,

        fname: '',
        lname: '',
        email: '',
        phone: '',
        address: '',
        number: '',
        expire: '',
        currentPassword: '',
        newPassword: '',
        confirmPassword: '',
        username: Auth.user.username,
    }
}

componentDidMount() {
    return fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/getAccount.php', {
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
            });
        })
        .catch((error) => {
            console.error(error);
        });
}

verifyEmail = () => {
    Auth.verifyCurrentUserAttribute('email')
    .then(() => {
        Alert.alert('a verification code is sent');
        console.log('a verification code is sent');
    }).catch((e) => {
        Alert.alert(JSON.stringify(e.message));
        console.log('failed with error', e);
    });
}

verifyCode = () => {
    Auth.verifyCurrentUserAttributeSubmit('email', this.state.verficationCode)
    .then(() => {
        this.setState({ isPasswordVerifcaitonVisible: !this.state.isPasswordVerifcaitonVisible });
        Alert.alert('Email verified');
    }).catch(e => {
        Alert.alert(JSON.stringify(e.message));
         console.log('failed with error', e);
    });
}

submitAccountChanges = () => {
    fetch('http://303.itpwebdev.com/~kim687/Pullin/PHP/submitAccount.php', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            fname: this.state.fname,
            lname: this.state.lname,
            email: this.state.email,
            phone: this.state.phone,
            address: this.state.address,
            number: this.state.number,
            expire: this.state.expire,
            username: this.state.username
        })
        })
        .then((response) => response.json())
        .then((responseJson) => {
            // Showing response message coming from server after inserting records.
            Alert.alert(responseJson);
        }).catch((error) => {
            console.error(error);
        });
}
  
changePassword = () => {
    if (this.state.currentPassword == '' || this.state.newPassword == '' || this.state.confirmPassword == '') {
        Alert.alert('Please fill out all the fields!')
    }else if (this.state.newPassword != this.state.confirmPassword) {
        Alert.alert('New password not match to re-entered password!')
    }else {
        Auth.currentAuthenticatedUser()
        .then(user => {
            return Auth.changePassword(user, this.state.currentPassword, this.state.newPassword);
        })
        .then(() => {
            this.setState({ isModalVisible: !this.state.isModalVisible });
            Alert.alert('Password changed successfully.');
        })
        .catch(
            err => Alert.alert(JSON.stringify(err.message)));
    }
}

render() {
    if (this.state.isLoading) {
        return (
            <View style={{flex: 1, paddingTop: 20}}>
                <ActivityIndicator />
            </View>
        );
    }
    return ( 
            <View style={styles.MainContainer}>
                <Text style={styles.title}>Account Settings</Text>
                <ScrollView contentContainerStyle={styles.container}>
                    <View style={styles.texView}>
                        <Text style={styles.textTitle}>Hello {this.state.username}</Text>
                    </View>
                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>First name   </Text>
                        <TextInput
                            defaultValue={this.state.fname}
                            onChangeText={ TextInputValue => this.setState({ fname : TextInputValue }) }
                            underlineColorAndroid='transparent'
                            style={styles.TextInputStyleClass}
                        />
                    </View>

                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>Last name</Text>
                        <TextInput
                            defaultValue={this.state.lname}
                            onChangeText={ TextInputValue => this.setState({ lname : TextInputValue }) }
                            underlineColorAndroid='transparent'
                            style={styles.TextInputStyleClass}
                        />
                    </View>
                    
                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>Email</Text>
                        <TextInput
                            keyboardType={'email-address'}
                            defaultValue={this.state.email}
                            onChangeText={ TextInputValue => this.setState({ email : TextInputValue }) }
                            underlineColorAndroid='transparent'
                            style={styles.TextInputStyleClass}
                        />
                    </View>
                    
                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>Phone</Text>
                        <TextInput
                            keyboardType={'numeric'}
                            defaultValue={this.state.phone}
                            onChangeText={ TextInputValue => this.setState({ phone : TextInputValue }) }
                            underlineColorAndroid='transparent'
                            style={styles.TextInputStyleClass}
                        />
                    </View>
                    
                    <View style={styles.textView}>
                        <Text style={styles.textTitle}>Address</Text>
                        <TextInput
                            defaultValue={this.state.address}
                            onChangeText={ TextInputValue => this.setState({ address : TextInputValue }) }
                            underlineColorAndroid='transparent'
                            style={styles.TextInputStyleClass}
                        />
                    </View>
                    </ScrollView>
                    <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityStyle} onPress={this._toggleModal} >
                        <Text style={styles.TextStyle}> Change Password</Text>
                    </TouchableOpacity>
                    <Modal isVisible={this.state.isModalVisible}>
                        <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
                            <View style={styles.popUpView}>
                                <View>
                                    <Text style={styles.whiteText}>Current Password</Text>
                                    <TextInput
                                        defaultValue={this.state.currentPassword}
                                        onChangeText={ TextInputValue => this.setState({ currentPassword : TextInputValue }) }
                                        underlineColorAndroid='transparent'
                                        style={styles.whiteInputText}
                                    />
                                </View>
                                <View>
                                    <Text style={styles.whiteText}>New Password</Text>
                                    <TextInput
                                        defaultValue={this.state.newPassword}
                                        onChangeText={ TextInputValue => this.setState({ newPassword : TextInputValue }) }
                                        underlineColorAndroid='transparent'
                                        style={styles.whiteInputText}
                                    />
                                </View>
                                <View >
                                    <Text style={styles.whiteText}>Re-Enter New Password</Text>
                                    <TextInput
                                        defaultValue={this.state.confirmPassword}
                                        onChangeText={ TextInputValue => this.setState({ confirmPassword : TextInputValue }) }
                                        underlineColorAndroid='transparent'
                                        style={styles.whiteInputText}
                                    />
                                </View>
                                 <View style= {{paddingTop: Dimensions.get('window').height * 0.25}}></View>
                                <TouchableOpacity onPress={this.changePassword}>
                                    <Text style={styles.whiteCenter}>Change Password</Text>
                                </TouchableOpacity>
                                <TouchableOpacity onPress={this._toggleModal}>
                                    <Text style={styles.whiteCenter}>Cancel</Text>
                                </TouchableOpacity>
                            </View>
                        </TouchableWithoutFeedback>
                    </Modal>
                    <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityStyle} onPress={this._togglePasModal} >
                        <Text style={styles.TextStyle}> Email Verification </Text>
                    </TouchableOpacity>
                    <Modal isVisible={this.state.isPasswordVerifcaitonVisible}>
                        <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
                            <View style={styles.popUpView}>
                                <TouchableOpacity onPress={this.verifyEmail}>
                                    <Text style={styles.whiteCenter}>Send Verification Code</Text>
                                </TouchableOpacity>
                                <View >
                                    <Text style={{ textAlign: 'center', color: 'white',fontSize: 20}}>Enter Verfication Code</Text>
                                    <TextInput
                                        keyboardType={'numeric'}
                                        defaultValue={this.state.confirmPassword}
                                        onChangeText={ TextInputValue => this.setState({ verficationCode : TextInputValue }) }
                                        underlineColorAndroid='transparent'
                                        style={styles.whiteInputText}
                                    />
                                </View>
                                <View style= {{paddingTop: Dimensions.get('window').height * 0.3}}></View>
                                <TouchableOpacity onPress={this.verifyCode}>
                                    <Text style={styles.whiteCenter}>Verify</Text>
                                </TouchableOpacity>
                                <TouchableOpacity onPress={this._togglePasModal}>
                                    <Text style={styles.whiteCenter}>Cancel</Text>
                                </TouchableOpacity>
                            </View>
                        </TouchableWithoutFeedback>
                    </Modal>
                    <TouchableOpacity activeOpacity = { .4 } style={styles.TouchableOpacityStyle} onPress={this.submitAccountChanges} >
                        <Text style={styles.TextStyle}> Submit Account Changes </Text>
                    </TouchableOpacity>
                
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
        width: Dimensions.get('window').width * 0.95,
        borderColor: '#fff',
        paddingLeft: '7%'
        // justifyContent: 'space-around',
    },
    TextInputView: {
        alignItems: 'flex-end',
        width: '100%'
    },
    TextInputStyleClass: {
        textAlign: 'center',
        width: '100%',
        marginBottom: 7,
        height: 30,
        borderWidth: 1,
        borderColor: 'rgb(128, 128, 128)',
        borderRadius: 5 ,
        marginRight: 10
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
    },
    textTitle: {
        height: 30, 
        paddingTop: 9, 
        paddingRight: 5,
        fontWeight: 'bold', 
        fontSize: 17,
        textAlign: 'center'
    },
    textDisplay: {
        height: 30,
        paddingTop: 9,
        paddingLeft: 5,
        fontWeight: 'bold',
        fontSize: 17,
        color: 'green'
    },
    popUpView: {
        paddingTop: Dimensions.get('window').height * 0.3,
        textAlign: 'center',
        color: 'white',
        fontSize: 20
    },

    whiteText: {
        color: 'white',
        fontSize: 20,
        textAlign: 'center'
    },
    whiteCenter: {
        color: 'white',
        fontSize: 20,
        textAlign: 'center',
        paddingBottom: 10,
        paddingTop: 10,
        borderRadius: 10,
        borderWidth: 1,
        borderColor: 'white',
        marginBottom: 7,
        backgroundColor: '#124E78'
    },
    whiteInputText: {
        textAlign: 'center',
        width: '100%',
        marginBottom: 7,
        height: 30,
        borderWidth: 1,
        borderColor: 'rgb(128, 128, 128)',
        borderRadius: 5 ,
        color: 'white'
    }
});

export default AccountScreen;

