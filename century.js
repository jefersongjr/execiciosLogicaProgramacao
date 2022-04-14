//recebe um ano e diz a qual seculo ele pertence! 
const century =(year) =>  year % 100 === 0 ? (year/100) : Math.floor((year/100)+1) ;
