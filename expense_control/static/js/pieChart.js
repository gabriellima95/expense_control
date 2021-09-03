var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
canvas.width = 300;
canvas.height = 300;

const colors = ['red', 'green', 'yellow', 'blue', 'gray'];
const categories = [...document.querySelectorAll('.categories')];
const totalAmount = categories.map(cat => parseFloat(cat.innerHTML)).reduce((x, y) => x+y);

function drawSlice(ctx, centerX, centerY, radius, startAngle, endAngle, color) {
    ctx.fillStyle = color
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.arc(centerX, centerY, radius, startAngle, endAngle);
    ctx.closePath()
    ctx.fill()
}

let startAngle = -Math.PI / 2;

categories.forEach((cat, index) => {
    let x = parseFloat(cat.innerHTML)/ totalAmount
    cat.style.width = `${x * 300}px`
    cat.style.paddingLeft = `${x * 300}px`
    cat.style.background = `linear-gradient(to left, rgb(255, 255, 255, 0.5), ${colors[index]}`
    let endAngle = startAngle + 2 * Math.PI * x;
    drawSlice(ctx, 150, 150, 150, startAngle, endAngle, colors[index])
    startAngle = endAngle;
    cat.innerHTML = `${cat.id}: ${cat.innerHTML}`  
});