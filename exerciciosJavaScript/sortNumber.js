// #Your task is to make a function that can take any 
// non-negative integer as an argument and return it with its digits in descending order. Essentially, 
// rearrange the digits to create the highest possible number.


function descendingOrder(n){
    const x = n.toString().split('');
    const list = [];
    for( let i = 0; i < x.length; i++) {
      list.push(parseInt(x[i]));
    }
    let q = ''
    const y = list.sort((a, b) => b - a)
    y.forEach((b) => q += b)
    return parseInt(q)
 }


//  function descendingOrder(n){
//     return +(n + '').split('').sort(function(a,b){ return b - a }).join('');
//   }