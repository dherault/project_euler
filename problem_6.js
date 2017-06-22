let squareOfSum = 0;
let sumOfSquare = 0;

for (let i = 1; i <= 100; i++) {
  squareOfSum += i;
  sumOfSquare += i * i;
}

console.log(squareOfSum * squareOfSum - sumOfSquare);
