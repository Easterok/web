//************************************
//                MENU                
//************************************
const menuList = document.querySelector(".menu__list");
const hideIcon = document.querySelector(".menu__hide-icon");
const menuLogined = document.querySelector(".menu__logined");

function onMenuLoginedClick(event) {
  $(".menu__logined__ddmenu").toggle("menu__hide");
}

function onHideIconClick(event) {
  if ($(hideIcon).hasClass("menu__icon-rotate")) {
    $(hideIcon).removeClass("menu__icon-rotate");
  } else {
    $(hideIcon).addClass("menu__icon-rotate");
  }
  $(menuList).toggle("menu__hide");
}


hideIcon.addEventListener('click', onHideIconClick);
menuLogined.addEventListener('click', onMenuLoginedClick);