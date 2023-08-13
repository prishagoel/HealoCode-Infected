import React from 'react'
import {View, Text, StyleSheet} from 'react-native';

function Home(){
    return(
        <View>
            <Text style = {{color: 'red', background: 'yellow'}}>Welcome or some shit</Text>
            <Text style = {{color: 'green', padding: 10, margin:20}}>Another useless line</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    textStyle: {
        color: 'green',
        padding: 10,
        margin:20
    }
})
export default Home