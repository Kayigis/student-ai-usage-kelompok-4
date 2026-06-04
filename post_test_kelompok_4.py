from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "Kelas F_Student AI Usage.csv"
OUTPUT_DIR = BASE_DIR / "hasil_kelompok_4"

NUMERIC_COLUMNS = [
    "age",
    "study_hours_per_day",
    "grades_before_ai",
    "grades_after_ai",
    "daily_screen_time_hours",
]

REQUIRED_COLUMNS = [
    "age",
    "education_level",
    "study_hours_per_day",
    "uses_ai",
    "ai_tools_used",
    "purpose_of_ai",
    "grades_before_ai",
    "grades_after_ai",
    "daily_screen_time_hours",
]


def configure_style():
    sns.set_theme(style="whitegrid")
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans", "Arial", "Liberation Sans", "sans-serif"],
            "figure.facecolor": "#FFFFFF",
            "axes.facecolor": "#FFFFFF",
            "axes.edgecolor": "#CBD5E1",
            "axes.labelcolor": "#334155",
            "axes.titlecolor": "#0F172A",
            "xtick.color": "#334155",
            "ytick.color": "#334155",
            "text.color": "#0F172A",
        }
    )


def save_plot(filename):
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / filename
    plt.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"Grafik disimpan: {path}")


def style_axes(ax):
    ax.grid(axis="y", linestyle="--", linewidth=0.8, alpha=0.5, color="#CBD5E1")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#CBD5E1")
    ax.spines["bottom"].set_color("#CBD5E1")
    ax.tick_params(axis="both", length=0)


def add_bar_labels(ax, bars, suffix="", decimals=1):
    for bar in bars:
        value = bar.get_height()
        label = f"{value:.{decimals}f}{suffix}"
        ax.annotate(
            label,
            xy=(bar.get_x() + bar.get_width() / 2, value),
            xytext=(0, 7),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
            color="#0F172A",
        )


def add_insight(fig, text, y=0.035):
    fig.text(
        0.5,
        y,
        text,
        ha="center",
        va="center",
        fontsize=9.3,
        color="#475569",
        bbox={
            "boxstyle": "round,pad=0.55",
            "facecolor": "#F8FAFC",
            "edgecolor": "#E2E8F0",
        },
    )


