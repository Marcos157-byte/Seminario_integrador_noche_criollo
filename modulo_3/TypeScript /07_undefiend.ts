// null-undefined.ts

// En JS esto no da error, en TS sí (modo estricto)
// let nombre: string = null;    // ❌ Error

// Para permitir null hay que declararlo explícitamente
let nombre2: string | null = null;   // ✅ puede ser string o null

nombre2 = "Ana";
console.log(nombre2);  // "Ana"
nombre2 = null;
console.log(nombre2);  // null

// undefined — variable declarada pero sin valor
let ciudad: string | undefined;
console.log(ciudad);  // undefined

ciudad = "Madrid";
console.log(ciudad);  // "Madrid"