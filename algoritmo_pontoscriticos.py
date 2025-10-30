#Algoritmo para calcular pontos criticos de uma função, da matéria de Caculo Diferencial e Integral I

import sympy as sp

x = sp.symbols('x')

def _safe_float(expr):
    try:
        val = complex(sp.N(expr))
        if abs(val.imag) < 1e-8:
            return float(val.real)
    except Exception:
        pass
    return None

def analisar_funcao(func_texto):
    """
    Recebe uma string com f(x) e retorna:
      f (símbolo), pontos_criticos (lista), pontos_inflexao (lista), resultados (lista de mensagens)
    """
    x = sp.symbols('x')
    f = sp.sympify(func_texto)

    # derivadas
    f_1derivada = sp.diff(f, x)
    f_2derivada = sp.diff(f_1derivada, x)

    # raízes (potenciais pontos)
    pontos_criticos = sp.solve(sp.simplify(f_1derivada), x)
    pontos_inflexao = sp.solve(sp.simplify(f_2derivada), x)

    resultados = []
    eps = 1e-6

    # Classificação dos pontos críticos usando segunda derivada
    if not pontos_criticos:
        resultados.append("Não há pontos críticos para analisar.")
    else:
        for ponto in pontos_criticos:
            val_segunda = _safe_float(f_2derivada.subs(x, ponto))
            if val_segunda is None:
                resultados.append(f"O ponto crítico {ponto} necessita de análise adicional (valor não numérico).")
            else:
                if val_segunda > 0:
                    resultados.append(f"O ponto crítico {ponto} é um mínimo local.")
                elif val_segunda < 0:
                    resultados.append(f"O ponto crítico {ponto} é um máximo local.")
                else:
                    resultados.append(f"O ponto crítico {ponto} é um ponto de inflexão ou necessita de análise adicional (segunda derivada zero).")

    # Análise dos pontos de inflexão: verifica mudança de sinal da segunda derivada ao redor do ponto
    if not pontos_inflexao:
        resultados.append("Não há pontos de inflexão identificados pela segunda derivada.")
    else:
        for ponto in pontos_inflexao:
            left = _safe_float(f_2derivada.subs(x, ponto - eps))
            right = _safe_float(f_2derivada.subs(x, ponto + eps))
            if left is None or right is None:
                resultados.append(f"O ponto de inflexão {ponto} necessita de análise adicional (avaliação numérica falhou).")
            else:
                if left == 0 or right == 0:
                    resultados.append(f"O ponto de inflexão {ponto} necessita de análise adicional (amostras deram zero).")
                elif left * right < 0:
                    # houve mudança de sinal -> inflexão confirmada
                    if left > 0 and right < 0:
                        resultados.append(f"O ponto de inflexão {ponto} tem concavidade para cima antes do ponto e para baixo depois (mudança + -> -).")
                    elif left < 0 and right > 0:
                        resultados.append(f"O ponto de inflexão {ponto} tem concavidade para baixo antes do ponto e para cima depois (mudança - -> +).")
                    else:
                        resultados.append(f"O ponto de inflexão {ponto} apresenta mudança de concavidade.")
                else:
                    resultados.append(f"O ponto {ponto} não apresentou mudança de sinal da segunda derivada nas amostras; requer análise adicional.")

    return f, pontos_criticos, pontos_inflexao, resultados
