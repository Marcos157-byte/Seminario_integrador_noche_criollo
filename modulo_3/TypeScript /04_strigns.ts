// tipos-string.ts
const nombre1:    string = "Ana García";
const saludo:    string = `Hola, ${nombre1}`;
const vacia:     string = "";
const comillas:  string = 'También con comillas simples';

console.log(nombre);
console.log(saludo);
console.log(`La cadena vacía tiene longitud: ${vacia.length}`);

// Métodos de string funcionan igual que en JS
console.log(nombre1.toUpperCase());      // ANA GARCÍA
console.log(nombre1.toLowerCase());      // ana garcía
console.log(nombre1.includes("García")); // true
console.log(nombre1.split(" "));         // ["Ana", "García"]
