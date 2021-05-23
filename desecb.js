// ==UserScript==
// @name         Script cifrado
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        file:///C:/Users/Vicente/Desktop/Universidad2021_1/criptografia/Tarea3/index.html
// @icon         https://www.google.com/s2/favicons?domain=google.com
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// ==/UserScript==

//const CryptoJS = require('crypto-js')
const key = document.getElementsByClassName('keypy')
const keyHex = CryptoJS.enc.Utf8.parse(document.getElementsByClassName('keypy')[0].id)
const mensaje = document.getElementsByClassName('algorithm')

console.log(mensaje)

const decoded = CryptoJS.DES.decrypt(
  // encoded,
  { ciphertext: CryptoJS.enc.Hex.parse(document.getElementsByClassName('algorithm')[0].id) },
  keyHex,
  {
    mode: CryptoJS.mode.ECB,
    padding: CryptoJS.pad.NoPadding //no se como funciona esto
  }
)

console.log(decoded.toString(CryptoJS.enc.Utf8))
console.log("Se updateo")
