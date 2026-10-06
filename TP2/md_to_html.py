import re 

def md_to_html (texto):
    texto = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1">', texto)
    texto = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', texto)
    texto = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", texto)
    texto = re.sub(r"\*(.*?)\*", r"<i>\1</i>", texto)
    texto = re.sub(r"^### (.*)$", r"<h3>\1</h3>", texto, flags=re.MULTILINE)
    texto = re.sub(r"^## (.*)$", r"<h2>\1</h2>", texto, flags=re.MULTILINE)
    texto = re.sub(r"^# (.*)$", r"<h1>\1</h1>", texto, flags=re.MULTILINE)
    texto = re.sub(r"^\s*\d+\. (.*)$", r"<li>\1</li>", texto, flags=re.MULTILINE)
    texto = re.sub(r"(<li>.*</li>\n?)+", r"<ol>\n\g<0></ol>", texto)
    return texto

teste = """#TESTE
 
Este é um exemplo de texto com *itálico* e **negrito**.

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coelho.com)

1. Primeiro item
2. Segundo item
3. Terceiro item"""

print (md_to_html(teste))