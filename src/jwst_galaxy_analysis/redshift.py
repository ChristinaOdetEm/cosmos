from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.use("Agg")


@dataclass(frozen=True)
class ExponentialFitResult:
    bin_count: int
    value_range: tuple[float, float]
    counts: np.ndarray
    edges: np.ndarray
    centers: np.ndarray
    fitted_counts: np.ndarray
    residuals: np.ndarray
    A: float
    k: float
    r2_count: float
    r2_log: float
    rmse: float

    @property
    def equation(self) -> str:
        return f"count(z) = {self.A:.6f} * exp(-{self.k:.6f} * z)"


def summarize_redshift_series(values: pd.Series) -> dict[str, float]:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    return {
        "count": float(numeric.count()),
        "mean": float(numeric.mean()),
        "median": float(numeric.median()),
        "std": float(numeric.std(ddof=1)),
        "min": float(numeric.min()),
        "max": float(numeric.max()),
    }


def fit_exponential_count_distribution(
    values: pd.Series | np.ndarray,
    *,
    bins: int = 40,
    value_range: tuple[float, float] = (0.0, 20.0),
) -> ExponentialFitResult:
    numeric = pd.to_numeric(pd.Series(values), errors="coerce").dropna().to_numpy()
    counts, edges = np.histogram(numeric, bins=bins, range=value_range)
    centers = 0.5 * (edges[:-1] + edges[1:])
    mask = counts > 0
    fit_x = centers[mask]
    fit_y = counts[mask].astype(float)

    slope, intercept = np.polyfit(fit_x, np.log(fit_y), 1)
    A = float(np.exp(intercept))
    k = float(-slope)
    fitted_counts = A * np.exp(-k * centers)
    fit_prediction = A * np.exp(-k * fit_x)
    residuals = counts - fitted_counts

    count_ss_res = float(np.sum((fit_y - fit_prediction) ** 2))
    count_ss_tot = float(np.sum((fit_y - fit_y.mean()) ** 2))
    log_observed = np.log(fit_y)
    log_predicted = np.log(fit_prediction)
    log_ss_res = float(np.sum((log_observed - log_predicted) ** 2))
    log_ss_tot = float(np.sum((log_observed - log_observed.mean()) ** 2))

    return ExponentialFitResult(
        bin_count=bins,
        value_range=value_range,
        counts=counts,
        edges=edges,
        centers=centers,
        fitted_counts=fitted_counts,
        residuals=residuals,
        A=A,
        k=k,
        r2_count=1.0 - (count_ss_res / count_ss_tot),
        r2_log=1.0 - (log_ss_res / log_ss_tot),
        rmse=float(np.sqrt(np.mean((fit_y - fit_prediction) ** 2))),
    )


def plot_count_histogram(values: pd.Series, *, output_path: Path, title: str, bins: int = 40) -> None:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(numeric, bins=bins, range=(0.0, 20.0), color="#1f77b4", edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel("Redshift")
    ax.set_ylabel("Count")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def plot_normalized_histogram(
    values: pd.Series,
    *,
    output_path: Path,
    title: str,
    bins: int = 40,
) -> None:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(
        numeric,
        bins=bins,
        range=(0.0, 20.0),
        density=True,
        color="#ff7f0e",
        edgecolor="black",
    )
    ax.set_title(title)
    ax.set_xlabel("Redshift")
    ax.set_ylabel("Density")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def plot_fit(result: ExponentialFitResult, *, output_path: Path, title: str) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(result.centers, result.counts, width=result.edges[1] - result.edges[0], color="#9ecae1", edgecolor="black", alpha=0.8, label="Observed")
    ax.plot(result.centers, result.fitted_counts, color="#d62728", linewidth=2, label=result.equation)
    ax.set_title(title)
    ax.set_xlabel("Redshift")
    ax.set_ylabel("Count")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def plot_residuals(result: ExponentialFitResult, *, output_path: Path, title: str) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axhline(0.0, color="black", linewidth=1)
    ax.bar(result.centers, result.residuals, width=result.edges[1] - result.edges[0], color="#2ca02c", edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel("Redshift")
    ax.set_ylabel("Observed - Fitted")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
