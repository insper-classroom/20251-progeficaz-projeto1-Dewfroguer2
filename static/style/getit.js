function getRandomColor() {
    let r = Math.floor(Math.random() * 128 + 127); // Red: 127 - 255
    let g = Math.floor(Math.random() * 128 + 127); // Green: 127 - 255
    let b = Math.floor(Math.random() * 128 + 127); // Blue: 127 - 255
  
    return `rgb(${r}, ${g}, ${b})`; // Retorna a cor em RGB
  }
  
  // Aplica cores aleatórias às notas
  document.addEventListener("DOMContentLoaded", function() {
    let notas = document.querySelectorAll(".random-bg");
    notas.forEach(nota => {
      nota.style.backgroundColor = getRandomColor();
    });
  });

  