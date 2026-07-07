#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate implementation-oriented MIMO design figures for Session 06."""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"

COLORS = {
    "blue": "#1f77b4",
    "orange": "#ff7f0e",
    "green": "#2ca02c",
    "red": "#d62728",
    "purple": "#9467bd",
    "teal": "#17becf",
    "gray": "#4f5b66",
    "light_gray": "#f3f5f7",
    "line": "#56616d",
}


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 15,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
        }
    )


def add_box(
    ax,
    x,
    y,
    w,
    h,
    text,
    *,
    facecolor,
    edgecolor=None,
    fontsize=9.5,
    weight="normal",
    textcolor="#20262d",
    radius=0.08,
    lw=1.6,
):
    edgecolor = edgecolor or facecolor
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.025,rounding_size={radius}",
        linewidth=lw,
        edgecolor=edgecolor,
        facecolor=facecolor,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight=weight,
        color=textcolor,
        linespacing=1.18,
    )
    return patch


def add_diamond(
    ax,
    cx,
    cy,
    w,
    h,
    text,
    *,
    facecolor,
    edgecolor=None,
    fontsize=9.5,
):
    edgecolor = edgecolor or facecolor
    verts = [(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)]
    patch = Polygon(
        verts,
        closed=True,
        linewidth=1.7,
        edgecolor=edgecolor,
        facecolor=facecolor,
        joinstyle="round",
    )
    ax.add_patch(patch)
    ax.text(
        cx,
        cy,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color="#20262d",
        linespacing=1.16,
    )
    return patch


def add_arrow(ax, start, end, *, color=None, rad=0.0, lw=1.7):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=15,
        linewidth=lw,
        color=color or COLORS["line"],
        shrinkA=4,
        shrinkB=4,
        connectionstyle=f"arc3,rad={rad}",
    )
    ax.add_patch(arrow)
    return arrow


def save(fig, filename: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / filename, dpi=160, bbox_inches="tight")
    plt.close(fig)


def design_map() -> None:
    fig, ax = plt.subplots(figsize=(12.6, 7.2))
    ax.set_xlim(0, 12.6)
    ax.set_ylim(0, 7.6)
    ax.axis("off")

    ax.text(
        6.3,
        7.35,
        "Mapa de decisión MIMO: del problema de red a la estrategia",
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color="#20262d",
    )
    ax.text(
        6.3,
        7.0,
        "La misma matriz de antenas se usa distinto según cobertura, capacidad, interferencia y CSI.",
        ha="center",
        va="center",
        fontsize=10.5,
        color="#4f5b66",
    )

    columns = [
        (0.35, "Síntoma de red", COLORS["blue"]),
        (4.35, "Estrategia MIMO", COLORS["green"]),
        (8.35, "Costo que vigilar", COLORS["orange"]),
    ]
    for x, title, color in columns:
        add_box(
            ax,
            x,
            6.35,
            3.35,
            0.42,
            title,
            facecolor=color,
            edgecolor=color,
            fontsize=10.2,
            weight="bold",
            textcolor="white",
            radius=0.05,
        )

    rows = [
        (
            "Borde de celda\nSNR baja, BLER alto",
            "Rank 1\nbeamforming / diversidad",
            "No subir capas\nantes de cerrar enlace",
            "#e8f1fb",
            "#e8f5ea",
            "#fff3e5",
        ),
        (
            "Hotspot urbano\nmuchos UEs",
            "MU-MIMO\nRZF/ZF + scheduler",
            "CSI fresco\ncanales separables",
            "#fbeaea",
            "#eef7f5",
            "#fff3e5",
        ),
        (
            "Indoor / small cell\ncanal rico",
            "SU-MIMO\nrank 2/4",
            "Correlación de antenas\ny orientación del UE",
            "#eaf7f0",
            "#eaf2fb",
            "#fff3e5",
        ),
        (
            "Massive sub-6\nM >> K",
            "TDD\nMRT/RZF con scheduler",
            "Pilotos, reciprocidad\ny contaminación",
            "#f0edf8",
            "#eef7f5",
            "#fff3e5",
        ),
        (
            "FR2 / mmWave\npath loss alto",
            "Array grande\nbeamforming híbrido",
            "Bloqueo, beams\ny RF chains",
            "#fff2df",
            "#eaf2fb",
            "#fff3e5",
        ),
    ]

    y_positions = [5.55, 4.55, 3.55, 2.55, 1.55]
    for y, (symptom, strategy, cost, c1, c2, c3) in zip(y_positions, rows):
        ax.plot([0.35, 11.7], [y - 0.13, y - 0.13], color="#dde3ea", lw=0.8, zorder=0)
        add_box(ax, 0.35, y, 3.35, 0.66, symptom, facecolor=c1, edgecolor="#b7cfe7", fontsize=9.1)
        add_box(ax, 4.35, y, 3.35, 0.66, strategy, facecolor=c2, edgecolor="#b9d8c2", fontsize=9.1)
        add_box(ax, 8.35, y, 3.35, 0.66, cost, facecolor=c3, edgecolor="#e8c08d", fontsize=9.0)
        add_arrow(ax, (3.72, y + 0.33), (4.32, y + 0.33), color="#8b98a6", lw=1.4)
        add_arrow(ax, (7.72, y + 0.33), (8.32, y + 0.33), color="#8b98a6", lw=1.4)

    ax.text(
        6.3,
        0.75,
        "Lectura operativa: primero identificar el síntoma; luego gastar los grados de libertad espaciales donde más ayudan.",
        ha="center",
        va="center",
        fontsize=10.2,
        color="#4f5b66",
    )

    save(fig, "mimo-design-map.png")


