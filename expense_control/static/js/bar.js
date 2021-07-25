const colors = ['red', 'green', 'yellow', 'blue', 'gray']
const categories = [...document.querySelectorAll('.categories')]
const totalAmount = categories.map(cat => parseFloat(cat.innerHTML)).reduce((x, y) => x+y)
console.log(totalAmount)
categories.forEach((cat, index) => {
    let x = parseFloat(cat.innerHTML) / totalAmount;
    console.log(parseFloat(x * 150));
    cat.style.width = `${x * 150}px`
    cat.style.background = `${colors[index]}`
    cat.innerHTML = `${cat.id}: ${cat.innerHTML}`   
});

console.log(categories.map(cat => cat.innerHTML))
// categories.map(cat => cat.innerHTML="")