import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import random
import os

# Define metrics with their value ranges and preferred plot types
metrics = {
    "Total Visitors": {"range": (1000, 10000), "plot": "line"},
    "Pageviews": {"range": (1500, 15000), "plot": "bar"},
    "Bounce Rate": {"range": (20, 90), "plot": "bar"},
    "Total Followers Growth": {"range": (0, 500), "plot": "line"},
    "Engagement Rate": {"range": (0.5, 10), "plot": "bar"},
    "Open Rate": {"range": (10, 60), "plot": "line"},
    "Click-Through Rate (CTR)": {"range": (1, 20), "plot": "line"},
    "Unsubscribe Rate": {"range": (0, 10), "plot": "bar"},
    "Organic Traffic Growth": {"range": (-10, 50), "plot": "line"},
    "Keyword Ranking": {"range": (1, 100), "plot": "hbar"},
    "Backlink Count": {"range": (50, 500), "plot": "bar"},
    "Cost Per Click (CPC)": {"range": (0.2, 5), "plot": "bar"},
    "Conversion Rate": {"range": (0.5, 15), "plot": "bar"},
    "Return on Ad Spend (ROAS)": {"range": (0.5, 10), "plot": "bar"},
    "Customer Lifetime Value (CLV)": {"range": (50, 1000), "plot": "bar"},
    "Churn Rate": {"range": (1, 30), "plot": "line"},
    "Average Order Value (AOV)": {"range": (20, 200), "plot": "bar"},
}

# Color palette (unique colors)
color_palette = [
    "steelblue", "coral", "mediumseagreen", "orchid", "goldenrod",
    "slateblue", "crimson", "teal", "darkorange", "dodgerblue",
    "darkgreen", "hotpink", "mediumpurple", "tomato", "skyblue",
    "olive", "firebrick"
]

# Dates and keyword labels
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
dates = [f"{random.choice(months)} {random.randint(1, 28)}" for _ in range(12)]
sample_keywords = [f"Keyword {i+1}" for i in range(12)]

# Output directory
output_dir = "output_of_the_analysis"
os.makedirs(output_dir, exist_ok=True)

# Recommendation logic
def get_recommendation(metric, value):
    if metric == "Bounce Rate":
        return "High bounce rate" if value > 60 else "Acceptable bounce rate"
    elif metric == "Conversion Rate":
        return "Optimize funnel" if value < 3 else "Good conversions"
    elif metric == "Open Rate":
        return "Improve subject lines" if value < 25 else "Strong open rate"
    elif metric == "Click-Through Rate (CTR)":
        return "Improve CTAs" if value < 5 else "Good CTR"
    elif metric == "Churn Rate":
        return "Reduce churn" if value > 10 else "Healthy churn"
    elif metric == "ROAS":
        return "Low ROAS, review ads" if value < 2 else "Profitable ROAS"
    elif metric == "Total Visitors":
        return "Boost traffic" if value < 3000 else "Strong traffic"
    elif metric == "Engagement Rate":
        return "Increase content value" if value < 3 else "Great engagement"
    elif metric == "Unsubscribe Rate":
        return "Reduce unsubscribes" if value > 3 else "Low unsub rate"
    elif metric == "Cost Per Click (CPC)":
        return "Lower CPC needed" if value > 2.5 else "Efficient CPC"
    elif metric == "CLV":
        return "Increase CLV" if value < 200 else "High value customers"
    elif metric == "Organic Traffic Growth":
        return "Improve SEO content" if value < 5 else "Good organic growth"
    elif metric == "Keyword Ranking":
        return "Improve ranking" if value > 50 else "Good keyword performance"
    elif metric == "Pageviews":
        return "Increase visibility" if value < 4000 else "Great reach"
    elif metric == "Backlink Count":
        return "Build more links" if value < 150 else "Strong backlink profile"
    elif metric == "Total Followers Growth":
        return "Boost follower growth" if value < 100 else "Steady growth"
    elif metric == "AOV":
        return "Upsell more" if value < 60 else "High AOV"
    return "No recommendation"

# Plotting function with side recommendation
def plot_metric_with_recommendation(dates_or_labels, values, title, ylabel, recommendation, chart_type='line', color='blue'):
    fig = plt.figure(figsize=(12, 5))
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 3], wspace=0.05)

    # Left panel for recommendation
    ax0 = fig.add_subplot(gs[0])
    ax0.axis("off")
    ax0.text(0, 0.5, f"Recommendation:\n{recommendation}", fontsize=10, wrap=True, verticalalignment='center')

    # Right panel for chart
    ax1 = fig.add_subplot(gs[1])
    if chart_type == 'line':
        ax1.plot(dates_or_labels, values, marker='o', color=color)
    elif chart_type == 'bar':
        ax1.bar(dates_or_labels, values, color=color)
    elif chart_type == 'scatter':
        ax1.scatter(dates_or_labels, values, color=color)
    elif chart_type == 'hbar':
        sorted_pairs = sorted(zip(values, dates_or_labels))  # Sort for better clarity
        sorted_values, sorted_labels = zip(*sorted_pairs)
        ax1.barh(sorted_labels, sorted_values, color=color)
        ax1.set_xlabel("Ranking")
        ax1.set_ylabel("Keyword")
        ax1.set_title(title + " (Lower is Better)")

    if chart_type != 'hbar':
        ax1.set_title(title)
        ax1.set_ylabel(ylabel)
        ax1.set_xlabel("Date")
        ax1.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    filename = f"{output_dir}/{title.replace(' ', '_')}.png"
    plt.savefig(filename)
    plt.close()

# Loop through and generate all charts
for idx, (metric, props) in enumerate(metrics.items()):
    values = [round(random.uniform(*props["range"]), 2) for _ in range(12)]
    avg_value = sum(values) / len(values)
    recommendation = get_recommendation(metric, avg_value)
    color = color_palette[idx % len(color_palette)]

    if props["plot"] == "hbar":
        plot_metric_with_recommendation(
            sample_keywords, values, metric, "Value", recommendation, chart_type='hbar', color=color
        )
    else:
        plot_metric_with_recommendation(
            dates, values, f"{metric} Over Time", "Value", recommendation, chart_type=props["plot"], color=color
        )

print("✅ Charts generated with unique colors and side-panel recommendations.")
