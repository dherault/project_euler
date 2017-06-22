function isPalindrome(n) {
  const s = n.toString();

  return s === s.split('').reverse().join('');
}

let max = 0;

// ...
for (i = 100; i < 1000; i++) {
  for (j = 100; j < 1000; j++) {
    if (isPalindrome(i * j) && i * j > max) max = i * j;
  }
}

console.log(max);
