const initedEditor = function() {
    let e = new Editor()
    let element = $('.editor').get(0)
    e.render(element)
    return e
}

const __main = function() {
    initedEditor()
}

$(document).ready(function() {
    __main()
})