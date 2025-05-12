// Exibe uma mensagem de boas-vindas ao carregar a página
window.onload = function () {
    alert("Bem-vindo ao site de Treinamento de Desenvolvimento Web!");
};

// Adiciona funcionalidade ao botão de alerta
function mostrarMensagem() {
    alert("Você clicou no botão!");
}

// Altera o estilo do título principal ao passar o mouse
const tituloPrincipal = document.querySelector("h1");
tituloPrincipal.addEventListener("mouseover", function () {
    tituloPrincipal.style.color = "#3498db"; // Azul
    tituloPrincipal.style.transition = "color 0.5s";
});

tituloPrincipal.addEventListener("mouseout", function () {
    tituloPrincipal.style.color = "#ebebeb"; // Branco
});

// Adiciona interatividade ao formulário
const formulario = document.querySelector("form");
formulario.addEventListener("submit", function (event) {
    event.preventDefault(); // Impede o envio do formulário
    const nome = document.querySelector("#nome").value;
    const email = document.querySelector("#email").value;

    if (nome && email) {
        alert(`Obrigado, ${nome}! Seus dados foram enviados com sucesso.`);
    } else {
        alert("Por favor, preencha todos os campos.");
    }
});

// Adiciona funcionalidade para alternar o tema claro/escuro
const botaoTema = document.createElement("button");
botaoTema.textContent = "Alternar Tema";
botaoTema.style.backgroundColor = "#00ff6c";
botaoTema.style.color = "#121212";
botaoTema.style.border = "none";
botaoTema.style.padding = "10px 20px";
botaoTema.style.borderRadius = "5px";
botaoTema.style.cursor = "pointer";
botaoTema.style.marginTop = "20px";

document.body.appendChild(botaoTema);

botaoTema.addEventListener("click", function () {
    const body = document.body;
    if (body.style.backgroundColor === "white") {
        body.style.backgroundColor = "#121212"; // Fundo escuro
        body.style.color = "#e0e0e0"; // Texto claro
        botaoTema.style.backgroundColor = "#00ff6c";
        botaoTema.style.color = "#121212";
    } else {
        body.style.backgroundColor = "white"; // Fundo claro
        body.style.color = "#121212"; // Texto escuro
        botaoTema.style.backgroundColor = "#3498db";
        botaoTema.style.color = "white";
    }
});