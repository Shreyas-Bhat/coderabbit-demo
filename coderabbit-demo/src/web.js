export function greet(name) {
  const container = document.getElementById("greet");
  container.innerHTML = `<strong>Hello, ${name}</strong>`;
}
