//recebe um array de numeros, verifica se o numero tem raiz quadrada
//potencializando por 2 ou fazendo a raiz quadrada

function squareOrSquareRoot(array) {
    for (let i = 0; i < array.length; i += 1) {
      let x = Math.sqrt(array[i]);
      if (Number.isInteger(x)) {
        array[i] = x;
      } else {
        array[i] *= array[i];
      }
    }
    return array;  
  }

/*usando o map
const squareOrSquareRoot = array => array.map(a => Math.sqrt(a) % 1 == 0 ? Math.sqrt(a) : (a * a));
*/