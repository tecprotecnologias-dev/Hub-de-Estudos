"""Compila (C++) e executa (Python) todos os trechos de código de um capítulo do livro.

Uso:
    python testar_codigo.py capitulos/capitulo-01.tex [caminho do g++]

Trechos com "int main" são compilados como estão; definições soltas (funções, structs,
classes, templates) ganham um main vazio; comandos soltos são colocados dentro de um main.
Todos recebem #include <iostream>, <string> e "using namespace std;" no início.
Trechos em Python (def, print, input, class com ":") são executados com o Python.
Trechos em Java ("public" sem dois-pontos, ou System.out) são compilados com javac -Xlint:all
e, se tiverem main, executados com java.
Algoritmos em Portugol (começam com algoritmo "Nome") são pulados, assim como código com erro
proposital (começa com // erro), comandos de terminal (começam com $) e mensagens do compilador.
"""
import os
import re
import subprocess
import sys
import tempfile

PRELUDIO = '#include <iostream>\n#include <string>\nusing namespace std;\n'
DEFINICAO = re.compile(r'^\s*(template\b|struct\b|class\b|#include\b|(?:bool|void|int|double|T)\s+\w+\s*\()', re.M)


def eh_python(codigo):
    return bool(re.search(r'^\s*(def |print\(|class \w+:|\w+ = int\(input)', codigo, re.M))


def eh_java(codigo):
    # linha começando com "public" seguido de palavra (em C++ é "public:", e a herança
    # "class B : public A" não começa a linha) ou System.out
    return bool(re.search(r'^\s*public\s+\w|System\.out', codigo, re.M))


def testar_java(codigo, pasta):
    """Compila com javac (avisos ligados) e, se houver main, executa a classe que o contém."""
    publica = re.search(r'public\s+(?:abstract\s+|final\s+)?(?:class|interface)\s+(\w+)', codigo)
    nome = publica.group(1) if publica else 'Trecho'
    os.makedirs(pasta, exist_ok=True)
    arq = os.path.join(pasta, nome + '.java')
    open(arq, 'w', encoding='utf-8').write(codigo)
    r = subprocess.run(['javac', '-Xlint:all', '-encoding', 'UTF-8', '-d', pasta, arq],
                       capture_output=True, text=True)
    if r.returncode != 0 or 'static void main' not in codigo:
        return r
    antes = codigo[:codigo.index('static void main')]
    principal = re.findall(r'class\s+(\w+)', antes)[-1]
    return subprocess.run(['java', '-Dstdout.encoding=UTF-8', '-cp', pasta, principal],
                          input='30\n4\n', capture_output=True, text=True, encoding='utf-8', timeout=20)


def main():
    tex = open(sys.argv[1], encoding='utf-8').read()
    gpp = sys.argv[2] if len(sys.argv) > 2 else 'g++'
    trechos = re.findall(r'\\begin\{Verbatim\}(?:\[[^]]*\])?\n(.*?)\\end\{Verbatim\}', tex, re.S)
    falhas = 0
    with tempfile.TemporaryDirectory() as tmp:
        for n, codigo in enumerate(trechos, 1):
            if re.match(r'\s*algoritmo\s+"', codigo, re.I):
                print(f'{n:2d} Portugol (não é compilado)')
                continue
            primeira = codigo.lstrip().split(chr(10), 1)[0]
            if primeira.startswith(('// erro', '// saída')) or primeira.startswith('$ ') or re.match(r'[\w.-]+\.cpp:', primeira):
                # código com erro proposital, comando de terminal ou mensagem do compilador
                print(f'{n:2d} exemplo de erro ou terminal (não é compilado)')
                continue
            if codigo.lstrip().startswith('// trecho'):
                # pedaço de uma classe mostrada completa (e testada) mais adiante no capítulo
                print(f'{n:2d} trecho (testado no programa completo)')
                continue
            if eh_python(codigo):
                arq = os.path.join(tmp, f't{n}.py')
                open(arq, 'w', encoding='utf-8').write(codigo)
                r = subprocess.run([sys.executable, arq], input='30\n', capture_output=True, text=True)
                tipo = 'Python'
            elif eh_java(codigo):
                r = testar_java(codigo, os.path.join(tmp, f'j{n}'))
                tipo = 'Java'
            else:
                if 'int main' in codigo:
                    fonte = PRELUDIO + codigo
                elif DEFINICAO.match(re.sub(r'^(\s*//[^\n]*\n)+', '', codigo).lstrip()):
                    fonte = PRELUDIO + codigo + '\nint main() { return 0; }\n'
                else:
                    fonte = PRELUDIO + 'int main() {\n' + codigo + '\nreturn 0;\n}\n'
                arq = os.path.join(tmp, f't{n}.cpp')
                exe = os.path.join(tmp, f't{n}.exe')
                open(arq, 'w', encoding='utf-8').write(fonte)
                r = subprocess.run([gpp, '-std=c++17', '-Wall', '-Wextra', arq, '-o', exe],
                                   capture_output=True, text=True)
                if r.returncode == 0:
                    r = subprocess.run([exe], input='30\n4\n', capture_output=True, text=True, timeout=10)
                tipo = 'C++'
            ok = r.returncode == 0 and 'warning' not in (r.stderr or '')
            falhas += not ok
            saida = (r.stdout or '').strip().replace('\n', ' | ')[:90]
            print(f'{n:2d} {tipo:6s} {"OK " if ok else "FALHOU"} {saida}')
            if not ok:
                print('   ', (r.stderr or '').strip()[:600])
    print(f'{len(trechos)} trechos, {falhas} com problema')
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    main()
