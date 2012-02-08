function get_cards(name, callback) {
    ajax = window.XMLHttpRequest?(new XMLHttpRequest()):(new ActiveXObject("Microsoft.XMLHttp"));
    ajax.onreadystatechange=function() {
        if(ajax.readyState===4) {
            cards = eval(ajax.responseText)||[];
            eval(callback);
        }
    };
    ajax.open("GET", "./cards/"+name, true);
    ajax.send(null);
}