🔗 Short.it - Encurtador de Links Full Stack
O Short.it é uma aplicação completa para encurtamento de URLs, desenvolvida para demonstrar a integração entre um frontend moderno, uma API robusta e um banco de dados na nuvem.

🚀 Tecnologias Utilizadas
Frontend: React.js com Vite e Axios para consumo de API.

Backend: Python com FastAPI para uma API de alta performance.

Banco de Dados: MongoDB Atlas (NoSQL) para persistência de dados e contagem de cliques.

Deploy: Netlify (Frontend) e Render (Backend).

🛠️ Funcionalidades
Encurtamento de URL: Transforma links longos em códigos únicos (ex: 5uLDmT).

Redirecionamento Automático: Ao aceder ao link curto, o backend identifica o destino original no banco e redireciona o utilizador (Status 307).

Contador de Cliques: Regista quantas vezes cada link foi utilizado diretamente no documento do MongoDB.

Feedback em Tempo Real: Interface que indica estados de carregamento e permite copiar o link com um clique.

frontend repository:https://github.com/AdrianZapico/encurtadorlink