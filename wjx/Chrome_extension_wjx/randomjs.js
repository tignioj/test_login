/**
 * @name 问卷星自动随机答题并且提交
 * @version v0.1
 * @author Junly
 * @description 用于问卷星自动随机选择并提交，若有验证码需要手动输入验证码
 * @Date   2018.10.6
 * @Test Environment： Chrome broswer Version 69.0.3497.92 (Official Build) (64-bit)
 * @Usage: Paste all the code into the console of Chrome broswer
 */

// 已适配题型
// 依赖关系

// 表格
//  - 单选
//  - 多选
// 单选
// 多选
// 星星
// 下拉
// 拉条 
// 填空 自动留白
// 排序
// 图片


/**
 * 
 * 
 * @param {int} min The minimum value in the range
 * @param {int} max The maxmum value in the range
 * @return {int} Return Returns a random number within this range (both include)
 */
function randint(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}


/**
 * @description 该函数用于自动选择
 */
function RandomChoose() {
    /**
     * @name 普通单选题随机选择
     * @param {object}  subject single subject
     */
    this.singleChoose = function(subject) {
        if (subject.querySelectorAll("img")[0]) { //带有图片的，无法直接click 标签<li>
            img = subject.querySelectorAll("img");
            img[randint(0, img.length - 1)].click();
        } else {
            list = subject.querySelectorAll("li");
            list[randint(0, list.length - 1)].click();

        }
    }

    /****
     * @name    普遍多选题随机选择
     * @param {object}  subject single subject
     * 
     */
    this.multiChoose = function(subject) {
        list = subject.querySelectorAll("li");
        var arr = new Array();
        for (var i = 0; i < list.length; i++) {
            if (list[i].querySelectorAll("input")[0].checked == true) {
                list[i].click();
            }
            arr.push(list[i]);
        }
        times = randint(3, arr.length - 1); // 多选题选择数量，一般不小于3
        for (var i = 0; i < times; i++) {
            randomChoose = arr.splice(randint(0, arr.length - 1), 1)[0];
            if (randomChoose.querySelectorAll("input")[0].checked == false) {
                randomChoose.click();
            }
        }
    }


    //排序题
    this.randomSort = function(list) {
        var arr = new Array();
        for (var i = 0; i < list.length; i++) {
            if (list[i].querySelectorAll("input")[0].checked == true) {
                list[i].click();
            }
            arr.push(list[i]);
        }
        times = randint(3, arr.length - 1); // 多选题选择数量，一般不小于3
        for (var i = 0; i < times; i++) {
            randomChoose = arr.splice(randint(0, arr.length - 1), 1)[0];
            if (randomChoose.querySelectorAll("input")[0].checked == false) {
                randomChoose.click();
            }
        }
    }

    //随机排序题
    this.randomSort = function(subject) {
        list = subject.querySelectorAll("li");
        var arr = new Array();
        for (var i = 0; i < list.length; i++) {
            list[i].querySelectorAll("input")[0].checked = false;
            list[i].querySelectorAll("span")[0].classList.remove("sortnum-sel"); //事实上这个只是一个样式，真正选择在于checkd = true || false
            arr.push(list[i]);
        }
        for (var i = 0; i < list.length; i++) {
            randomChoose = arr.splice(randint(0, arr.length - 1), 1)[0];
            randomChoose.querySelectorAll("input")[0].checked = true;
            randomChoose.querySelectorAll("span")[0].classList.add("sortnum-sel");
            randomChoose.querySelectorAll("span")[0].innerHTML = i + 1;
        }
    }

    //表格单选
    this.martixSingleChoose = function(subject) {
            tr = subject.querySelectorAll("tbody > tr");
            for (var i = 0; i < tr.length; i++) {
                td = tr[i].querySelectorAll("td");
                td[randint(0, td.length - 1)].click();
            }
        }
        //表格多选
    this.martixMultiChoose = function(subject) {
        tr = subject.querySelectorAll("tbody > tr");
        for (var i = 0; i < tr.length; i++) {
            td = tr[i].querySelectorAll("td");
            var arr = new Array();
            for (var j = 0; j < td.length; j++) {
                td[j].querySelectorAll("input")[0].checked = false;
                td[j].querySelectorAll("a")[0].classList.remove("jqChecked");
                arr.push(td[j]);
            }

            times = randint(3, arr.length - 1); // 多选题选择数量，一般不小于3
            for (var k = 0; k < times; k++) {
                randomChoose = arr.splice(randint(0, arr.length - 1), 1)[0];
                randomChoose.querySelectorAll("input")[0].checked = true;
                randomChoose.querySelectorAll("a")[0].classList.add("jqChecked");
            }
            console.log(times);
        }
    }
    this.martixStar = function(subject) {
        tr = subject.querySelectorAll("tbody > tr");
        for (var i = 0; i < tr.length; i++) {
            list = tr[i].querySelectorAll("li");
            var rnnum = randint(0, list.length - 1);
            list[rnnum].click();
            console.log(i, rnnum);
        }
    }

    this.dropdownSelect = function(subject) {
        select = subject.querySelectorAll("select")[0];
        var rnnum = randint(1, select.length - 1);
        select.selectedIndex = rnnum;
    }

    this.singleSlider = function(subject) {

        /**
         * 
         * @param {int} _value 随机值
         * @param {*} min 可选的最小值
         * @param {*} max 可选的最大值
         * @param {*} subject 题目
         * @description 里面的_coordsX, _Number, getElCoordinate, 方法不用管，这是根据网页的方法复制下来的， 用来反模拟出clientX的值（即鼠标的值）, 因为网页上没有提供js直接修改的value，因此只能模拟鼠标时间来点击拉条，需要参数clientX。
         * 
         */
        function getClientX(_value, min, max, subject) {
            var _bar = subject.querySelectorAll(".imageBar1")[0];
            var _slider = subject.querySelectorAll(".imageSlider1")[0]

            function _coordsX(x) {
                x = _Number(x);
                x = x <= _slider.offsetLeft ? _slider.offsetLeft : x >= _slider.offsetLeft + _slider.offsetWidth - _bar.offsetWidth ? _slider.offsetLeft + _slider.offsetWidth - _bar.offsetWidth : x;
                return x;
            }

            function _Number(b) {
                return isNaN(b) ? 0 : b;
            }

            function getElCoordinate(h) {
                var e = h.offsetLeft;
                while (h = h.offsetParent) {
                    e += h.offsetLeft;
                }
                return {
                    left: e,
                };
            }

            x = (_value - min) * ((_slider.offsetWidth - _bar.offsetWidth) / (max - min));
            x = _coordsX(x);
            clientX = x + getElCoordinate(_slider).left + (_bar.offsetWidth / 2);
            return Math.round(clientX);
        }

        var max = Number(subject.querySelectorAll(".slider")[0].getAttribute("maxvalue"));
        var min = Number(subject.querySelectorAll(".slider")[0].getAttribute("minvalue"));
        //模拟鼠标点击的事件, 关键参数ClientX
        var evt = new MouseEvent("click", {
            clientX: getClientX(randint(min, max), min, max, subject),
            type: "click",
            __proto__: MouseEvent,
        });
        subject.querySelectorAll(".ruler")[0].dispatchEvent(evt);
    }
    this.singleStar = function(subject) {
        list = subject.querySelectorAll("li:not([class='notchoice'])");
        list[randint(0, list.length - 1)].click();
    }
}


