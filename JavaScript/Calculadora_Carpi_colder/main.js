
/*
ENLACE VIDEO TUTORIAL CALCULADORA
https://www.youtube.com/watch?v=hZFEgkrOwks 
*/

const pantalla = document.querySelector(".pantalla"); // llamamos a la pantalla
const botones = document.querySelectorAll(".btn"); // llamamos a todos los botones
// Al hacer un querySelectorAl se nos hace un array, por eso usamos un forEach para recorrerla
botones.forEach(boton => {
    boton.addEventListener("click", () => { // el addEvent es para que cuando apretemos los botones pasen cosas
        const botonApretado = boton.textContent;

        if (boton.id === "c") {
            pantalla.textContent = "0";
            return;
        }

        if (boton.id === "borrar"){
            if(pantalla.textContent.length === 1 || pantalla.textContent === "Error"){
                pantalla.textContent = "0";
            } else {
            pantalla.textContent = pantalla.textContent.slice(0, -1);
            }
            return;
        }

        if (boton.id === "igual"){
            try {
                pantalla.textContent = eval(pantalla.textContent);
            } catch {
                pantalla.textContent ="Error";
            }
            return;
        }
        
        if (pantalla.textContent === "0" || pantalla.textContent === "Error"){
            pantalla.textContent = botonApretado;
        } else {
            pantalla.textContent += botonApretado;
        }

        

    })
})