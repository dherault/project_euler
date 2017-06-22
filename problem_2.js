const max = 4000000;
let a = 0;
let b = 1;
let sum = 0;

while (b < max) {
  if (!(b % 2)) sum += b;
  [a, b] = [b, a + b];
}

console.log(sum);