/**
 * @name 智慧树题目类型判断，并随机选择
 */
function judgeType() {
    //q = $$(".div_question");
    q = document.getElementsByClassName("div_question");
    rc = new RandomChoose();
    for (var i = 0; i < q.length; i++) {
        //普通单选 or 多选
        if ((q[i].querySelectorAll(".ulradiocheck")[0]) && (q[i].querySelectorAll("input")[0])) { // 非表格单选或者多选
            input = q[i].querySelectorAll("input");
            if (input[0].type == 'radio') {
                console.log("单选题", i);
                rc.singleChoose(q[i]);
            } else if (input[0].type == 'checkbox') {
                console.log("多选题", i);
                rc.multiChoose(q[i]);
            }

            //表格
        } else if (q[i].querySelectorAll("table")[0]) {
            if (q[i].querySelectorAll("input")[0]) { // 表格题中包含有单选， 多选
                input = q[i].querySelectorAll("input");
                if (input[0].type == 'radio') {
                    console.log("表格单选", i);
                    rc.martixSingleChoose(q[i]);
                } else if (input[0].type == 'checkbox') {
                    console.log("表格多选", i);
                    rc.martixMultiChoose(q[i]);
                }
            } else if (!q[i].querySelectorAll("input")[0] && q[i].querySelectorAll("li")[0]) { // 表格中的星星题目，没有Input标签
                console.log("Martix-Star", i);
                rc.martixStar(q[i]);
            }
        } else if (q[i].querySelectorAll("textarea")[0]) {
            console.log("填空", i);
        } else if (q[i].querySelectorAll(".slider")[0]) {
            console.log("Slider-Single-line", i);
            rc.singleSlider(q[i]);
        } else if (q[i].querySelectorAll(".notchoice")[0]) {
            console.log("Star-Single-line", i);
            rc.singleStar(q[i]);
        } else if (q[i].querySelectorAll(".lisort")[0]) {
            console.log("li-Sort", i);
            rc.randomSort(q[i]);
        } else if (q[i].querySelectorAll("select")[0]) {
            console.log("Select", i);
            rc.dropdownSelect(q[i]);
        }
    }
}
judgeType();