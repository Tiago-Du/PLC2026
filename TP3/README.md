# TPC1

## Autor
**Nome:** Tiago Du

**Número de aluno:** A112235

**Foto:**

<img src="FOTO.png" alt="Fotografia" width="250">

## Resumo

O objetivo deste trabalho foi fazer um analisador léxico em Python para uma linguagem de queries (SPARQL). O programa lê um ficheiro texto e segmenta-o nos seus tokens constituintes (variáveis, string, palavras-chave, delimitadores e conceitos).

No código recorri ao módulo re através da função re.findall, utilizando uma única Expressão Regular combinada. A ordem dos padrões nesta expressão foi um fator crucial: as palavras (select, where, LIMIT) foram colocadas antes dos padrões genéricos de conceitos para evitar conflitos de classificação. Após a extração, os tokens foram categorizados através de condições if/elif simples.

O resultado é um script simples acessível que, com o apoio do módulo sys para processar os ficheiros diretamente via terminal, cumpre todos os requisitos.

## Lista de Resultados

[Analisador Léxico](analisador_lexico.py)
[Ficheiro teste](teste.txt)