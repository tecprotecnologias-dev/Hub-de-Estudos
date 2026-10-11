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


def carregar(arquivo, pasta='exercicios'):
    spec = importlib.util.spec_from_file_location(f'{pasta}_{arquivo[:-3]}', os.path.join(AQUI, pasta, arquivo))
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


PRELUDIO = '#include <iostream>\n#include <string>\nusing namespace std;\n'
normalizar = lambda s: ' '.join(s.split())


def testar_objetiva(ob, rotulo, gpp, tmp):
    """Questão objetiva com 'executar' (C++) ou 'executar_java': a saída do programa tem de ser
    exatamente a alternativa certa (espaços normalizados) e diferente das erradas."""
    erros = []
    alternativas = [ob['certa']] + ob['erradas']
    if len(ob['erradas']) != 3 or len(set(map(normalizar, alternativas))) != 4:
        erros.append(f'{rotulo}: precisa de 1 certa e 3 erradas diferentes')
    programa, linguagem = ob.get('executar'), 'C++'
    if programa is True:
        programa = ob['codigo']
    if ob.get('executar_java'):
        programa, linguagem = ob['executar_java'], 'Java'
    if not programa:
        return erros
    if linguagem == 'C++':
        if 'int main' not in programa:
            programa = PRELUDIO + 'int main() {\n' + programa + '\nreturn 0;\n}\n'
        elif '#include' not in programa:
            programa = PRELUDIO + programa
        fonte, exe = os.path.join(tmp, 'ob.cpp'), os.path.join(tmp, 'ob.exe')
        open(fonte, 'w', encoding='utf-8').write(programa)
        # sem -Wextra: algumas questões mostram de propósito código que gera aviso (ex.: switch sem break)
        r = subprocess.run([gpp, '-std=c++17', fonte, '-o', exe], capture_output=True, text=True)
        if r.returncode != 0:
            return erros + [f'{rotulo}: não compila\n{r.stderr[:400]}']
        r = subprocess.run([exe], capture_output=True, timeout=10)
    else:
        import re
        nome = re.search(r'public\s+class\s+(\w+)', programa).group(1)
        pasta = os.path.join(tmp, 'objava')
        os.makedirs(pasta, exist_ok=True)
        fonte = os.path.join(pasta, nome + '.java')
        open(fonte, 'w', encoding='utf-8').write(programa)
        r = subprocess.run(['javac', '-encoding', 'UTF-8', '-d', pasta, fonte], capture_output=True, text=True)
        if r.returncode != 0:
            return erros + [f'{rotulo}: Java não compila\n{r.stderr[:400]}']
        r = subprocess.run(['java', '-Dstdout.encoding=UTF-8', '-cp', pasta, nome], capture_output=True, timeout=20)
    saida = normalizar(r.stdout.decode('utf-8', 'replace'))
    if saida != normalizar(ob['certa']):
        erros.append(f'{rotulo}: o programa mostra {saida!r}, mas a alternativa certa é {ob["certa"]!r}')
    return erros


def converter_objetiva(capitulo, n, ob):
    # a alternativa certa muda de posição de uma questão para outra (o site ainda embaralha)
    pos = (n * 3 + len(capitulo)) % 4
    alternativas = list(ob['erradas'])
    alternativas.insert(pos, ob['certa'])
    q = {
        'id': f'{capitulo}-o{n}',
        'disciplinaId': DISCIPLINA,
        'capituloId': capitulo,
        'tipo': 'objetiva',
        'nivel': ob['nivel'],
    }
    if ob.get('codigo'):
        q['contexto'] = [{'t': 'codigo', 'texto': ob['codigo']}]
    q['enunciado'] = ob['enunciado']
    q['alternativas'] = alternativas
    q['correta'] = pos
    q['resolucao'] = ob['resolucao']
    return q


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
        for arquivo in sorted(f for f in os.listdir(os.path.join(AQUI, 'objetivas')) if f.startswith('cap')):
            m = carregar(arquivo, 'objetivas')
            for n, ob in enumerate(m.QUESTOES, 1):
                rotulo = f'{m.CAPITULO} objetiva {n}'
                erros += testar_objetiva(ob, rotulo, gpp, tmp)
                q = converter_objetiva(m.CAPITULO, n, ob)
                texto = json.dumps(q, ensure_ascii=False).lower()
                erros += [f'{rotulo}: termo proibido "{t}"' for t in TERMOS_PROIBIDOS if t in texto]
                banco.append(q)
            print(f'{m.CAPITULO}: {len(m.QUESTOES)} objetivas')
    if erros:
        print('\n'.join(erros))
        sys.exit(1)
    with open(DESTINO, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(banco, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'{len(banco)} questões testadas e gravadas em {os.path.normpath(DESTINO)}')


if __name__ == '__main__':
    main()
