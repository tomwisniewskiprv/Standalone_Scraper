/**
 * Created by Tomasz Wiśniewski on 05.01.2018.
 *
 */

function main() {
}

function hide_cookie() {
    $('#panel_cookie').hide();
    set_cookie();

}

function set_cookie() {
    var exp_date = new Date();
    exp_date.setTime(exp_date.getTime() + (31 * 24 * 60 * 60 * 1000));

    var expires = "expires="+ exp_date.toUTCString();
    document.cookie = "cookie_info=accepted;" + expires + ";";
}


$(document).ready(main);
