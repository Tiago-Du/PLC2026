# TPC1

## Autor
**Nome:** Tiago Du

**Número de aluno:** A112235

**Foto:**

<img src="FOTO.png" alt="Fotografia" width="250">

## Resumo

O objetivo deste trabalho foi fazer um conversor Markdown para HTML em Python para os seguintes elementos: cabeçalhos, texto a negrito, itálico, listas numeradas, links e imagens. Para cada elemento foi construída uma Expressão Regular adequada e processada através da função re.sub do módulo nativo re.

A implementação seguiu uma ordem específica onde a ordem das substituições é um fator crucial para evitar conflitos de sintaxe. Por exemplo, as imagens serem convertidas antes dos links, pois a sintaxe de uma imagem em Markdown contém, dentro, um link. No caso do negrito, este tem de ser convertido antes do itálico, pois ambos contêm asteriscos e a sintaxe do negrito, contém a sintaxe do itálico.

O resultado final é um script eficiente e de fácil leitura que cumpre todos os requisitos propostos, demonstrando na prática a eficácia das Expressões Regulares na manipulação e tranformação de texto estruturado.

## Lista de Resultados

[Conversor Markdown para HTML](md_to_html.py)