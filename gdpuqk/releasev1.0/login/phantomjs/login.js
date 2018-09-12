var page = require('webpage').create();

url = "http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html";
//url = "http://jwsys.gdpu.edu.cn/xtgl/login_getPublicKey.html?time=" + new Date().getTime() + "&_" + new Date().getTime();
phantom.outputEncoding = "gbk";

page.onConsoleMessage = function(msg) {
    console.log(msg);
};


page.open(url, function(status) {
    var cookies = page.cookies;
    var cookieText = '';
    for (var i in cookies) {
        cookieText += cookies[i].name + '=' + cookies[i].value;
    }

    var str = page.evaluate(function(cookieText) {
        console.log(cookieText);

        function get_PublicKey() {
            $.ajaxSettings.async = false; //phantomjs 中禁用异步
            $.getJSON(_path + "/xtgl/login_getPublicKey.html?time=" + new Date().getTime(), function(data) {
                modulus = data["modulus"];
                exponent = data["exponent"];
                PublicKey = data;
            });
        }

        function return_password() {
            var rsaKey = new RSAKey();
            rsaKey.setPublic(b64tohex(modulus), b64tohex(exponent));
            enPassword = hex2b64(rsaKey.encrypt('88888888.'));
        }

        function login() {
            url = "http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html";
            csrftoken = document.getElementById("csrftoken").value;
            var xhr = new XMLHttpRequest();
            xhr.open("POST", url, false);

            enPassword = encodeURI(enPassword).replace(/\+/g, '%2B'); //由于参数带加号，因此把加号转化为base64 编码 %2B
            data = "csrftoken=" + csrftoken + "&yhm=1700502163" + "&mm=" + enPassword + "&mm=" + enPassword;

            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
            xhr.send(data);

            if (xhr.readyState == 4 && xhr.status == 200)
                console.log(xhr.responseText);

        }


        get_PublicKey();
        return_password();
        login();

        str = "{'csrftoken':'" + csrftoken + "','enPassword': '" + enPassword + "'}";
        return str;
    }, cookieText);


    phantom.exit();
});