
"""
Parabola Lab - Equazioni e disequazioni di secondo grado

Esegui con:
    streamlit run parabola_lab.py

Permette di muovere la parabola y = a(x-h)^2 + k
e osservare:
- dove interseca l'asse x: soluzioni dell'equazione y = 0;
- dove sta sopra l'asse x: soluzioni della disequazione y > 0;
- dove sta sotto l'asse x: soluzioni della disequazione y < 0.
"""

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Parabola Lab", layout="wide")

st.title("Parabola Lab")
st.subheader("Dal completamento del quadrato alle disequazioni di secondo grado")

st.markdown(
    "Muovi i cursori e osserva come cambiano le soluzioni dell'equazione "
    "$a(x-h)^2+k=0$ e delle disequazioni associate."
)

col_controls, col_plot = st.columns([1, 2])

with col_controls:
    st.header("Parametri")

    a = st.slider("Apertura a", -3.0, 3.0, 1.0, 0.1)
    h = st.slider("Spostamento orizzontale h", -20.0, 20.0, -12.0, 0.5)
    k = st.slider("Spostamento verticale k", -600.0, 600.0, -484.0, 10.0)

    st.markdown("### Parabola")
    st.latex(r"y = a(x-h)^2+k")
    st.latex(fr"y = {a:.1f}(x-({h:.1f}))^2+({k:.1f})")

    roots = []

    if abs(a) < 1e-9:
        st.warning("Con a = 0 non abbiamo una parabola.")
    else:
        valore = -k / a

        st.markdown("### Equazione")
        st.latex(r"a(x-h)^2+k=0")

        if valore < 0:
            st.write("Nessuna soluzione reale: la parabola non incontra l'asse x.")
        elif abs(valore) < 1e-9:
            x0 = h
            roots = [x0]
            st.write(f"Una soluzione doppia: x = {x0:.2f}")
        else:
            r = np.sqrt(valore)
            x1 = h - r
            x2 = h + r
            roots = [x1, x2]
            st.write(f"Due soluzioni: x1 = {x1:.2f}, x2 = {x2:.2f}")

        st.markdown("### Differenza chiave")
        st.write("Equazione: cerca i punti in cui y = 0.")
        st.write("Disequazione y > 0: cerca gli intervalli in cui la parabola sta sopra l'asse x.")
        st.write("Disequazione y < 0: cerca gli intervalli in cui la parabola sta sotto l'asse x.")

with col_plot:
    x = np.linspace(-40, 40, 1000)
    y = a * (x - h) ** 2 + k

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, y, linewidth=2, label="parabola")
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)

    ax.fill_between(x, y, 0, where=(y > 0), alpha=0.18, label="y > 0")
    ax.fill_between(x, y, 0, where=(y < 0), alpha=0.18, label="y < 0")

    ax.scatter([h], [k], s=60)
    ax.annotate(f"V({h:.1f}, {k:.1f})", (h, k), textcoords="offset points", xytext=(10, 10))

    for root in roots:
        ax.scatter([root], [0], s=70)
        ax.annotate(f"x={root:.2f}", (root, 0), textcoords="offset points", xytext=(5, 10))

    ax.set_xlim(-40, 40)
    ax.set_ylim(-600, 600)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Parabola, equazione e disequazioni")
    ax.grid(True, alpha=0.3)
    ax.legend()

    st.pyplot(fig)

st.markdown("---")
st.markdown(
    "Esempio dal laboratorio con i cartoncini: "
    "$x^2+24x=340 \\Rightarrow x^2+24x-340=0 \\Rightarrow (x+12)^2-484=0$."
)
