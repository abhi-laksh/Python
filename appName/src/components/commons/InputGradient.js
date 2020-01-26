
            import React, { Component } from 'react';
            import { TextInput, View } from 'react-native';
            import LinearGradient from 'react-native-linear-gradient';
            import { Colors } from '../../globals/Colors';
            import { Styles } from '../../globals/Styles';

            export default class InputGradient extends React.Component {
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
                                (this.state.isActive)
                                    ? (this.props.colors || [Colors.blue, Colors.light_blue])
                                    : [Colors.light_grey, Colors.light_grey]
                            }
                            style={[
                                { marginBottom: 16 },
                                this.props.parentStyle
                            ]}
                            useAngle={true}
                            angle={this.props.angle}
                            locations={this.props.locations}
                        >
                            <View
                                style={[
                                    {overflow:"hidden"},
                                    this.props.viewStyle
                                ]}
                            >
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
                                    {...this.props}
                                />
                            </View>
                        </LinearGradient>
                    )
                }
        };