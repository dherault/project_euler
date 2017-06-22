for (let a = 1; a < 1001; a++) {
  for (let b = a; b < 1001 - a; b++) {
    const c = 1000 - a - b;

    if (a * a + b * b === c * c) console.log(a, b, c, a + b + c, a * b * c);
  }
}
