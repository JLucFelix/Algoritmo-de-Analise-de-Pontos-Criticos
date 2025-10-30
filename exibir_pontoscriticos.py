import algoritmo_pontoscriticos
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def _to_float_point(p):
    try:
        pv = complex(sp.N(p))
        if abs(pv.imag) < 1e-8:
            return float(pv.real)
    except Exception:
        pass
    try:
        return float(p)
    except Exception:
        return None

texto_da_funcao = input("Digite a sua função f(x): ")

try:
    # agora desempacotamos os 4 valores retornados pelo algoritmo
    f, pontos_criticos, pontos_inflexao, resultados = algoritmo_pontoscriticos.analisar_funcao(texto_da_funcao)

    # (Pequena necessidade técnica: precisamos do 'x' aqui também)
    x = sp.symbols('x')

    # Mostra resultados simbólicos e mensagens de classificação
    print(f"Função: {f}")
    print(f"Pontos Críticos (simbolicamente): {pontos_criticos}")
    print(f"Pontos de Inflexão (simbolicamente): {pontos_inflexao}")
    print("Classificação / observações:")
    for r in resultados:
        print(" -", r)

    # Prepara função numérica
    f_numerica = sp.lambdify(x, f, 'numpy')

    # Decide intervalo de plotagem com base nos pontos críticos/inflexão quando possível
    xs_candidates = []
    for p in list(pontos_criticos) + list(pontos_inflexao):
        pf = _to_float_point(p)
        if pf is not None:
            xs_candidates.append(pf)

    if xs_candidates:
        xmin = min(xs_candidates) - 5
        xmax = max(xs_candidates) + 5
        if xmin == xmax:
            xmin -= 5
            xmax += 5
    else:
        xmin, xmax = -10, 10

    x_vals = np.linspace(xmin, xmax, 1500)

    # Avalia a função (tenta mascarar valores inválidos)
    with np.errstate(all='ignore'):
        y_vals = f_numerica(x_vals)

    # Converte valores complexos para nan quando necessário
    if np.iscomplexobj(y_vals):
        y_vals = np.where(np.abs(np.imag(y_vals)) < 1e-8, np.real(y_vals), np.nan)

    plt.figure(figsize=(10,6))
    plt.plot(x_vals, y_vals, label=f"f(x) = {str(f)}", color='tab:blue')

    # Segunda derivada simbólica para classificar pontos críticos
    f2 = sp.diff(f, x, 2)

    # Função auxiliar para avaliar simbolicamente um ponto e retornar float or None
    def eval_point(expr, pt):
        try:
            val = expr.subs(x, pt).evalf()
            valc = complex(val)
            if abs(valc.imag) < 1e-8:
                return float(valc.real)
        except Exception:
            pass
        return None

    # Marca pontos críticos
    for p in pontos_criticos:
        p_float = _to_float_point(p)
        if p_float is None:
            continue
        yp = eval_point(f, p)
        if yp is None or np.isnan(yp):
            continue
        # classificação pelo sinal da segunda derivada
        f2val = eval_point(f2, p)
        if f2val is None:
            label = f"Ponto crítico {p}"
            color = 'black'
        else:
            if f2val > 0:
                label = f"Mínimo em x={p}"
                color = 'green'
            elif f2val < 0:
                label = f"Máximo em x={p}"
                color = 'red'
            else:
                label = f"Ponto crítico (indeterminado) x={p}"
                color = 'orange'
        plt.scatter([p_float], [yp], color=color, s=80, zorder=5)
        plt.annotate(label, (p_float, yp), textcoords="offset points", xytext=(5,5), fontsize=9)

    # Marca pontos de inflexão
    for p in pontos_inflexao:
        p_float = _to_float_point(p)
        if p_float is None:
            continue
        yp = eval_point(f, p)
        if yp is None or np.isnan(yp):
            continue
        plt.scatter([p_float], [yp], color='purple', marker='D', s=70, zorder=5)
        plt.annotate(f"Ponto de inflexão x={p}", (p_float, yp), textcoords="offset points", xytext=(5,-12), fontsize=9)

    plt.axhline(0, color='gray', linewidth=0.8)
    plt.axvline(0, color='gray', linewidth=0.8)
    plt.title("Gráfico de f(x) e pontos críticos / de inflexão")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Ocorreu um erro: {e}. Verifique a sua entrada.")