#-----------------------------------------------------------------------------------------# 
#                                                                                         #
#    This script creates a Web Design Architecture. See below to know more :              #
#                                                                                         #
#    1. Dictionary's Key is name of directory , whose value is a list of name of          #
#       files in that directory.                                                          #
#                                                                                         #
#    2. If want to create subFolders, then use dictionary in that list, following the     #
#       instruction (1).                                                                  #
#                                                                                         #
#-----------------------------------------------------------------------------------------#

#-----------------------------------# 
#                                   #
#    Author : Abhishek Soni         #
#    Format : UTF- 8                #
#    About : CREATE React Native    #
#             FOLDER STRUCTURE      #
#                                   #
#-----------------------------------#
from shutil import which
about='Create React Native Folder Structure'
print('About : ' + about)
def areDependenciesPresent():
    depencies = ['react-native' , 'node' , 'npm']
    for name in depencies:
        if which(name) is None:
            print("\nIt seems '{}' in ENV. Path is missing.\nSet it in env and rerun file in new window".format(name))
areDependenciesPresent()
print("Creating...")
import os
from datetime import datetime as dt
import shutil
import sys


# --- Creates File
def createFile(pyVer,fname):
    if pyVer[0] == "2":
        import io
        io.open(fname , "w+" , encoding="utf8")
    else:
        open(fname , "w+" , encoding="utf8")
# --- Writes into File
def writeFile(pyVer , fname , content):
    if pyVer[0] == "2":
        import io
        with io.open(fname , "a") as newFile:
            newFile.write(content)
    else:
        with open(fname , "a") as newFile:
            newFile.write(content)
# --- Create Project Structure
def create_web_proj(struct,fileData):
    global curDir , projDir
    # infos = str(struct)
    toCopy = "sass.py"
    pyVer = sys.version[0:5]
    mainDir = list(struct.keys())
    token = dt.today().strftime("%d_%m_%Y_%H_%M_%S")
    for k in mainDir:
        subDir = os.path.join(curDir,k)
        curDir = subDir
        if not os.path.exists(curDir):
            os.mkdir(curDir)
        val = struct[k]
        if type(val) != str:
            for each in val:
                if type(each) == str:
                    if "." in each:
                        dist = os.path.join(curDir , each)
                        createFile(pyVer,dist)
                        if each in list(fileData.keys()):
                            writeFile(pyVer,dist,fileData[each])
                    else:
                        subF = os.path.join(curDir , each)
                        os.mkdir(subF)
                elif type(each) == list:
                    print("Found List ---- " , each)
                elif type(each) == dict:
                    create_web_proj(each,fileData)
            if "src" not in k:
                curDir= os.path.join(curDir , "..")
        else:
            print("Other --- " ,val)
