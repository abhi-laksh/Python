
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
        }