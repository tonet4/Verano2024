const pantalla = document.querySelector(".pantalla"); // llamamos a la pantalla
const botones = document.querySelectorAll(".btn"); // llamamos a todos los botones
const resetButton = document.getElementById("reset"); // llamamos al botón de reset

const resultado1 = document.querySelector(".marca1");
const resultado2 = document.querySelector(".marca2");

let cont1 = 0;
let cont2 = 0;
let gameOver = false; // Variable para indicar si el juego ha terminado

// Función para generar un movimiento aleatorio de la máquina
function machineMove() {
    if (blockOrWin("X") || blockOrWin("O")) {
        return;
    }
    const availableButtons = Array.from(botones).filter(boton => boton.textContent === ""); // Filtramos los botones que no estén ocupados
    const randomIndex = Math.floor(Math.random() * availableButtons.length); // Generamos un índice aleatorio
    const randomButton = availableButtons[randomIndex]; // Seleccionamos el botón aleatorio
  
    // Actualizamos el texto del botón aleatorio con la marca de la máquina (en este caso, "X")
    randomButton.textContent = "X";
    randomButton.innerHTML = '<span class="x">X</span>'; // Agrega la clase "x" a la "X"
}

// Función para bloquear al jugador o ganar si es posible
function blockOrWin(mark) {
    const winPatterns = [
        ["cas1", "cas2", "cas3"],
        ["cas4", "cas5", "cas6"],
        ["cas7", "cas8", "cas9"],
        ["cas1", "cas4", "cas7"],
        ["cas2", "cas5", "cas8"],
        ["cas3", "cas6", "cas9"],
        ["cas1", "cas5", "cas9"],
        ["cas3", "cas5", "cas7"]
    ];

    for (let pattern of winPatterns) {
        const [a, b, c] = pattern.map(id => document.getElementById(id).textContent);
        const emptyCell = pattern.find(id => document.getElementById(id).textContent === "");
        if ((a === mark && b === mark && c === "") ||
            (a === mark && c === mark && b === "") ||
            (b === mark && c === mark && a === "")) {
            document.getElementById(emptyCell).textContent = "X";
            document.getElementById(emptyCell).innerHTML = '<span class="x">X</span>';
            return true;
        }
    }
    return false;
}

// Event listener para los botones normales
botones.forEach(boton => {
    boton.addEventListener("click", () => { // el addEvent es para que cuando apretemos los botones pasen cosas
        if (gameOver) return; // Si el juego ha terminado, no permitimos que el usuario haga un movimiento
        if (boton.textContent !== "") return;

        boton.textContent = "O";
        boton.innerHTML = '<span class="o">O</span>'; // Agrega la clase "o" a la "O"

        if (checkWin("O")) {
            cont1++;
            pantalla.textContent = "YOU WIN";
            pantalla.classList.add("win"); // Agrega la clase "win" a la pantalla
            document.getElementById("contador-jugador").textContent = cont1.toString();
            gameOver = true; // El juego ha terminado
            return;
        }

        machineMove(); // Llamamos a la función machineMove() después de que el usuario haga un movimiento

        if (checkWin("X")) {
            cont2++;
            pantalla.textContent = "YOU LOSE";
            pantalla.classList.add("lose"); // Agrega la clase "lose" a la pantalla
            document.getElementById("contador-maquina").textContent = cont2.toString();
            gameOver = true; // El juego ha terminado
        }
    })
})

// Función para verificar si hay un ganador
function checkWin(mark) {
    const winPatterns = [
        ["cas1", "cas2", "cas3"],
        ["cas4", "cas5", "cas6"],
        ["cas7", "cas8", "cas9"],
        ["cas1", "cas4", "cas7"],
        ["cas2", "cas5", "cas8"],
        ["cas3", "cas6", "cas9"],
        ["cas1", "cas5", "cas9"],
        ["cas3", "cas5", "cas7"]
    ];

    return winPatterns.some(pattern => {
        const [a, b, c] = pattern.map(id => document.getElementById(id).textContent);
        return a === mark && b === mark && c === mark;
    });
}

// Event listener para el botón de reset
resetButton.addEventListener("click", () => {
    botones.forEach(boton => {
        if (boton.id !== "reset") { // Excluimos el botón de reset
            boton.textContent = ""; // Establecemos el texto en blanco
            pantalla.classList.remove("win", "lose"); // Removemos las clases win y lose
            pantalla.textContent = "";
        }
    });
    gameOver = false; // Reiniciamos el juego
});

document.getElementById("next").addEventListener("click", function() {
    location.reload(true);
});
