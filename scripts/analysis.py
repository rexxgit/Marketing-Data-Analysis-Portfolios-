import matplotlib.pyplot as plt
import random
import os

# Set number of data points per metric
data_points = 12

# Metric definitions: name and value range
metrics = {
    "Total Visitors": (1000, 10000),
    "Pageviews": (1500, 15000),
    "Bounce Rate": (20, 90),
    "Total Followers Growth": (0, 500),
    "Engagement Rate": (0.5, 10),
    "Open Rate": (10, 60),
    "Click-Through Rate (CTR)": (1, 20),
    "Unsubscribe Rate": (0, 10),
    "Organic Traffic Growth": (-10, 50),
    "Keyword Ranking": (1, 100),
    "Backlink Count": (50, 500),
    "Cost Per Click (CPC)": (0.2, 5),
    "Conversion Rate": (0.5, 15),
    "Return on Ad Spend (ROAS)": (0.5, 10),
    "Customer Lifetime Value (CLV)": (50, 1000),
    "Churn Rate": (1, 30),
    "Average Order Value (AOV)": (20, 200),
}

# Generate random dates like "May 1", "May 4"
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
dates = [f"{random.choice(months)} {random.randint(1, 28)}" for _ in range(data_points)]

# Create output directory
output_dir = "output_of_the_analysis"
os.makedirs(output_dir, exist_ok=True)

# Recommendation function (same as previous version)
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
    return ""

# Plot for each metric
for metric, value_range in metrics.items():
    y_values = [round(random.uniform(*value_range), 2) for _ in range(data_points)]
    recommendation = get_recommendation(metric, sum(y_values) / data_points)

    # Create plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dates, y_values, marker='o', linestyle='-', color='teal')

    # Label highest point with recommendation
    max_index = y_values.index(max(y_values))
    ax.annotate(recommendation,
                xy=(dates[max_index], y_values[max_index]),
                xytext=(dates[max_index], y_values[max_index] + (max(y_values) * 0.1)),
                ha='center',
                fontsize=8,
                bbox=dict(boxstyle="round", fc="wheat", alpha=0.8))

    ax.set_title(f"{metric} Over Time", fontsize=10)
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    plt.xticks(rotation=45, fontsize=7)
    plt.tight_layout()
    plt.grid(True, linestyle="--", alpha=0.3)

    # Save chart
    filename = f"{output_dir}/{metric.replace(' ', '_')}.png"
    plt.savefig(filename)
    plt.close()

print(f"✅ Generated {len(metrics)} charts with time-based x-axis and metric values.")
