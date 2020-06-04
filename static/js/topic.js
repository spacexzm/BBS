const initedEditor = function () {
    let e = new Editor()
    let element = $('.editor').get(0)
    e.render(element)
    return e
}

const __main = function () {
    initedEditor()
}

$(document).ready(function () {
    __main()
})


var a = 1

function b() {
    a = 10;
    return;

    function a() {
    };
}

b()
console.log(a)


const ticket = function () {
    let query_ticket_button = document.getElementById("query_ticket")
    let ring_action = document.getElementById('tryPlayer')
    let seat_value = document.getElementById('YZ_390000K82208')
    setInterval(function () {
        // query_ticket
        query_ticket_button.click()
        if (seat_value.innerHTML != "无") {
            ring_action.click()
        }
    }, 1000)
}