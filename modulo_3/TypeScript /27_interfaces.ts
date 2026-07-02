interface Producto {
  readonly sku: string;
  nombre: string;
  precio: number;
  descripcion?: string;   // texto largo, no siempre presente
  enStock: boolean;
}

function mostrarProducto(p: Producto): void {
  const desc = p.descripcion ? ` — ${p.descripcion}` : "";
  const stock = p.enStock ? "Disponible" : "Agotado";
  console.log(`[${p.sku}] ${p.nombre} $${p.precio}${desc} (${stock})`);
}

const laptop: Producto = {
  sku: "LAP-001",
  nombre: "Laptop Pro 15",
  precio: 1299,
  descripcion: "Pantalla 4K, 16 GB RAM",
  enStock: true,
};

const mouse: Producto = {
  sku: "MOU-042",
  nombre: "Mouse Inalámbrico",
  precio: 25,
  enStock: false,
};

mostrarProducto(laptop); // [LAP-001] Laptop Pro 15 $1299 — Pantalla 4K, 16 GB RAM (Disponible)
mostrarProducto(mouse);  // [MOU-042] Mouse Inalámbrico $25 (Agotado)

interface Empleado {

  nombres: String;
  apellidos: String;
  cargos: String;
  ubicacions: String;
};
const empleado1: Empleado = {
  nombres: "Marcos Criollo",
  apellidos: "Criollo",
  cargos: "Empleado",
  ubicacions: "carolina"
};

const empleado2: Empleado = {
  nombres: "Paolo Criollo2",
  apellidos: "Criollo2",
  cargos: "Empleado2",
  ubicacions: "carolina2"
};
function  mostrarEmpleado(e: Empleado): void {
  const mos = e.nombres 
  const ape = e.cargos
   console.log(`[${e.nombres}] ${e.cargos} ${mos} (${ape})`);
}
mostrarEmpleado(empleado1);
mostrarEmpleado(empleado2);