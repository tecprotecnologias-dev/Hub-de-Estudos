"""Gera o banco de exercícios práticos de Algoritmos I para o site, testando as soluções antes.

Uso (na pasta apostilas/algoritmos-i):
    python gerar_exercicios.py [caminho do g++]

Lê exercicios/capNN.py (lista EXERCICIOS), compila cada solução em C++ com -Wall -Wextra
(qualquer aviso conta como falha), executa com a entrada de cada exemplo e confere se todas
as linhas da saída esperada aparecem na saída do programa. Só grava
site/src/data/questoes/alg1.json se tudo passar. As soluções em Java (cap. 12) são testadas da
mesma forma com javac -Xlint:all; as em Portugol não são executadas.
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(AQUI, '..', '..', 'site', 'src', 'data', 'questoes', 'alg1.json')
DISCIPLINA = 'algoritmos-e-linguagem-de-programacao-i'
TERMOS_PROIBIDOS = ('faeterj', 'faetec', 'barra mansa', 'enade')


def carregar(arquivo):
    spec = importlib.util.spec_from_file_location(arquivo[:-3], os.path.join(AQUI, 'exercicios', arquivo))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def testar(cpp, exemplos, rotulo, gpp, tmp):
    fonte = os.path.join(tmp, 'ex.cpp')
    exe = os.path.join(tmp, 'ex.exe')
    open(fonte, 'w', encoding='utf-8').write(cpp)
    r = subprocess.run([gpp, '-std=c++17', '-Wall', '-Wextra', fonte, '-o', exe], capture_output=True, text=True)
    if r.returncode != 0 or 'warning' in r.stderr:
        return [f'{rotulo}: não compila sem avisos\n{r.stderr[:500]}']
    erros = []
    for entrada, saida in exemplos:
        r = subprocess.run([exe], input=(entrada + '\n').encode(), capture_output=True, timeout=10)
        obtido = r.stdout.decode('utf-8', 'replace')
        faltando = [linha for linha in saida.split('\n') if linha.strip() not in obtido]
        if r.returncode != 0 or faltando:
            erros.append(f'{rotulo}: entrada {entrada!r} -> faltou {faltando} em {obtido!r}')
    return erros


def testar_java(codigo, exemplos, rotulo, tmp):
    import re
    publica = re.search(r'public\s+class\s+(\w+)', codigo)
    if not publica:
        return [f'{rotulo}: solução Java sem public class']
    nome = publica.group(1)
    pasta = os.path.join(tmp, 'java')
    os.makedirs(pasta, exist_ok=True)
    fonte = os.path.join(pasta, nome + '.java')
    open(fonte, 'w', encoding='utf-8').write(codigo)
    r = subprocess.run(['javac', '-Xlint:all', '-encoding', 'UTF-8', '-d', pasta, fonte], capture_output=True, text=True)
    if r.returncode != 0 or 'warning' in r.stderr:
        return [f'{rotulo}: Java não compila sem avisos\n{r.stderr[:500]}']
    erros = []
    for entrada, saida in exemplos:
        r = subprocess.run(['java', '-Dstdout.encoding=UTF-8', '-cp', pasta, nome],
                           input=(entrada + '\n').encode(), capture_output=True, timeout=20)
        obtido = r.stdout.decode('utf-8', 'replace')
        faltando = [linha for linha in saida.split('\n') if linha.strip() not in obtido]
        if r.returncode != 0 or faltando:
            erros.append(f'{rotulo} (Java): entrada {entrada!r} -> faltou {faltando} em {obtido!r}')
    return erros


def converter(capitulo, n, ex):
    q = {
        'id': f'{capitulo}-e{n}',
        'disciplinaId': DISCIPLINA,
        'capituloId': capitulo,
        'tipo': 'discursiva',
        'pratica': True,
        'nivel': ex['nivel'],
    }
    if ex.get('contexto'):
        q['contexto'] = [{'t': t, 'texto': texto} for t, texto in ex['contexto']]
    q['enunciado'] = ex['enunciado']
    q['exemplos'] = [{'entrada': e, 'saida': s} for e, s in ex['exemplos']]
    q['resolucao'] = [
        {'t': 'p', 'texto': texto} if t == 'p' else {'t': 'codigo', 'linguagem': t, 'texto': texto}
        for t, texto in ex['resolucao']
    ]
    return q


def main():
    gpp = sys.argv[1] if len(sys.argv) > 1 else 'g++'
    banco, erros = [], []
    with tempfile.TemporaryDirectory() as tmp:
        for arquivo in sorted(f for f in os.listdir(os.path.join(AQUI, 'exercicios')) if f.startswith('cap')):
            m = carregar(arquivo)
            for n, ex in enumerate(m.EXERCICIOS, 1):
                rotulo = f'{m.CAPITULO} exercício {n}'
                codigos = [texto for t, texto in ex['resolucao'] if t == 'C++']
                if not codigos:
                    erros.append(f'{rotulo}: sem solução em C++')
                for cpp in codigos:
                    erros += testar(cpp, ex['exemplos'], rotulo, gpp, tmp)
                for java in (texto for t, texto in ex['resolucao'] if t == 'Java'):
                    erros += testar_java(java, ex['exemplos'], rotulo, tmp)
                q = converter(m.CAPITULO, n, ex)
                texto = json.dumps(q, ensure_ascii=False).lower()
                erros += [f'{rotulo}: termo proibido "{t}"' for t in TERMOS_PROIBIDOS if t in texto]
                banco.append(q)
            print(f'{m.CAPITULO}: {len(m.EXERCICIOS)} exercícios')
    if erros:
        print('\n'.join(erros))
        sys.exit(1)
    with open(DESTINO, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(banco, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'{len(banco)} exercícios testados e gravados em {os.path.normpath(DESTINO)}')


if __name__ == '__main__':
    main()
