import {StatusBar} from 'expo-status-bar';
import React from 'react';
import {StyleSheet, Text, View} from 'react-native';

export default function App(){
    return(
        <View style = {StyleSheet.container}>
            <text>Welcome to Python flask And React native</text>
            <StatusBar style = "auto"></StatusBar>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: '#fff',
        flex: 1,
        alignItems: 'centre',
        justifyContent: 'centre'
    }
});