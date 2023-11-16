#!/usr/local/bin/python
# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
from adjustText import adjust_text


def plot_vs_errorbar(
    x, y, y_avg, y_std, node_label, title, xaxis, yaxis, color="g", save=False
):
    fig = plt.figure()
    plt.plot(x, y, linestyle="--", color="b", marker="d", label=node_label)
    (_, caps, _) = plt.errorbar(
        x, y_avg, y_std, color="g", capsize=5, errorevery=5, label="Node average"
    )
    for cap in caps:
        cap.set_markeredgewidth(1)
    legend = plt.legend(frameon=True)
    legend.get_frame().set_facecolor("white")
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    if save:
        fig.savefig("figures/" + title)
    else:
        plt.show()


def log_binning(x, y, bin_count=10):
    bins = np.logspace(math.log10(1), math.log10(max(x)), num=bin_count)
    deltas = bins[1:] - bins[:-1]

    digitized = np.digitize(x, bins)

    x = np.array(x)
    y = np.array(y)

    bin_medians = np.array([np.median(y[digitized == i]) for i in range(1, len(bins))])

    bins_x = bins[1:] - deltas / 2
    bins_y = bin_medians

    bins_x = bins_x[np.isfinite(bins_y)]
    bins_y = bins_y[np.isfinite(bins_y)]

    return bins_x, bins_y


def plot_oddball_features(x, y, x_fit, y_fit, labels, anomalies, output="nmf results"):
    fig = plt.figure()
    # plt.title('Node vs. Edge Feature')
    plt.xlabel("# Nodes")
    plt.ylabel("# Edges")
    # y_max = 1
    x_max = int(max(x) * 1.2)
    y_max = int(max(y) * 1.2)
    plt.axis([0, x_max, 0, y_max])

    # median_x, median_y = log_binning(x, y, 10)
    # print(median_x, median_y)
    # plt.plot(median_x, median_y, 'ro')

    def func(x, a, b):
        fc = a * (np.array(x).astype(float) ** b)
        return fc

    # popt, pcov = curve_fit(func, median_x, median_y, maxfev=20000)

    # fitline = func(median_x, *popt)

    # plt.plot(median_x, fitline, color='b')

    plt.scatter(x, y, c="c")

    plt.plot(x_fit, y_fit, "r-", color="r")
    # thresholds identifying extremes
    plt.plot(
        [i for i in range(1, x_max)],
        [i - 1 for i in range(1, x_max)],
        linestyle="--",
        color="#000000",
    )
    plt.plot(
        [i for i in range(0, x_max)],
        [i**2 for i in range(0, x_max)],
        linestyle="--",
        color="b",
    )
    ax = plt.gca()

    ax.set_yscale("log")
    ax.set_xscale("log")
    ax.set_ylim(0, y_max)
    ax.set_xlim(0, x_max)

    print(anomalies)

    texts = []
    for label, x, y in list(zip(labels, x, y))[:10]:
        label = label[0:29]
        texts.append(plt.text(x, y, label, fontsize=7))
        # if label == 'kenneth.lay@enron.com':
        # 	texts.append(plt.text(x, y, label))

    adjust_text(texts, arrowprops=dict(arrowstyle="->", color="r", lw=0.5))

    plt.show()
    fig.savefig(output + "NMF")
