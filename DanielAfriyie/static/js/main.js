let navBar = document.querySelector('#navHome nav');
let logo = document.querySelector('#daniel');
let links = document.querySelectorAll('#navElements li a');
let home = document.querySelector('#home');
let myWork = document.querySelector('#portfolio');
let about = document.querySelector('#about');
let contact = document.querySelector('#contact');
let homeLink = document.querySelector('a[href="#home"]');
let myWorkLink = document.querySelector('a[href="#portfolio"]');
let aboutLink = document.querySelector('a[href="#about"]');
let contactLink = document.querySelector('a[href="#contact"]');


window.onscroll = function () {
    // Sticky navbar on scroll
    if (window.pageYOffset > 300) {
        navBar.classList.add("navbarFixed");
        logo.classList.add('blackColor');
        links.forEach(function (e) {
            e.classList.add('blackColor');
        });
        $('#burger div').css('background', '#242424');
    } else {
        navBar.classList.remove("navbarFixed");
        logo.classList.remove('blackColor');
        links.forEach(function (e) {
            e.classList.remove('blackColor');
        });
        $('#burger div').css('background', '#d6d6d6');
    }

    if (window.pageYOffset > home.offsetTop && window.pageYOffset < (myWork.offsetTop - 150)) {
        homeLink.classList.add('activeLink')
    }
    else {
        homeLink.classList.remove('activeLink')
    }

    // active nav link (myWork) on scroll
    if (window.pageYOffset >= myWork.offsetTop && window.pageYOffset < (about.offsetTop - 150)) {
        myWorkLink.classList.add('activeLink');
    } else {
        myWorkLink.classList.remove('activeLink')
    }

    // active nav link on (about) scroll
    if (window.pageYOffset >= (about.offsetTop - 150) && window.pageYOffset < (contact.offsetTop - 150)) {
        aboutLink.classList.add('activeLink')
    } else {
        aboutLink.classList.remove('activeLink')
    }

    // active nav link (contact) on scroll
    if (window.pageYOffset >= (contact.offsetTop - 150)) {
        contactLink.classList.add('activeLink')
    } else {
        contactLink.classList.remove('activeLink')
    }
};

