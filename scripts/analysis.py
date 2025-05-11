import matplotlib.pyplot as plt
import random
import os

# Define metric names and value ranges
metrics = {
    "Total Visitors": (1000, 10000),
    "Pageviews": (1500, 15000),
    "Bounce Rate": (20, 90),  # %
    "Total Followers Growth": (0, 500),
    "Engagement Rate": (0.5, 10),  # %
    "Open Rate": (10, 60),  # %
    "Click-Through Rate (CTR)": (1, 20),  # %
    "Unsubscribe Rate": (0, 10),  # %
    "Organic Traffic Growth": (-10, 50),  # %
    "Keyword Ranking": (1, 100),
    "Backlink Count": (50, 500),
    "Cost Per Click (CPC)": (0.2, 5),  # $
    "Conversion Rate": (0.5, 15),  # %
    "Return on Ad Spend (ROAS)": (0.5, 10),
    "Customer Lifetime Value (CLV)": (50, 1000),  # $
    "Churn Rate": (1, 30),  # %
    "Average Order Value (AOV)": (20, 200),  # $
}

# Generate data
data = {
    "Metric Name": list(metrics.keys()),
    "Metric Value": [round(random.uniform(*metrics[m]), 2) for m in metrics],
    "Date": [f"{random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])} {random.randint(1, 28)}" for _ in metrics]
}

# Recommendations logic based on calculated values
def get_recommendation(metric, value):
    if metric == "Bounce Rate":
        if value > 60:
            return "High bounce rate. Analyze landing pages and align content with intent."
        else:
            return "Bounce rate is acceptable. Keep optimizing."

    elif metric == "Conversion Rate":
        if value < 3:
            return "Low conversion rate. Review funnel and optimize CTAs."
        else:
            return "Good conversion rate. Scale successful campaigns."

    elif metric == "Open Rate":
        if value < 25:
            return "Improve subject lines or send time to boost email open rates."
        else:
            return "Strong open rate. Continue testing successful elements."

    elif metric == "Click-Through Rate (CTR)":
        if value < 5:
            return "CTR is low. Improve CTAs and email content relevance."
        else:
            return "Great CTR. Keep using effective content and CTAs."

    elif metric == "Churn Rate":
        if value > 10:
            return "High churn. Investigate customer dissatisfaction and improve retention."
        else:
            return "Healthy churn rate. Retention strategies are working."

    elif metric == "Return on Ad Spend (ROAS)":
        if value < 2:
            return "Low ROAS. Review ad creatives and audience targeting."
        else:
            return "Good ROAS. Scale performing campaigns."

    elif metric == "Total Visitors":
        if value < 3000:
            return "Traffic is low. Increase outreach and improve SEO."
        else:
            return "Traffic is strong. Maintain growth momentum."

    elif metric == "Engagement Rate":
        if value < 3:
            return "Low engagement. Try new formats and increase content value."
        else:
            return "Strong engagement. Focus on what's working."

    elif metric == "Unsubscribe Rate":
        if value > 3:
            return "Unsubscribes are high. Provide more relevant content."
        else:
            return "Unsubscribe rate is under control."

    elif metric == "Cost Per Click (CPC)":
        if value > 2.5:
            return "CPC is high. Consider optimizing bidding and keywords."
        else:
            return "CPC is reasonable. Maintain cost efficiency."

    elif metric == "Customer Lifetime Value (CLV)":
        if value < 200:
            return "CLV is low. Enhance retention and upselling strategies."
        else:
            return "Good CLV. Customers are bringing strong value."

    elif metric == "Organic Traffic Growth":
        if value < 5:
            return "Slow organic growth. Refresh SEO content and strategy."
        else:
            return "Good organic growth. Keep content SEO-friendly."

    elif metric == "Keyword Ranking":
        if value > 50:
            return "Keywords ranked low. Improve keyword strategy."
        else:
            return "Keywords performing well. Optimize further."

    elif metric == "Pageviews":
        if value < 4000:
            return "Pageviews are low. Promote pages and improve SEO."
        else:
            return "Good pageviews. Analyze top content and replicate success."

    elif metric == "Backlink Count":
        if value < 150:
            return "Backlinks are low. Reach out for guest posts and PR."
        else:
            return "Solid backlink profile. Continue outreach."

    elif metric == "Total Followers Growth":
        if value < 100:
            return "Follower growth is slow. Increase content consistency."
        else:
            return "Followers growing well. Analyze top campaigns."

    elif metric == "Average Order Value (AOV)":
        if value < 60:
            return "Low AOV. Use bundling or upselling techniques."
        else:
            return "Strong AOV. Promote best-performing products."

    return "No recommendation available."

# Create output directory
output_dir = "output_charts"
os.makedirs(output_dir, exist_ok=True)

# Generate individual charts
for i in range(len(data["Metric Name"])):
    metric = data["Metric Name"][i]
    value = data["Metric Value"][i]
    date = data["Date"][i]
    recommendation = get_recommendation(metric, value)

    # Create figure
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar([metric], [value], color='skyblue')
    ax.set_title(f"{metric} - {date}", fontsize=10)
    ax.set_ylabel("Value")
    ax.set_xticks([])  # Hide x-ticks for clarity

    # Add recommendation as annotation
    ax.annotate(recommendation, xy=(0, value), xytext=(0, value + value*0.1),
                ha='center', fontsize=8, wrap=True, bbox=dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9))

    plt.tight_layout()
    plt.savefig(f"{output_dir}/{metric.replace(' ', '_')}.png")
    plt.close()

print(f"✅ Generated {len(data['Metric Name'])} charts with recommendations in '{output_dir}/'.")
