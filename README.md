📦 Sistema de Controle de Estoque – Loja de Eletrônicos

📌 Descrição do Projeto

Este projeto consiste em um Sistema de Controle de Estoque desenvolvido em Python, com foco no gerenciamento de produtos de uma loja de eletrônicos.

O sistema permite ao usuário, por meio de um menu interativo no terminal, realizar operações essenciais de estoque, como:
	•	Visualizar produtos cadastrados
	•	Adicionar novos produtos
	•	Atualizar informações de produtos existentes
	•	Excluir produtos do estoque
	•	Encerrar o sistema de forma segura

O objetivo principal do projeto é aplicar conceitos fundamentais de programação, como funções, estruturas de controle, manipulação de arquivos e organização de código, simulando o funcionamento de um sistema real utilizado no backend de aplicações.

⸻

🗂 Estrutura do Projeto

O projeto está organizado em três arquivos, seguindo boas práticas de separação de responsabilidades:

código:

📁 sistema-controle-estoque
 ├── sistema.py      # Arquivo principal (main) – controla o fluxo do sistema e o menu
 ├── estoque.py      # Responsável pelas regras de negócio do estoque
 └── estoque.txt     # Arquivo onde os dados dos produtos são armazenados

Essa separação facilita a manutenção, a leitura do código e futuras expansões do sistema.

⸻

⚙️ Funcionalidades
	•	📋 Visualizar estoque: lista todos os produtos com nome, preço e quantidade
	•	➕ Adicionar produto: cadastra um novo item no estoque
	•	✏️ Atualizar produto: altera preço e/ou quantidade de um produto existente
	•	❌ Excluir produto: remove um item do estoque
	•	🔁 Persistência de dados: os dados são salvos em arquivo .txt, garantindo que não sejam perdidos ao encerrar o programa

⸻

▶️ Como Executar o Projeto
	1.	Certifique-se de ter o Python 3 instalado na máquina
	2.	Clone este repositório ou faça o download dos arquivos
	3.	No terminal, navegue até a pasta do projeto
	4.	Execute o comando:
  
python sistema.py

O menu será exibido diretamente no terminal.

⸻

🧠 Conceitos Aplicados
	•	Funções (def)
	•	Estruturas de controle (if, elif, else, while, for)
	•	Manipulação de arquivos (open, read, write, append)
	•	Tratamento de erros com try/except
	•	Manipulação de strings (strip)
	•	Organização de código em módulos
	•	Simulação de um sistema backend via terminal

⸻

🎓 Contexto Acadêmico

Projeto desenvolvido como atividade avaliativa do curso de Análise e Desenvolvimento de Sistemas, com o objetivo de consolidar os conhecimentos iniciais em Python e lógica de programação.

⸻

👤 Autor

Tony Anderson
Estudante de Análise e Desenvolvimento de Sistemas
Projeto acadêmico para fins educacionais

⸻

🙏 Agradecimentos
	•	Professor Fernando Leonid (Coordenação e orientação acadêmica)
	•	Grupo Código & Café – FECAP / UniFECAF
	•	Colegas de curso que contribuíram com discussões e trocas de conhecimento
