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
    document.cookie = "cookie_info=accepted;";
}


$(document).ready(main);
