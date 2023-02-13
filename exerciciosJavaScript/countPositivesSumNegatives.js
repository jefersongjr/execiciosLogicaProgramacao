//Função recebe um array, caso o array não seja nulo, devolve a contagem dos positivos e a soma dos negativos

const countPositivesSumNegatives = (input) => {
  let contador = 0;
  let somaNegativos = 0;
  let arrayFinal = [];
  if (input === null) {
    return [];
  } else {
    for (let i = 0; i < input.length; i += 1) {
      if (input[i] > 0) {
        contador += 1;
      } else {
        somaNegativos += input[i];
      }
    }
  }
  if (contador || somaNegativos !== 0) {
    arrayFinal.push(contador);
    arrayFinal.push(somaNegativos);
  }
  return arrayFinal;
};

console.log(countPositivesSumNegatives([1,0]));
