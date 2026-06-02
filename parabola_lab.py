import numpy as np
import matplotlib.pyplot as plt


def parabola(a=1, b=24, c=-340):

    x = np.linspace(-100, 100, 1000)
    y = a*x**2 + b*x + c

    display(Math(rf"y = {a:.1f}x^2 + {b:.1f}x + {c:.1f}"))
    display(Math(rf"{a:.1f}x^2 + {b:.1f}x + {c:.1f}=0"))

    if abs(a) < 1e-9:
        print("Con a = 0 non abbiamo una parabola.")
        return

    delta = b**2 - 4*a*c
    print(f"Δ = {delta:.2f}")

    roots = []

    if delta > 0:
        x1 = (-b - np.sqrt(delta))/(2*a)
        x2 = (-b + np.sqrt(delta))/(2*a)
        roots = [x1, x2]

        print("\nEQUAZIONE")
        print(f"x₁ = {x1:.2f}")
        print(f"x₂ = {x2:.2f}")

        print("\nDISEQUAZIONE > 0")
        if a > 0:
            print(f"x < {x1:.2f} oppure x > {x2:.2f}")
        else:
            print(f"{x1:.2f} < x < {x2:.2f}")

        print("\nDISEQUAZIONE < 0")
        if a > 0:
            print(f"{x1:.2f} < x < {x2:.2f}")
        else:
            print(f"x < {x1:.2f} oppure x > {x2:.2f}")

    elif np.isclose(delta, 0):
        x0 = -b/(2*a)
        roots = [x0]

        print("\nEQUAZIONE")
        print(f"Soluzione doppia: x = {x0:.2f}")

        print("\nDISEQUAZIONI")
        if a > 0:
            print(f"{a:.1f}x² + {b:.1f}x + {c:.1f} ≥ 0 per ogni x")
            print(f"{a:.1f}x² + {b:.1f}x + {c:.1f} > 0 per x ≠ {x0:.2f}")
        else:
            print(f"{a:.1f}x² + {b:.1f}x + {c:.1f} ≤ 0 per ogni x")
            print(f"{a:.1f}x² + {b:.1f}x + {c:.1f} < 0 per x ≠ {x0:.2f}")

    else:
        print("\nEQUAZIONE")
        print("Nessuna soluzione reale")

        print("\nDISEQUAZIONI")
        if a > 0:
            print(f"{a:.1f}x² + {b:.1f}x + {c:.1f} > 0 per ogni x")
            print(f"{a:.1f}x² + {b:.1f}x + {c:.1f} < 0 mai")
        else:
            print(f"{a:.1f}x² + {b:.1f}x + {c:.1f} < 0 per ogni x")
            print(f"{a:.1f}x² + {b:.1f}x + {c:.1f} > 0 mai")

    plt.figure(figsize=(9, 6))

    plt.plot(x, y, linewidth=3, label="parabola")
    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)

    plt.fill_between(x, y, 0, where=(y > 0), alpha=0.2, label="y > 0")
    plt.fill_between(x, y, 0, where=(y < 0), alpha=0.2, label="y < 0")

    xv = -b/(2*a)
    yv = a*xv**2 + b*xv + c

    plt.scatter([xv], [yv], s=100)
    plt.annotate(
        f"V({xv:.2f}, {yv:.2f})",
        (xv, yv),
        xytext=(10, 10),
        textcoords="offset points"
    )

    if len(roots) == 2:
        x1, x2 = roots

        plt.scatter([x1, x2], [0, 0], s=120)
        plt.axvline(x1, linestyle="--", linewidth=1)
        plt.axvline(x2, linestyle="--", linewidth=1)

        plt.annotate(
            f"x₁ = {x1:.2f}",
            (x1, 0),
            xytext=(0, 15),
            textcoords="offset points",
            ha="center"
        )

        plt.annotate(
            f"x₂ = {x2:.2f}",
            (x2, 0),
            xytext=(0, 15),
            textcoords="offset points",
            ha="center"
        )

        plt.text(
            0.02,
            0.98,
            f"x₁ = {x1:.2f}\nx₂ = {x2:.2f}",
            transform=plt.gca().transAxes,
            verticalalignment="top",
            bbox=dict(boxstyle="round")
        )

    elif len(roots) == 1:
        x0 = roots[0]

        plt.scatter([x0], [0], s=120)
        plt.axvline(x0, linestyle="--", linewidth=1)

        plt.annotate(
            f"x = {x0:.2f}",
            (x0, 0),
            xytext=(0, 15),
            textcoords="offset points",
            ha="center"
        )

        plt.text(
            0.02,
            0.98,
            f"x = {x0:.2f}",
            transform=plt.gca().transAxes,
            verticalalignment="top",
            bbox=dict(boxstyle="round")
        )

    plt.xlim(-100, 100)
    plt.ylim(-1000, 1000)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Parabola, equazione e disequazioni")
    plt.grid(True)
    plt.legend()
    plt.show()

interact(
    parabola,
    a=FloatSlider(min=-3, max=3, step=0.1, value=1),
    b=FloatSlider(min=-100, max=100, step=1, value=24),
    c=FloatSlider(min=-1000, max=1000, step=10, value=-340)
);
