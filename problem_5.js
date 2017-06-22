// Absolutly not the correct way to do that

let i = 0;
let evenlyDivisible;

while (true) {
  i++;
  evenlyDivisible = true;
  for (let k = 1; k <= 20; k++) {
    if (i % k) evenlyDivisible = false;
  }

  if (evenlyDivisible) break;
}

console.log(i);
