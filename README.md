🛠️ README: Backend (Python + FastAPI)
Repositório: encurtador-de-links

Encurtador de Links - API 🚀
API robusta desenvolvida para gerir o encurtamento de URLs, armazenamento em base de dados e redirecionamento dinâmico.

📝 Descrição
Este é o núcleo do projeto, responsável por receber URLs longas, gerar códigos únicos e processar o redirecionamento. A API está hospedada no Render e comunica diretamente com o MongoDB Atlas.

⚙️ Tecnologias
FastAPI: Framework moderno para construção de APIs de alta performance.

MongoDB: Banco de dados NoSQL utilizado para persistência dos links e contagem de cliques.

Motor: Driver assíncrono para integração com MongoDB.

📡 Endpoints Principais
POST /api/v1/links/: Cria um novo link encurtado. Recebe { "target_url": "..." }.

GET /api/v1/links/{code}: Busca o link no banco, incrementa o contador de cliques e redireciona o usuário (Status 307).

🌐 Deploy
URL Base: https://encurtador-de-links-h4p4.onrender.com/api/v1