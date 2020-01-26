
            import React from 'react';
            import { TouchableHighlight, Text, View } from 'react-native';
            import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
            import { Colors } from '../../globals/Colors';
            import { Styles } from '../../globals/Styles';
            export const Button = ({ disabled, onPress, style, textStyle, iconName, onleft = false, iconSize = 18, iconColor = Colors.black, textless = false, bgColor = Colors.blue, color = Colors.black, text = 'Button', onlyBorder = false, ...props }) => (
                <TouchableHighlight
                    disabled={disabled}
                    onPress={onPress}
                    underlayColor={Colors.hexToRGB(bgColor,0.5)}
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