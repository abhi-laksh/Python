
            const Validator = {
                isBlank: (val) => { return String(val).length === 0 },
                isPhone: (val) => { return String(val).length === 10 },
                isEmail: (val) => {
                    var regex = /^(([^<>()\[\]\.,;:\s@"]+(\.[^<>()\[\]\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                    return regex.test(String(val).toLowerCase())
                },
            }
            export default Validator;
        