def main():
    global curDir , projDir
    # curDir = os.getcwd()
    curDir = input("Enter path to keep project :")
    if len(curDir) == 0:
        curDir = os.getcwd()
    appName = input("Enter project name :")
    appName = appName.replace(" ","")
    if len(appName) == 0 : 
        print("Project name cannot be blank.") 
        return
    os.system("react-native init " + str(appName))
    packages = " ".join([
        "react-native-gesture-handler" ,
        "react-native-image-picker" ,
        "react-native-linear-gradient",
        "react-native-vector-icons",
        "react-native-reanimated",
        "react-navigation",
        "react-navigation-drawer",
        "react-navigation-stack",
        "react-native-screens",
        "@react-native-community/async-storage",
    ])
    if which("yarn") is not None:
        os.system("cd {} && yarn add {}".format(appName,packages))
    else:
        os.system("cd {} && npm install --save {}".format(appName,packages))

    projDir = os.path.join(curDir , appName)
    os.system("cd {} && start . && start".format(appName))
    toCreate = {
    appName : [{
            "src": [
                        {
                            "components": [
                                {
                                    "commons" : [
                                        "Button.js",
                                        "ButtonGradient.js",
                                        "MyText.js",
                                        "CheckBox.js",
                                        "Input.js", 
                                        "InputGradient.js",
                                        "SearchBox.js",
                                    ]   
                                },
                                {
                                    "screens" : [
                                        "HomeScreen.js",
                                    ]
                                },
                                {
                                    "navigations" : [
                                        "AuthNav.js",
                                        "DrawerNav.js",
                                        "Header.js",
                                        "Router.js",
                                    ]
                                },
                            ]   
                        } ,
                        {
                            "globals": ["Colors.js", "Validator.js","Styles.js"]
                        } ,
                        {
                            "assets": [
                                {
                                    "images" : []
                                },
                                {
                                    "fonts": []
                                }
                            ]
                        }
                    ]
            }]
    }
    fileContents = {
    # ----    Search_Box    ----
        "SearchBox.js" : '''
            import React from "react";
            import { StyleSheet } from "react-native";
            import { Button } from "./Button";
            import InputGradient from "./InputGradient";
            import { Colors } from "../../globals/Colors";

            const styles = StyleSheet.create({
                inputParent: {
                    padding: 3,
                    borderRadius: 48,
                    marginBottom: 0,
                    marginLeft: 16,
                    flexGrow: 1,
                    height: 48
                },
                input: {
                    paddingHorizontal: 25,
                    fontSize: 16,
                    height: "100%"

                },
                inputView: {
                    borderRadius: 50,
                    height: "100%"
                },
                searchBtn: {
                    width: 46,
                    height: "100%",
                    padding: 0,
                },
                searchBtnParent: {
                    borderRadius: 50,
                    overflow: "hidden",
                },
            })

            export default class SearchBox extends React.Component {
                render() {
                    return (
                        <InputGradient
                            colors={[Colors.purple, Colors.red]}
                            parentStyle={styles.inputParent}
                            viewStyle={styles.inputView}
                            placeholder={"Search"}
                            inputStyle={styles.input}
                            componentOnRight={
                                <Button
                                    bgColor={Colors.trans}
                                    textless={true}
                                    iconName={"magnify"}
                                    iconSize={25}
                                    iconColor={Colors.red}
                                    style={styles.searchBtn}
                                    parentStyle={styles.searchBtnParent}
                                    onPress={() => console.log("Search")}
                                />
                            }
                        />
                    )
                }
            }
        '''
    # ----    BUTTON    ----
        "Button.js" : '''
            import React from 'react'
            import { TouchableHighlight, Text, View } from 'react-native'
            import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
            import { Colors } from '../../globals/Colors';
            import { Styles } from '../../globals/Styles';
            export const Button = ({ parentStyle, disabled, onPress, style, textStyle, iconName, onleft = false, iconSize = 18, iconColor = Colors.black, textless = false, bgColor = Colors.blue, color = Colors.black, text = 'Button', onlyBorder = false, ...props }) => (
                <TouchableHighlight
                    disabled={disabled}
                    onPress={onPress}
                    underlayColor={bgColor !== Colors.trans ? Colors.hexToRGB(bgColor, 0.5) : Colors.white}
                    style={parentStyle}
                >
                    <View style={[
                        {
                            backgroundColor: (!onlyBorder) ? (!disabled) ? bgColor : Colors.lightenDarken(0.35, Colors.hexToRGB(bgColor, 1)) : Colors.trans,
                            padding: 12,
                            flexDirection: "row",
                            alignItems: "center",
                            justifyContent: 'center'
                        },
                        style
                    ]}>
                        {((textless || (iconName)) && onleft) ? <Icon name={iconName} color={iconColor} size={iconSize} ></Icon> : null}
                        {!textless ?
                            <Text style={[
                                Styles.font,
                                textStyle,
                                (iconName && !onleft) ? { marginRight: 10 } : null,
                                (iconName && onleft) ? { marginLeft: 10 } : null,
                            ]}
                            >
                                {text}
                            </Text>
                            : null}
                        {((textless || iconName) && !onleft) ? <Icon name={iconName} color={iconColor} size={iconSize} ></Icon> : null}
                    </View>
                </TouchableHighlight>
            )
        ''',
    # ----    BUTTON GRADIENT    ----
        "ButtonGradient.js" : '''
            import React from 'react'
            import { TouchableHighlight, Text, View } from 'react-native'
            import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
            import LinearGradient from 'react-native-linear-gradient';
            import { Colors } from '../../globals/Colors';
            import { Styles } from '../../globals/Styles';
            export const ButtonGradient = ({ gradientStyle, disabled, viewStyle, locations, onPress, style, textStyle, iconName, angle = 90, onleft = false, iconSize = 18, iconColor = Colors.black, textless = false, colors = [Colors.blue, Colors.light_blue], color = Colors.black, text = 'Button', onlyBorder = false, ...props }) => (
                <TouchableHighlight
                    disabled={disabled}
                    onPress={onPress}
                    underlayColor={Colors.white}
                    {...props}
                    style={[
                        { overflow: "hidden", height: 64 },
                        style
                    ]}
                >
                    <LinearGradient
                        colors={!disabled ? colors : [Colors.light_grey, Colors.light_grey]}
                        style={[
                            (disabled ? { opacity: 0.6 } : null),
                            (!onlyBorder
                                ? {
                                    padding: 12,
                                    paddingHorizontal: 25,
                                    flexDirection: "row",
                                    alignItems: "center",
                                    // justifyContent: 'center',
                                    height: "100%",
                                    textAlign:"center"
                                }
                                : {
                                    padding: 2,
                                }
                            ),
                            gradientStyle
                        ]}
                        useAngle={true}
                        angle={angle}
                        locations={locations}
                    >

                        {(!onlyBorder)
                            ? (
                                <>
                                    {(
                                        ((textless || (iconName)) && onleft)
                                            ? <Icon name={iconName} color={iconColor} size={iconSize} ></Icon>
                                            : null
                                    )}
                                    {(
                                        !textless ?
                                            <Text style={[
                                                Styles.font,
                                                textStyle,
                                                (iconName && !onleft) ? { marginRight: 10 } : null,
                                                (iconName && onleft) ? { marginLeft: 10 } : null,
                                                (disabled ? { color: Colors.grey } : null),
                                            ]}
                                            >
                                                {text}
                                            </Text>
                                            : null
                                    )}
                                    {(
                                        ((textless || (iconName)) && !onleft)
                                            ? <Icon name={iconName} color={iconColor} size={iconSize} ></Icon>
                                            : null
                                    )}
                                </>
                            )
                            : (
                                <View style={[
                                    {
                                        backgroundColor: Colors.white,
                                        padding: 12,
                                        flexDirection: "row",
                                        alignItems: "center",
                                        justifyContent: 'center',
                                    },
                                    viewStyle
                                ]}>
                                    {((textless || (iconName)) && onleft) ? <Icon name={iconName} color={iconColor} size={iconSize} ></Icon> : null}
                                    {!textless ?
                                        <Text style={[
                                            Styles.font,
                                            textStyle,
                                            (iconName && !onleft) ? { marginRight: 10 } : null,
                                            (iconName && onleft) ? { marginLeft: 10 } : null,
                                            (disabled ? { color: Colors.grey } : null),
                                        ]}
                                        >
                                            {text}
                                        </Text>
                                        : null}
                                    {((textless || iconName) && !onleft) ? <Icon name={iconName} color={iconColor} size={iconSize} ></Icon> : null}

                                </View>
                            )
                        }
                    </LinearGradient>
                </TouchableHighlight >
            )
        ''',
    # ----    INPUT    ----
        "Input.js" : '''
            import React, { Component } from 'react';
            import { TextInput, View } from 'react-native';
            import { Colors } from '../../globals/Colors';
            import { Styles } from '../../globals/Styles';

            export default class Input extends React.Component {
                constructor(props) {
                    super(props);
                    this.state = {
                        value: "",
                        isActive: false
                    }
                }
                render() {
                    return (
                        <View style={[
                            { borderColor: (this.state.isActive) ? (this.props.activeColor || Colors.blue) : Colors.light_grey, overflow: "hidden" },
                            Styles.inputParent,
                            this.props.parentStyle
                        ]}>
                            <TextInput
                                style={[
                                    Styles.input,
                                    this.props.inputStyle
                                ]}
                                onChangeText={(value) => this.setState({ value })}
                                onFocus={() => this.setState({ isActive: true })}
                                onBlur={() => this.setState({ isActive: false })}
                                autoCapitalize={this.props.autoCapitalize}
                                autoFocus={this.props.autoFocus}
                                inlineImageLeft={this.props.inlineImageLeft}
                                keyboardType={this.props.keyboardType}
                                maxLength={this.props.maxLength}
                                placeholder={this.props.placeholder}
                                placeholderTextColor={Colors.grey}
                                maxLength={this.props.maxLength}
                                value={this.state.value}
                                {...this.props}
                            />
                        </View>
                    )
                }
        };''',
    # ----    INPUT GRADIENT    ----
        "InputGradient.js" : '''
            import React from 'react';
            import { TextInput, View } from 'react-native';
            import LinearGradient from 'react-native-linear-gradient';
            import { Colors } from '../../globals/Colors';
            import { Styles } from '../../globals/Styles';
            export default class InputGradient extends React.PureComponent {
                constructor(props) {
                    super(props);
                    this.state = {
                        value: "",
                        isActive: false
                    }
                }
                render() {
                    return (
                        <LinearGradient
                            colors={
                                (this.props.colors || [Colors.blue, Colors.light_blue])
                            }
                            // colors={
                            //     (this.state.isActive)
                            //         ? (this.props.colors || [Colors.blue, Colors.light_blue])
                            //         : this.props.inactiveColors || [Colors.light_grey, Colors.light_grey]
                            // }
                            style={[
                                { marginBottom: 16, paddingBottom: 2 },
                                this.props.parentStyle
                            ]}
                            useAngle={true}
                            angle={this.props.angle}
                            locations={this.props.locations}
                        >
                            <View
                                style={[
                                    (
                                        (this.props.componentOnLeft || this.props.componentOnRight)
                                            ? { position: "relative", flexDirection: "row", backgroundColor: Colors.white, overflow: "hidden" }
                                            : { overflow: "hidden" }
                                    ),
                                    this.props.viewStyle
                                ]}
                            >
                                {
                                    this.props.componentOnLeft
                                        ? (
                                            this.props.componentOnLeft
                                        )
                                        : null
                                }
                                <TextInput
                                    style={[
                                        { flexGrow: 1 },
                                        Styles.input,
                                        this.props.inputStyle
                                    ]}
                                    onChangeText={this.props.onChangeText || ((value) => this.setState({ value }))}
                                    // onFocus={() => this.setState({ isActive: true })}
                                    // onBlur={() => this.setState({ isActive: false })}
                                    onFocus={this.props.onFocus}
                                    onBlur={this.props.onBlur}
                                    autoCapitalize={this.props.autoCapitalize}
                                    autoFocus={this.props.autoFocus}
                                    inlineImageLeft={this.props.inlineImageLeft}
                                    keyboardType={this.props.keyboardType}
                                    maxLength={this.props.maxLength}
                                    placeholder={this.props.placeholder}
                                    placeholderTextColor={Colors.grey}
                                    maxLength={this.props.maxLength}
                                    {...this.props}
                                />
                                {
                                    this.props.componentOnRight
                                        ? (
                                            this.props.componentOnRight
                                        )
                                        : null
                                }
                            </View>
                        </LinearGradient>
                    )
                }
            };''',
    # ----    COLORS    ----
        "Colors.js" : '''
            export const Colors = {
                trans: 'transparent',
                purple: '#5352ed',
                pink: '#fc00ff',
                red: '#ff5252',
                yellow: '#ffb142',
                green: '#20bf6b',
                black: '#212121',
                grey: '#5e5e5e',
                white: '#fff',
                blue: '#1e90ff',

                light_purple: '#b7b2ff',
                light_pink: '#ffcccc',
                light_red: '#ff7675',
                light_yellow: '#feca57',
                light_green: '#7bed9f',
                light_grey: '#cfd8dc',
                light_blue: '#74b9ff',

                purpleOpac: function (val) {
                    return this.hexToRGB(this.purple, val);
                },
                pinkOpac: function (val) {
                    return this.hexToRGB(this.pink, val);
                },
                redOpac: function (val) {
                    return this.hexToRGB(this.red, val);
                },
                yellowOpac: function (val) {
                    return this.hexToRGB(this.yellow, val);
                },
                greenOpac: function (val) {
                    return this.hexToRGB(this.green, val);
                },
                blackOpac: function (val) {
                    return this.hexToRGB(this.black, val);
                },
                greyOpac: function (val) {
                    return this.hexToRGB(this.grey, val);
                },
                whiteOpac: function (val) {
                    return this.hexToRGB(this.white, val);
                },
                blueOpac: function (val) {
                    return this.hexToRGB(this.blue, val);
                },

                hexToRGB: function (hex, alpha) {
                    hex = hex.replace('#', '');
                    var r = parseInt(hex.length == 3 ? hex.slice(0, 1).repeat(2) : hex.slice(0, 2), 16);
                    var g = parseInt(hex.length == 3 ? hex.slice(1, 2).repeat(2) : hex.slice(2, 4), 16);
                    var b = parseInt(hex.length == 3 ? hex.slice(2, 3).repeat(2) : hex.slice(4, 6), 16);
                    if (alpha) {
                        return 'rgba(' + r + ', ' + g + ', ' + b + ', ' + alpha + ')';
                    }
                    else {
                        return 'rgb(' + r + ', ' + g + ', ' + b + ')';
                    }
                },
                lightenDarken: (p, c) => {
                    var i = parseInt, r = Math.round, [a, b, c, d] = c.split(","), P = p < 0, t = P ? 0 : 255 * p, P = P ? 1 + p : 1 - p;
                    return "rgb" + (d ? "a(" : "(") + r(i(a[3] == "a" ? a.slice(5) : a.slice(4)) * P + t) + "," + r(i(b) * P + t) + "," + r(i(c) * P + t) + (d ? "," + d : ")");
                }
        }''',
    # ----    VALIDATOR    ----
        "Validator.js" : '''
            const Validator = {
                isBlank: (val) => { return String(val).length === 0 },
                isPhone: (val) => {
                    var regex = /[0-9]{10}/g;
                    return regex.test(String(val))
                },
                isEmail: (val) => {
                    var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                    return regex.test(String(val).toLowerCase())
                },
                isChar: (val) => {
                    var regex = /[a-zA-Z ]/g;
                    return regex.test(String(val))
                },
                isNum: (val) => {
                    var regex = /[0-9]/g;
                    return regex.test(String(val))
                },
                isCharNum: (val) => {
                    var regex = /[a-zA-Z0-9 ]/g;
                    return regex.test(String(val))
                },
                isSymbol: (val) => {
                    var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                    return regex.test(String(val))
                },
                isSpecificLength: (val, len) => { return String(val).length === len; },
                isMinLength: (val, len) => { return String(val).length >= len; },
                isMaxLength: (val, len) => { return String(val).length <= len; },
            }
            export default Validator;
        ''',
        "Styles.js" : '''
            import { StyleSheet } from 'react-native';
            import { Colors } from './Colors';
            export const Styles = StyleSheet.create({
                container: {
                    padding: 20,
                    // flex: 1,
                },
                font: {
                    fontSize: 16,
                },
                input: {
                    backgroundColor: Colors.white,
                    paddingHorizontal: 16,
                    color:Colors.black
                },
                inputParent: {
                    backgroundColor: Colors.trans,
                    borderBottomWidth:1,
                    marginBottom: 10,
                }
        });''',
        "CheckBox.js":'''
            import React from 'react'
            import { TouchableHighlight, Text, View } from 'react-native'
            import Icon from 'react-native-vector-icons/MaterialCommunityIcons'
            import { MyText } from './MyText';
            import { Colors } from '../../globals/Colors';
            import { Styles } from '../../globals/Styles';


            export const CheckBox = ({ selected, onPress, style, textStyle, size = 30, color = Colors.black, activeColor = Colors.blue, text = '', ...props }) => (
                <TouchableHighlight
                    onPress={onPress}
                    underlayColor={Colors.white}

                    {...props}
                >
                    <View style={[
                        (
                            (text)
                                ? {
                                    flexDirection: 'row',
                                    alignItems: 'center',
                                }
                                : {
                                    flexDirection: 'row',
                                    alignItems: 'center',
                                    width: size,
                                    height: size,
                                }
                        ),
                        style
                    ]}
                    >
                        <Icon
                            size={size}
                            color={selected ? activeColor : color}
                            name={selected ? 'checkbox-marked-circle-outline' : 'checkbox-blank-circle-outline'}
                        />
                        {
                            text ? (
                                <MyText size={"p"} style={[{ paddingLeft: 10, flexShrink: 1 }, textStyle, (selected ? { color: activeColor } : null)]}> {text} </MyText>
                            )
                                : null
                        }
                    </View>
                </TouchableHighlight>
            );
        '''
    }
    create_web_proj(toCreate,fileContents)
if __name__=="__main__":
    main()
