// scripts.js
document.getElementById("form-cadastro").addEventListener("submit", async (e) => {
  e.preventDefault(); // Impede que o formulário seja enviado da forma tradicional

  // Obtendo os dados dos campos
  const titulo = document.getElementById("newTitle").value;
  const autor = document.getElementById("newAuthor").value;
  const genero = document.getElementById("newGenre").value;
  const resumo = document.getElementById("newSummary").value;
  const statusLeitura = document.getElementById("status_leitura").value;

  // Enviando os dados via POST para a API
  try {
      const response = await fetch("/api/livros", {  // URL para sua API que adiciona livros
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({
              titulo,
              autor,
              genero,
              resumo,
              status_leitura: statusLeitura
          }),
      });

      const result = await response.json();
      if (response.ok) {
          console.log("Livro adicionado com sucesso!", result);
          // Aqui você pode adicionar o livro à lista na interface
      } else {
          console.error("Erro ao adicionar livro:", result);
      }
  } catch (error) {
      console.error("Erro de conexão:", error);
  }
});
