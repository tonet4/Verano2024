const pantalla = document.querySelector(".pantalla");
const botones = document.querySelectorAll("button");

botones.forEach(boton => {
    boton.addEventListener("click", () => {
        const botonApretado = boton.textContent;
        
    if (pantalla.textContent === "0"){
        pantalla.textContent = botonApretado;
    } else { 
        pantalla.textContent += botonApretado;
    }
    
    if (boton.id == "igual") {
        pantalla.textContent = eval(pantalla.textContent);
        return;
    }
    
    if (boton.id == "borraTodo") {  // condición para borrar todo
        pantalla.textContent = "";
        return; // con este return ya no sigue el código y vuelve a mpezar
    }

    if (boton.id === "borra") {  
        pantalla.textContent = pantalla.textContent.slice(0, -1);
        return; 
    }

    
    
    
    })
})