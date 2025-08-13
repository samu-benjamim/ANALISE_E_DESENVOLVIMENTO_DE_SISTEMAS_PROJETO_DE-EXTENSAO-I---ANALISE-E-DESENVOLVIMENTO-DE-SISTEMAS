# Sistema de Registro de Ocorrências de Iluminação Pública

## Descrição do Projeto

Este projeto foi desenvolvido como parte do Programa de Extensão do curso de **Análise e Desenvolvimento de Sistemas**. O sistema permite o registro, armazenamento e visualização de ocorrências relacionadas à iluminação pública em áreas urbanas.

O projeto foi **levantado e testado em campo** com um grupo de moradores, garantindo interação direta com a comunidade. Após validação, o sistema foi revisado e aprovado pela Prefeitura e está em funcionamento há um mês, proporcionando **agilidade, transparência e melhoria na comunicação entre moradores e administração municipal**.

### Objetivos

- Registrar ocorrências de falhas na iluminação pública.
- Organizar e disponibilizar dados para consulta e acompanhamento.
- Proporcionar melhoria na gestão das demandas urbanas e aumento da segurança.
- Aplicar conhecimentos do curso de ADS em um projeto prático e com impacto social.

---

## Funcionalidades

- Formulário para cadastro de ocorrências com campos de **Nome, Endereço e Descrição**.
- Interface para visualização das ocorrências cadastradas.
- Persistência dos dados em banco **SQLite**.
- Sistema web simples, responsivo e intuitivo.
- Histórico de ocorrências registrado e organizado para consultas futuras.

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Flask** – Framework web para backend.
- **SQLite** – Banco de dados leve e integrado.
- **HTML5, CSS3** – Estrutura e estilo da interface web.

---

## Estrutura do Projeto

├── app.py # Arquivo principal do Flask

├── ocorrencias.db # Banco de dados SQLite

├── templates/ # HTMLs do sistema

│ ├── index.html # Formulário de registro

│ └── visualizar.html # Visualização de ocorrências

├── README.md
