#=========================================================
# EffortModel.py
# Estimación de esfuerzo según LOC (PM)
# Versión lista para ejecutar
#=========================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# -----------------------------
# Dataset histórico
# -----------------------------
data = {
    'LOC': [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    'Esfuerzo': [2,3,5,7,11,13,17,19,23,29]
}
df = pd.DataFrame(data)

# -----------------------------
# MODELO LINEAL
# -----------------------------
a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
y_lin = a*df['LOC'] + b
R = np.corrcoef(df['LOC'], df['Esfuerzo'])[0,1]
R2_lin = R**2
print(f"Modelo lineal: E = {b:.5f} + {a:.5f}*LOC, R² = {R2_lin:.4f}")

# -----------------------------
# MODELO EXPONENCIAL: E = k * LOC^b
# -----------------------------
df['logEsfuerzo'] = np.log(df['Esfuerzo'])
df['logLOC'] = np.log(df['LOC'])
X = sm.add_constant(df['logLOC'])
model_exp = sm.OLS(df['logEsfuerzo'], X).fit()
k = np.exp(model_exp.params['const'])
b_exp = model_exp.params['logLOC']
R2_exp = model_exp.rsquared
print(f"Modelo exponencial: E = {k:.5f} * LOC^{b_exp:.5f}, R² = {R2_exp:.4f}")

# -----------------------------
# Elegir mejor modelo
# -----------------------------
if R2_lin > R2_exp:
    print("Se elige el modelo lineal")
    best_model = lambda x: a*x + b
else:
    print("Se elige el modelo exponencial")
    best_model = lambda x: k*(x**b_exp)

# -----------------------------
# Estimaciones
# -----------------------------
LOC_estimados = [9100, 200]
for loc in LOC_estimados:
    esfuerzo = best_model(loc)
    print(f"Esfuerzo estimado para LOC={loc}: {esfuerzo:.2f} PM")

# -----------------------------
# Gráfico
# -----------------------------
plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos históricos', color='blue')

# Graficar modelos
plt.plot(df['LOC'], a*df['LOC']+b, 'r-', label=f'Lineal (R²={R2_lin:.2f})')
plt.plot(df['LOC'], k*(df['LOC']**b_exp), 'g-', label=f'Exponencial (R²={R2_exp:.2f})')

# Graficar estimaciones
for loc in LOC_estimados:
    plt.scatter(loc, best_model(loc), color='black', s=80, label=f'Predicción LOC={loc}')

plt.xlabel('LOC')
plt.ylabel('Esfuerzo (PM)')
plt.title('Estimación de Esfuerzo por LOC')
plt.legend()
plt.grid(True)
plt.show()
