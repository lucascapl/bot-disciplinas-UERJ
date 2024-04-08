# Projeto de Visualização de Disciplinas Restantes

Este projeto se trata de uma ferramenta para auxiliar os alunos a visualizarem as disciplinas restantes a serem cursadas através de uma busca no site do Aluno Online UERJ.

## Como utilizar

### Pré-requisitos

- Python 3 instalado
- Gerenciador de pacotes pip instalado
- Selenium instalado

### Instalação
1. Clone o repositório:

   ```sh
   git clone https://github.com/lucascapl/bot-disciplinas-UERJ.git
   
2. Crie um arquivo chamado  "config.txt" na raiz do projeto.

   ```plaintext
   matricula:sua_matricula
   senha:sua_senha

3. Preencha com sua matrícula e senha usadas para acessar o aluno online e salve o arquivo.


4. Execute o main.py

    ```sh
    python main.py

Isso abrirá um navegador Chrome automatizado que fará login no Aluno Online e mostrará as disciplinas restantes a serem cursadas dentro do console.

**Observação**: Este projeto foi desenvolvido apenas para fins educacionais e de aprendizado. Não nos responsabilizamos pelo uso indevido do mesmo. Recomendamos que utilize apenas **uma vez por período**.
