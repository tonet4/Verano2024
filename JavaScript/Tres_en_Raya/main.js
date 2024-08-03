const pantalla = document.querySelector(".pantalla"); // llamamos a la pantalla
const botones = document.querySelectorAll(".btn"); // llamamos a todos los botones
const resetButton = document.getElementById("reset"); // llamamos al botón de reset

const resultado1 = document.querySelector(".marca1");
const resultado2 = document.querySelector(".marca2");


// Función para generar un movimiento aleatorio de la máquina
function machineMove() {
    const availableButtons = Array.from(botones).filter(boton => boton.textContent === ""); // Filtramos los botones que no estén ocupados
    const randomIndex = Math.floor(Math.random() * availableButtons.length); // Generamos un índice aleatorio
    const randomButton = availableButtons[randomIndex]; // Seleccionamos el botón aleatorio
  
    // Actualizamos el texto del botón aleatorio con la marca de la máquina (en este caso, "X")
    randomButton.textContent = "X";
    
    randomButton.innerHTML = '<span class="x">X</span>'; // Agrega la clase "x" a la "X"
  }


  let cont1 = 0; 
  let cont2 = 0;
  let gameOver = false; // Variable para indicar si el juego ha terminado

// Event listener para los botones normales

botones.forEach(boton => {
    boton.addEventListener("click", () => { // el addEvent es para que cuando apretemos los botones pasen cosas
        if (gameOver) return; // Si el juego ha terminado, no permitimos que el usuario haga un movimiento
        if (boton.textContent !== "") return;

        const botonApretado = boton.textContent;

        if (boton.id === "cas1" || boton.id === "cas2" || boton.id === "cas3" || boton.id === "cas4" || 
            boton.id === "cas5" || boton.id === "cas6" || boton.id === "cas7" || boton.id === "cas8" || 
            boton.id === "cas9") {
            boton.textContent = "O";
            boton.innerHTML = '<span class="o">O</span>'; // Agrega la clase "o" a la "O"
            
            if ((document.getElementById("cas1").textContent === "O" && 
                document.getElementById("cas2").textContent === "O" && 
                document.getElementById("cas3").textContent === "O") ||
                (document.getElementById("cas4").textContent === "O" && 
                document.getElementById("cas5").textContent === "O" && 
                document.getElementById("cas6").textContent === "O") ||
                (document.getElementById("cas7").textContent === "O" && 
                document.getElementById("cas8").textContent === "O" && 
                document.getElementById("cas9").textContent === "O") ||
                (document.getElementById("cas1").textContent === "O" && 
                document.getElementById("cas4").textContent === "O" && 
                document.getElementById("cas7").textContent === "O") ||
                (document.getElementById("cas2").textContent === "O" && 
                document.getElementById("cas5").textContent === "O" && 
                document.getElementById("cas8").textContent === "O") ||
                (document.getElementById("cas3").textContent === "O" && 
                document.getElementById("cas6").textContent === "O" && 
                document.getElementById("cas9").textContent === "O") ||
                (document.getElementById("cas1").textContent === "O" && 
                document.getElementById("cas5").textContent === "O" && 
                document.getElementById("cas9").textContent === "O") ||
                (document.getElementById("cas3").textContent === "O" && 
                document.getElementById("cas5").textContent === "O" && 
                document.getElementById("cas7").textContent === "O")) {
                    cont1++;
                    pantalla.textContent = "YOU WIN";
                    pantalla.classList.add("win"); // Agrega la clase "win" a la pantalla
                    document.getElementById("contador-jugador").textContent = cont1.toString(); 
                    gameOver = true; // El juego ha terminado
                    return;
            }

            machineMove(); // Llamamos a la función machineMove() después de que el usuario haga un movimiento

            if ((document.getElementById("cas1").textContent === "X" && 
                document.getElementById("cas2").textContent === "X" && 
                document.getElementById("cas3").textContent === "X") ||
                (document.getElementById("cas4").textContent === "X" && 
                document.getElementById("cas5").textContent === "X" && 
                document.getElementById("cas6").textContent === "X") ||
                (document.getElementById("cas7").textContent === "X" && 
                document.getElementById("cas8").textContent === "X" && 
                document.getElementById("cas9").textContent === "X") ||
                (document.getElementById("cas1").textContent === "X" && 
                document.getElementById("cas4").textContent === "X" && 
                document.getElementById("cas7").textContent === "X") ||
                (document.getElementById("cas2").textContent === "X" && 
                document.getElementById("cas5").textContent === "X" && 
                document.getElementById("cas8").textContent === "X") ||
                (document.getElementById("cas3").textContent === "X" && 
                document.getElementById("cas6").textContent === "X" && 
                document.getElementById("cas9").textContent === "X") ||
                (document.getElementById("cas1").textContent === "X" && 
                document.getElementById("cas5").textContent === "X" && 
                document.getElementById("cas9").textContent === "X") ||
                (document.getElementById("cas3").textContent === "X" && 
                document.getElementById("cas5").textContent === "X" && 
                document.getElementById("cas7").textContent === "X")) {
                    cont2++;
                    pantalla.textContent = "YOU LOSE";
                    pantalla.classList.add("lose"); // Agrega la clase "lose" a la pantalla
                    document.getElementById("contador-maquina").textContent = cont2.toString();
                    gameOver = true; // El juego ha terminado
            }
        
        
        }



    })
})


// Event listener para el botón de reset
resetButton.addEventListener("click", () => {
    botones.forEach(boton => {
        if (boton.id !== "reset") { // Excluimos el botón de reset
            boton.textContent = ""; // Establecemos el texto en blanco
            pantalla.classList.remove("win", "lose"); // Removemos las clases win y lose
            pantalla.textContent ="";
        }
    });
    gameOver = false; // Reiniciamos el juego
});


document.getElementById("next").addEventListener("click", function() {
    location.reload(true);
  });