var log = console.log.bind(console)

var e = function(selector, parent=document) {
    return parent.querySelector(selector)
}

var es = function(selector, parent=document) {
    return parent.querySelectorAll(selector)
}

/*
 ajax 函数
*/
var ajax = function(method, path, data, responseCallback) {
    var r = new XMLHttpRequest()
    // 设置请求方法和请求地址
    r.open(method, path, true)
    // 设置发送的数据的格式为 application/json
    // 这个不是必须的
    r.setRequestHeader('Content-Type', 'application/json')
    // 注册响应函数
    log('before onreadystatechange')
    r.onreadystatechange = function() {
        log('in onreadystatechange')
        if(r.readyState === 4) {
            // r.response 存的就是服务器发过来的放在 HTTP BODY 中的数据
            log('load ajax response', r.response)
            var json = JSON.parse(r.response)
            responseCallback(json)
            log('on last onreadystatechange')
        }
    }
    log('after onreadystatechange')
    // 把数据转换为 json 格式字符串
    data = JSON.stringify(data)
    log('after data')
    // 发送请求
    r.send(data)
}
