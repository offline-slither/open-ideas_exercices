  var btn0 = document.getElementById('btn0');
var btn1 = document.getElementById('btn1');
var btn2 = document.getElementById('btn2');
var btn3 = document.getElementById('btn3');
var btn4 = document.getElementById('btn4');
var btn5 = document.getElementById('btn5');
var btn6 = document.getElementById('btn6');
var btn7 = document.getElementById('btn7');
var btn8 = document.getElementById('btn8');
var btn9 = document.getElementById('btn9');
var btnClr = document.getElementById('btnClr');
var btnEql = document.getElementById('btnEql');
var btnSum = document.getElementById('btnSum');
var btnSub = document.getElementById('btnSub');
var btnMul = document.getElementById('btnMul');
var btnDiv = document.getElementById('btnDiv');
var res = document.getElementById('res');
btn0.addEventListener('click', enter('0'));
btn1.addEventListener('click', enter('1'));
btn2.addEventListener('click', enter('2'));
btn3.addEventListener('click', enter('3'));
btn4.addEventListener('click', enter('4'));
btn5.addEventListener('click', enter('5'));
btn6.addEventListener('click', enter('6'));
btn7.addEventListener('click', enter('7'));
btn8.addEventListener('click', enter('8'));
btn9.addEventListener('click', enter('9'));

btnClr.addEventListener('click', enter('clear'));
btnEql.addEventListener('click', enter('enter'));
btnSum.addEventListener('click', enter('+'));
btnSub.addEventListener('click', enter('-'));
btnMul.addEventListener('click', enter('*'));
btnDiv.addEventListener('click', enter('/'));

function enter(char) {
    return function() {
        if (char === 'clear')
            return (res.value = '');
        if (char === 'enter')
            return calc();
        res.value += char;
    }
}
// binairy engine calculator
// function calc() {
//     var resVal = res.value;
//     var operator = resVal.match(/[\+\-\*\/]/);
//     var operands = resVal.split(/[\+\-\*\/]/);
//     var result;
//     switch (operator[0]) {
//         case '+':
//             result = parseInt(operands[0], 2) + parseInt(operands[1], 2);
//             break;
//         case '-':
//             result = parseInt(operands[0], 2) - parseInt(operands[1], 2);
//             break;
//         case '*':
//             result = parseInt(operands[0], 2) * parseInt(operands[1], 2);
//             break;
//         case '/':
//             result = parseInt(operands[0], 2) / parseInt(operands[1], 2);
//             break;
//     }
//     res.value = result.toString(2);
// }

function calc() {
    var resVal = res.value;
    var operator = resVal.match(/[\+\-\*\/]/);
    var operands = resVal.split(/[\+\-\*\/]/);
    var result;
    switch (operator[0]) {
        case '+':
            result =parseInt(operands[0]) + parseInt(operands[1]);
            break;
        case '-':
            result = parseInt(operands[0]) - parseInt(operands[1]);
            break;
        case '*':
            result = parseInt(operands[0]) * parseInt(operands[1]);
            break;
        case '/':
            result = parseInt(operands[0]) / parseInt(operands[1]);
            break;
    }
    res.value = result;
}