const flip = (d, a) => {
    let retorno = [];
    switch (d) {
    case 'R':
      retorno = a.sort();
      break;

    case 'L':
      retorno = a.revert.sort();
      break;
  }
  return retorno;
};

console.log