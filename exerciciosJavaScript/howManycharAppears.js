function RunLength(str) { 
    x;
    for (let index = 0; index < str.length; index++) {
        if(!x || x != str[index]) {
            x = str[index];
        }
        
    }
    console.log(x);
    return x; 
  
  }
     
  // keep this function call here 
  console.log(RunLength("olá"));