def rank_precoder_flow() -> None:
    fig, ax = plt.subplots(figsize=(12.2, 7.4))
    ax.set_xlim(0, 12.2)
    ax.set_ylim(0, 8.4)
    ax.axis("off")

    ax.text(
        6.1,
        8.05,
        "Flujo de decisión: rank, capas y precoder",
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color="#20262d",
    )
    ax.text(
        6.1,
        7.68,
        "La adaptación usa mediciones de enlace y canal; no basta contar antenas disponibles.",
        ha="center",
        va="center",
        fontsize=10.5,
        color="#4f5b66",
    )

    add_box(
        ax,
        4.55,
        6.95,
        3.1,
        0.55,
        "Medir H, SNR,\nBLER, CQI/RI/PMI",
        facecolor="#eaf2fb",
        edgecolor="#9bbfdf",
        fontsize=9.6,
        weight="bold",
    )
    add_diamond(
        ax,
        6.1,
        5.95,
        3.3,
        0.95,
        "¿El enlace cierra\ncon BLER objetivo?",
        facecolor="#fff3e5",
        edgecolor="#e8b66f",
    )
    add_box(
        ax,
        0.75,
        4.95,
        3.35,
        0.82,
        "Rank 1\nbeamforming / diversidad\nMRT si hay CSIT",
        facecolor="#e8f1fb",
        edgecolor="#9bbfdf",
        fontsize=9.2,
    )
    add_diamond(
        ax,
        6.1,
        4.55,
        3.45,
        1.02,
        "¿rank efectivo > 1\ny $\\sigma_2$ no es débil?",
        facecolor="#eaf7f0",
        edgecolor="#9ed0a8",
    )
    add_box(
        ax,
        8.45,
        4.45,
        3.15,
        0.8,
        "Mantener rank bajo\n+ codificación robusta",
        facecolor="#f5f0fb",
        edgecolor="#c7b3de",
        fontsize=9.2,
    )
    add_diamond(
        ax,
        6.1,
        3.08,
        3.3,
        0.95,
        "¿Interferencia domina\nal ruido?",
        facecolor="#fff3e5",
        edgecolor="#e8b66f",
    )
    add_box(
        ax,
        1.2,
        1.8,
        3.45,
        0.82,
        "RZF/ZF\nsi canales son separables\ny M >= K",
        facecolor="#fbeaea",
        edgecolor="#e3aaa7",
        fontsize=9.1,
    )
    add_box(
        ax,
        7.55,
        1.8,
        3.45,
        0.82,
        "MMSE/MRT o SU-MIMO\nrank alto si SNR y modos\nlo permiten",
        facecolor="#eaf2fb",
        edgecolor="#9bbfdf",
        fontsize=9.1,
    )
    add_box(
        ax,
        4.05,
        0.55,
        4.1,
        0.62,
        "Verificar BLER y throughput; actualizar scheduler",
        facecolor=COLORS["light_gray"],
        edgecolor="#c8d0d8",
        fontsize=9.3,
        weight="bold",
    )

    add_arrow(ax, (6.1, 6.92), (6.1, 6.42))
    add_arrow(ax, (5.0, 5.95), (4.08, 5.36), rad=0.05)
    add_arrow(ax, (6.1, 5.47), (6.1, 5.08))
    add_arrow(ax, (7.35, 4.55), (8.43, 4.86), rad=-0.05)
    add_arrow(ax, (6.1, 4.04), (6.1, 3.56))
    add_arrow(ax, (4.85, 3.08), (4.02, 2.62), rad=0.02)
    add_arrow(ax, (7.35, 3.08), (7.92, 2.62), rad=-0.02)
    add_arrow(ax, (2.42, 4.93), (4.35, 1.16), rad=0.16, color="#8b98a6", lw=1.25)
    add_arrow(ax, (9.95, 4.43), (7.72, 1.16), rad=-0.13, color="#8b98a6", lw=1.25)
    add_arrow(ax, (2.92, 1.78), (4.23, 1.07), rad=-0.05, color="#8b98a6", lw=1.25)
    add_arrow(ax, (9.28, 1.78), (7.95, 1.07), rad=0.05, color="#8b98a6", lw=1.25)

    ax.text(4.58, 5.72, "no", color=COLORS["red"], fontsize=9.2, fontweight="bold")
    ax.text(6.32, 5.32, "sí", color=COLORS["green"], fontsize=9.2, fontweight="bold")
    ax.text(7.85, 4.92, "no", color=COLORS["red"], fontsize=9.2, fontweight="bold")
    ax.text(6.32, 3.86, "sí", color=COLORS["green"], fontsize=9.2, fontweight="bold")
    ax.text(4.55, 2.86, "sí", color=COLORS["green"], fontsize=9.2, fontweight="bold")
    ax.text(7.48, 2.86, "no", color=COLORS["red"], fontsize=9.2, fontweight="bold")

    save(fig, "mimo-rank-precoder-flow.png")


