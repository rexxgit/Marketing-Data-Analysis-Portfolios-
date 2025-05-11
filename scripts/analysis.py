import matplotlib.pyplot as plt
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

# Generate dates for x-axis
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
dates = [f"{random.choice(months)} {random.randint(1, 28)}" for _ in range(12)]

# Create output directory
output_dir = "output_of_the_analysis"
os.makedirs(output_dir, exist_ok=True)

# Function for recommendations
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

# Create charts with side panel for recommendations
for metric, props in metrics.items():
    values = [round(random.uniform(*props["range"]), 2) for _ in range(12)]
    recommendation = get_recommendation(metric, sum(values) / len(values))

    fig, ax = plt.subplots(figsize=(10, 4))
    plt.subplots_adjust(left=0.3)  # Create space for the recommendation

    if props["plot"] == "line":
        ax.plot(dates, values, marker='o', linestyle='-', color='steelblue')
    elif props["plot"] == "bar":
        ax.bar(dates, values, color='coral')
    elif props["plot"] == "hbar":
        ax.barh(dates, values, color='mediumseagreen')
        ax.set_xlabel("Value")
        ax.set_ylabel("Keyword")
        ax.set_title(f"{metric} (Lower is Better)")
        # Add recommendation as text box
        fig.text(0.01, 0.5, f"Recommendation:\n{recommendation}", fontsize=10,
                 va='center', ha='left', bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{metric.replace(' ', '_')}.png")
        plt.close()
        continue

    ax.set_title(f"{metric} Over Time", fontsize=10)
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, linestyle='--', alpha=0.5)

    # Add recommendation as text box in left margin
    fig.text(0.01, 0.5, f"Recommendation:\n{recommendation}", fontsize=10,
             va='center', ha='left', bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

    plt.tight_layout()
    plt.savefig(f"{output_dir}/{metric.replace(' ', '_')}.png")
    plt.close()

"✅ Charts with unique types and side-panel recommendations generated."
