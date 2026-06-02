import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Parabola Lab", layout="wide")

st.title("Parabola Lab")
st.subheader("Equazioni e disequazioni di secondo grado")

a = st.slider("Coefficiente a", -3.0, 3.0, 1.0, 0.1)
b = st.slider("Coefficiente b", -100.0, 100.0, 24.0, 1.0)
c = st.slider("Coefficiente c", -600.0, 600.0, -340.0, 10.0)

st.latex(fr"y = {a:.1f}x^2 + {b:.1f}x + {c:.1f}")
st.latex(fr"{a:.1f}x^2 + {b:.1f}x + {c:.1f}=0")

if abs(a) < 1e-9:
    st.warning("Con a = 0 non abbiamo una parabola.")
else:
    delta = b**2 - 4*a*c
    st.write(f"Δ = {delta:.2f}")

    roots = []

    if delta > 0:
        x1 = (-b - np.sqrt(delta))/(2*a)
        x2 = (-b + np.sqrt(delta))/(2*a)
        roots = [x1, x2]

        st.markdown("### Equazione")
        st.write(f"x₁ = {x1:.2f}")
        st.write(f"x₂ = {x2:.2f}")

        st.markdown("### Disequazione > 0")
        if a > 0:
            st.write(f"x < {x1:.2f} oppure x > {x2:.2f}")
        else:
            st.write(f"{x1:.2f} < x < {x2:.2f}")

        st.markdown("### Disequazione < 0")
        if a > 0:
            st.write(f"{x1:.2f} < x < {x2:.2f}")
        else:
            st.write(f"x < {x1:.2f} oppure x > {x2:.2f}")

    elif np.isclose(delta, 0):
        x0 = -b/(2*a)
        roots = [x0]

        st.markdown("### Equazione")
        st.write(f"Soluzione doppia: x = {x0:.2f}")

    else:
        st.markdown("### Equazione")
        st.write("Nessuna soluzione reale")

        if a > 0:
            st.write("La parabola sta sempre sopra l'asse x.")
        else:
            st.write("La parabola sta sempre sotto l'asse x.")

    x = np.linspace(-80, 80, 1200)
    y = a*x**2 + b*x + c

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, y, linewidth=3, label="parabola")
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)

    ax.fill_between(x, y, 0, where=(y > 0), alpha=0.2, label="y > 0")
    ax.fill_between(x, y, 0, where=(y < 0), alpha=0.2, label="y < 0")

    xv = -b/(2*a)
    yv = a*xv**2 + b*xv + c

    ax.scatter([xv], [yv], s=100)
    ax.annotate(
        f"V({xv:.2f}, {yv:.2f})",
        (xv, yv),
        xytext=(10, 10),
        textcoords="offset points"
    )

    if len(roots) == 2:
        x1, x2 = roots

        ax.scatter([x1, x2], [0, 0], s=120)
        ax.axvline(x1, linestyle="--", linewidth=1)
        ax.axvline(x2, linestyle="--", linewidth=1)

        ax.annotate(
            f"x₁ = {x1:.2f}",
            (x1, 0),
            xytext=(0, 15),
            textcoords="offset points",
            ha="center"
        )

        ax.annotate(
            f"x₂ = {x2:.2f}",
            (x2, 0),
            xytext=(0, 15),
            textcoords="offset points",
            ha="center"
        )

    elif len(roots) == 1:
        x0 = roots[0]

        ax.scatter([x0], [0], s=120)
        ax.axvline(x0, linestyle="--", linewidth=1)

        ax.annotate(
            f"x = {x0:.2f}",
            (x0, 0),
            xytext=(0, 15),
            textcoords="offset points",
            ha="center"
        )

    ax.set_xlim(-80, 80)
    ax.set_ylim(-800, 800)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Parabola, equazione e disequazioni")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)