def csi_overhead() -> None:
    fig, ax = plt.subplots(figsize=(9.6, 5.6))

    m_antennas = np.array([8, 16, 32, 64, 128, 256])
    k_users = 8
    fdd = m_antennas
    tdd = np.full_like(m_antennas, k_users)

    ax.axvspan(64, 256, color="#f0f3f6", zorder=0)
    ax.plot(
        m_antennas,
        fdd,
        marker="o",
        linewidth=2.5,
        color=COLORS["red"],
        label="FDD: CSI DL y feedback crecen con M",
    )
    ax.plot(
        m_antennas,
        tdd,
        marker="s",
        linewidth=2.5,
        color=COLORS["blue"],
        label="TDD: pilotos UL crecen con K",
    )

    ax.set_title("Sobrecarga de CSI: por qué Massive MIMO prefiere TDD", pad=16, weight="bold")
    ax.set_xlabel("Antenas en estación base, M")
    ax.set_ylabel("Sobrecarga relativa por intervalo de coherencia")
    ax.set_xlim(6, 264)
    ax.set_ylim(0, 280)
    ax.set_xticks(m_antennas)
    ax.grid(True, color="#d7dde4", linewidth=0.8, alpha=0.8)
    ax.legend(loc="upper left", frameon=True, framealpha=0.95)

    ax.text(
        154,
        248,
        "régimen Massive MIMO\nM >> K",
        ha="center",
        va="center",
        fontsize=10,
        color="#4f5b66",
    )
    ax.annotate(
        "FDD escala con antenas:\ncanal DL grande que reportar",
        xy=(128, 128),
        xytext=(82, 186),
        arrowprops=dict(arrowstyle="-|>", color=COLORS["red"], lw=1.3),
        fontsize=9.5,
        color="#20262d",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#e3aaa7"),
    )
    ax.annotate(
        "TDD escala con usuarios:\nK pilotos UL",
        xy=(128, k_users),
        xytext=(140, 58),
        arrowprops=dict(arrowstyle="-|>", color=COLORS["blue"], lw=1.3),
        fontsize=9.5,
        color="#20262d",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#9bbfdf"),
    )
    ax.text(
        0.01,
        -0.18,
        "Ejemplo normalizado con K = 8 usuarios. En FDD el coste de CSI aumenta con M; en TDD queda fijado por pilotos de usuario.",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=9.2,
        color="#4f5b66",
    )

    fig.tight_layout()
    save(fig, "mimo-csi-overhead.png")


def main() -> None:
    setup_style()
    design_map()
    rank_precoder_flow()
    csi_overhead()


if __name__ == "__main__":
    main()
