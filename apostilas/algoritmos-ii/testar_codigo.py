"""Compila (C++) e executa (Python) todos os trechos de código de um capítulo do livro.

Uso:
    python testar_codigo.py capitulos/capitulo-01.tex [caminho do g++]

Trechos com "int main" são compilados como estão; definições soltas (funções, structs,
classes, templates) ganham um main vazio; comandos soltos são colocados dentro de um main.
Todos recebem #include <iostream>, <string> e "using namespace std;" no início.
Trechos em Python (def, print, input, class com ":") são executados com o Python.
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


def main():
    tex = open(sys.argv[1], encoding='utf-8').read()
    gpp = sys.argv[2] if len(sys.argv) > 2 else 'g++'
    trechos = re.findall(r'\\begin\{Verbatim\}(?:\[[^]]*\])?\n(.*?)\\end\{Verbatim\}', tex, re.S)
    falhas = 0
    with tempfile.TemporaryDirectory() as tmp:
        for n, codigo in enumerate(trechos, 1):
            if codigo.lstrip().startswith('// trecho'):
                # pedaço de uma classe mostrada completa (e testada) mais adiante no capítulo
                print(f'{n:2d} trecho (testado no programa completo)')
                continue
            if eh_python(codigo):
                arq = os.path.join(tmp, f't{n}.py')
                open(arq, 'w', encoding='utf-8').write(codigo)
                r = subprocess.run([sys.executable, arq], input='30\n', capture_output=True, text=True)
                tipo = 'Python'
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
