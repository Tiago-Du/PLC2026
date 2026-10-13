import sys
import re

def classificar_token(valor):
    """Função simples que diz o tipo de cada pedaço de texto encontrado."""
    if valor.startswith('#'):
        return 'COMENTARIO'
    elif valor.startswith('"'):
        return 'STRING'
    elif valor.startswith('@'):
        return 'LINGUA'
    elif valor.startswith('?'):
        return 'VARIAVEL'
    elif valor == 'LIMIT':
        return 'LIMIT'
    elif valor in ('select', 'where'):
        return 'PALAVRA_CHAVE'
    elif valor.isdigit():
        return 'NUMERO'
    elif valor in '{}.':
        return 'DELIMITADOR'
    else:
        return 'CONCEITO'

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            texto = f.read()
    else:
        texto = sys.stdin.read()

    padrao = r'#.*|"[^"]*"|@[a-zA-Z]{2}|\?[a-zA-Z0-9_]+|\bLIMIT\b|\bselect\b|\bwhere\b|\d+|[a-zA-Z0-9_]+:[a-zA-Z0-9_]+|[a-zA-Z0-9_]+|[{}.]'

    todos_os_tokens = re.findall(padrao, texto)

    for item in todos_os_tokens:
        tipo = classificar_token(item)
        if tipo != 'COMENTARIO':
            print(f"({tipo}, '{item}')")

if __name__ == '__main__':
    main()