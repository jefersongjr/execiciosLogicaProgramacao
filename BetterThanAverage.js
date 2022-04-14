function betterThanAverage(classPoints, yourPoints) {
  return yourPoints > classPoints.reduce((a, b) => a + b, 0) / classPoints.length; 
}

console.log(betterThanAverage([2,3],5));
  
//retorna se a média da sua turma foi maior que sua nota