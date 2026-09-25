# TPC1

## Autor
**Nome:** Tiago Du

**Número de aluno:** A112235

**Foto:**

<img src="FOTO.png" alt="Fotografia" width="250">

## Resumo

O objetivo deste trabalho foi chegar a uma expressão regular que detete strings binárias que não contenham a substring 011.

Para garantir que a sequência acima indicada nunca é gerada, a estratégia adotada focou-se em utilizar apenas blocos de construção seguros. Como a sequência começa com 0, qualquer quantidade de 1s no início da palavra é inofensiva, isto é, (1*). Após o primeiro 0, limitamos a construção aos blocos seguros 0 e 01.

Agrupando e repetindo apenas estes dois blocos, é impossível gerar a sequência 011.

## Lista de Resultados

[Expressão Geral](expressao)

[Código do Regex](testes.py)