def kategori_a(df):
    median_grades = (
        df.groupby("education_level", as_index=False)["grades_before_ai"]
        .median()
        .sort_values("grades_before_ai", ascending=False)
    )

    print("\nKategori A - Median grades_before_ai berdasarkan education_level")
    print(median_grades.to_string(index=False))

    fig, ax = plt.subplots(figsize=(8, 7))
    fig.subplots_adjust(bottom=0.23)

    colors = ["#4F46E5", "#06B6D4"]
    bars = ax.bar(
        median_grades["education_level"].str.capitalize(),
        median_grades["grades_before_ai"],
        color=colors,
        width=0.46,
        edgecolor="none",
        alpha=0.92,
        zorder=3,
    )

    overall_median = df["grades_before_ai"].median()
    ax.axhline(overall_median, color="#64748B", linestyle=":", linewidth=2, zorder=2)
    ax.text(
        1.38,
        overall_median + 1.1,
        f"Median keseluruhan: {overall_median:.1f}",
        ha="right",
        fontsize=9.5,
        fontweight="semibold",
        color="#475569",
    )

    add_bar_labels(ax, bars)
    style_axes(ax)
    ax.set_title("Median Nilai Awal Berdasarkan Jenjang Pendidikan", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Median nilai sebelum AI")
    ax.set_xlabel("")
    ax.set_ylim(0, 78)

    add_insight(
        fig,
        "Insight: Median nilai awal school (64.5) sedikit lebih tinggi dari college (63.0),\n"
        "namun selisihnya kecil sehingga kemampuan awal kedua jenjang relatif seimbang.",
    )
    save_plot("01_kategori_a_median_grades_before.png")


def kategori_b(df):
    filtered = df[
        (df["purpose_of_ai"] == "Homework")
        & (df["study_hours_per_day"] < 2)
    ].copy()
    filtered["student_label"] = [f"Siswa {idx + 1}" for idx in filtered.index]
    filtered["grade_improvement"] = filtered["grades_after_ai"] - filtered["grades_before_ai"]

    print("\nKategori B - Siswa purpose_of_ai Homework dan study_hours_per_day < 2")
    columns = [
        "student_label",
        "age",
        "education_level",
        "ai_tools_used",
        "study_hours_per_day",
        "grades_before_ai",
        "grades_after_ai",
        "grade_improvement",
    ]
    print(filtered[columns].to_string(index=False) if not filtered.empty else "Tidak ada data")

    fig, ax = plt.subplots(figsize=(11, 7.5))
    fig.subplots_adjust(bottom=0.31)

    if filtered.empty:
        ax.text(0.5, 0.5, "Tidak ada data yang memenuhi filter", ha="center", va="center", fontsize=12)
        ax.axis("off")
    else:
        tool_colors = {
            "ChatGPT": "#10A37F",
            "Gemini": "#1A73E8",
            "Copilot": "#F97316",
        }
        colors = [tool_colors.get(tool, "#64748B") for tool in filtered["ai_tools_used"]]
        x_pos = np.arange(len(filtered))
        bars = ax.bar(
            x_pos,
            filtered["study_hours_per_day"],
            color=colors,
            width=0.52,
            edgecolor="none",
            alpha=0.92,
            zorder=3,
        )

        ax.axhline(2.0, color="#EF4444", linestyle="--", linewidth=1.7, zorder=2)
        ax.text(len(filtered) - 0.55, 2.07, "Batas 2 jam", ha="right", fontsize=9.5, fontweight="bold", color="#EF4444")

        add_bar_labels(ax, bars, suffix=" jam")
        style_axes(ax)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(filtered["student_label"], fontsize=10, fontweight="semibold")

        for i, (_, row) in enumerate(filtered.iterrows()):
            ax.text(
                i,
                -0.20,
                f"{row['education_level'].capitalize()}, {row['age']} tahun\n"
                f"Nilai: {row['grades_before_ai']}->{row['grades_after_ai']} (+{row['grade_improvement']})\n"
                f"AI: {row['ai_tools_used']}",
                ha="center",
                va="top",
                fontsize=8.3,
                color="#475569",
                transform=ax.get_xaxis_transform(),
            )

        from matplotlib.patches import Patch

        legend_elements = [Patch(facecolor=color, label=tool) for tool, color in tool_colors.items()]
        ax.legend(handles=legend_elements, title="Alat AI", loc="upper right", frameon=True)
        ax.set_title("Pengguna AI untuk Homework dengan Waktu Belajar < 2 Jam", fontsize=14, fontweight="bold", pad=15)
        ax.set_ylabel("Jam belajar per hari")
        ax.set_xlabel("")
        ax.set_ylim(0, 2.6)

        avg_improvement = filtered["grade_improvement"].mean()
        add_insight(
            fig,
            f"Insight: Ada {len(filtered)} siswa yang belajar < 2 jam/hari untuk homework berbantuan AI.\n"
            f"Semua mengalami kenaikan nilai, dengan rata-rata peningkatan {avg_improvement:.1f} poin.",
        )

    save_plot("02_kategori_b_homework_under_2_hours.png")


def kategori_c(df):
    renamed = df[NUMERIC_COLUMNS].copy()
    renamed.columns = [
        "Umur\n(Age)",
        "Jam Belajar\n(Study Hours)",
        "Nilai Pre-AI\n(Before)",
        "Nilai Post-AI\n(After)",
        "Screen Time\n(Daily)",
    ]
    corr_matrix = renamed.corr()

    print("\nKategori C - Matriks korelasi kolom numerik")
    print(corr_matrix.round(3).to_string())

    fig, ax = plt.subplots(figsize=(10, 9))
    fig.subplots_adjust(bottom=0.2)

    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    cmap = sns.diverging_palette(240, 15, s=85, l=50, sep=10, as_cmap=True)
    sns.heatmap(
        corr_matrix,
        mask=mask,
        cmap=cmap,
        vmin=-1,
        vmax=1,
        annot=True,
        fmt=".2f",
        square=True,
        linewidths=2,
        linecolor="white",
        cbar_kws={"shrink": 0.75, "label": "Koefisien korelasi (r)"},
        annot_kws={"size": 12, "weight": "bold"},
        ax=ax,
    )
    ax.set_title("Matriks Korelasi Kolom Numerik", fontsize=14, fontweight="bold", pad=15)
    ax.tick_params(axis="both", length=0)
    plt.xticks(rotation=25, ha="right", fontweight="semibold")
    plt.yticks(rotation=0, fontweight="semibold")

    add_insight(
        fig,
        "Insight: Korelasi positif terkuat muncul antara nilai Pre-AI dan Post-AI (r=0.76).\n"
        "Screen time dan durasi belajar terlihat memiliki korelasi lebih lemah terhadap nilai akademik.",
    )
    save_plot("03_kategori_c_correlation_heatmap.png")


def kategori_d(df):
    print("\nKategori D - Distribusi umur siswa")
    print(df["age"].describe().to_string())

    age_counts = df["age"].value_counts().sort_index()
    ages = age_counts.index.to_numpy()
    counts = age_counts.values
    peak_index = int(np.argmax(counts))

    fig, ax = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(bottom=0.22)

    colors = ["#6366F1" if i != peak_index else "#EF4444" for i in range(len(ages))]
    bars = ax.bar(ages, counts, color=colors, width=0.68, edgecolor="none", alpha=0.9, zorder=3)

    add_bar_labels(ax, bars, suffix=" siswa", decimals=0)
    style_axes(ax)
    ax.set_xticks(ages)
    ax.set_xticklabels([f"{age} tahun" for age in ages], fontweight="semibold")
    ax.set_title("Distribusi Umur Siswa Responden", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Jumlah siswa")
    ax.set_xlabel("")
    ax.set_ylim(0, max(counts) + 7)

    peak_age = int(ages[peak_index])
    peak_count = int(counts[peak_index])
    peak_bar = bars[peak_index]
    ax.annotate(
        "Puncak data",
        xy=(peak_bar.get_x() + peak_bar.get_width() / 2, peak_count),
        xytext=(30, 22),
        textcoords="offset points",
        ha="left",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color="#EF4444",
        arrowprops={"arrowstyle": "->", "color": "#EF4444", "lw": 1.5},
    )

    add_insight(
        fig,
        f"Insight: Responden berada pada rentang usia {int(df['age'].min())}-{int(df['age'].max())} tahun.\n"
        f"Usia terbanyak adalah {peak_age} tahun dengan {peak_count} siswa, menunjukkan dominasi pelajar muda.",
    )
    save_plot("04_kategori_d_age_distribution.png")


def load_dataset():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Dataset tidak ditemukan: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Kolom wajib tidak ditemukan: {', '.join(missing_columns)}")
    return df


def main():
    configure_style()
    df = load_dataset()

    print(f"Dataset: {CSV_PATH}")
    print(f"Jumlah data: {len(df)} baris")
    print(f"Kolom: {', '.join(df.columns)}")

    kategori_a(df)
    kategori_b(df)
    kategori_c(df)
    kategori_d(df)

    print("\nSelesai. Semua grafik ada di folder hasil_kelompok_4.")


if __name__ == "__main__":
    main()
