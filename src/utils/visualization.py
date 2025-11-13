import matplotlib.pyplot as plt
import seaborn as sns


def plot_hist(df, col):
    sns.histplot(df[col], kde=True)
    plt.show()


def plot_box(df, col):
    sns.boxplot(x=df[col])
    plt.show()


def plot_corr(df):
    plt.figure(figsize=(12,6))
    sns.heatmap(df.corr(numeric_only=True), annot=False, cmap="Blues")
    plt.show()
