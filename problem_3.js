let n = 600851475143;
const sqrtN = Math.sqrt(n);

for (let div = 2; div <= sqrtN; div++) {
  while (!(n === div || n % div)) {
    n /= div;
  }
}

console.log(n);
