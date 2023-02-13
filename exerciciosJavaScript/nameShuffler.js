const nameShuffler = (str) => {
  let nome = str.split(' ');
  return `${nome[1]} ${nome[0]}`;
}

console.log(nameShuffler('Jhon Lenon'))