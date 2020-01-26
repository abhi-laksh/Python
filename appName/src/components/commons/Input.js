
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
        };