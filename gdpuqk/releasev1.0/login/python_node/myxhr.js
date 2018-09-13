var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
navigator = {
    appName: "Netscape"
}

function myxhr(url) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
    if (xhr.readyState == 4 && xhr.status == 200) {
        return xhr.responseText;
    } else {
        return "false";
    }
}
var _path = "http://10.50.17.187:80/zftal-ui-v5-1.0.2/assets/plugins/crypto/rsa/";
eval((myxhr(_path + 'jsbn.js')));
eval((myxhr(_path + 'prng4.js')));
eval((myxhr(_path + 'rng.js')));
eval((myxhr(_path + 'rsa.js')));
eval((myxhr(_path + 'base64.js')));

Originalpassword = "88888888.";
//modulus = "AK5CIgbMnmo5FE4H9rr968LcIZCILhrr5TQvMqzZk7+6ocq0B4wyV4ZXzCNo0xYeoXlbKRhbch/+mXIPI8htuTXXqbDTqpjiRnfqmZNYBl4Sv+9y/PXgEpfu6qrAWnyBUJWJ1rP9WC/D+6dbfuEPVhrrS4vMmZjBQeIGL5bXgL21";
modulus = process.argv[2]
exponent = "AQAB";

var rsaKey = new RSAKey();
rsaKey.setPublic(b64tohex(modulus), b64tohex(exponent));
var enPassword = hex2b64(rsaKey.encrypt(Originalpassword));
console.log(enPassword);