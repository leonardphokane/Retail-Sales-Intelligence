# scripts/plot_generator.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_revenue(data, date_col='Date', revenue_col='Revenue'):
    """
    Plots monthly revenue trends.
    Returns the matplotlib figure object.
    """
    df = data.copy()
    df['Month'] = df[date_col].dt.to_period('M').astype(str)
    monthly_rev = df.groupby('Month')[revenue_col].sum().reset_index()

    fig = plt.figure(figsize=(10, 5))
    sns.lineplot(data=monthly_rev, x='Month', y=revenue_col, marker='o', linewidth=2, color='royalblue')
    plt.title('Monthly Revenue Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def plot_revenue_by_region(data, region_col='Region', revenue_col='Revenue'):
    """
    Plots total revenue by region.
    Returns the matplotlib figure object.
    """
    region_rev = data.groupby(region_col)[revenue_col].sum().reset_index()

    fig = plt.figure(figsize=(8, 5))
    sns.barplot(data=region_rev, x=region_col, y=revenue_col, hue=region_col, palette='viridis', legend=False)
    plt.title('Regional Revenue Comparison')
    plt.xlabel('Region')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    return fig

def plot_top_products(data, product_col='Product', revenue_col='Revenue', top_n=5):
    """
    Plots top N products by total revenue.
    Returns the matplotlib figure object.
    """
    product_rev = data.groupby(product_col)[revenue_col].sum().reset_index()
    top_products = product_rev.sort_values(by=revenue_col, ascending=False).head(top_n)

    fig = plt.figure(figsize=(8, 5))
    sns.barplot(data=top_products, x=product_col, y=revenue_col, palette='coolwarm')
    plt.title(f'Top {top_n} Products by Revenue')
    plt.xlabel('Product')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    return fig
