//Dado um array, achar uma agulha no palheiro e devolver seu indice
function findNeedle(haystack) {
    const index = haystack.indexOf('needle');
    const needle = haystack.find((currentValue) => currentValue === 'needle');
    return `found the ${needle} at position ${index}`;
}

console.log(findNeedle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))