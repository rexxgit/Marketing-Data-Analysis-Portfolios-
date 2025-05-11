import os
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime

# Create the 'output_of_the_analysis' folder if it doesn't exist
output_folder = 'output_of_the_analysis'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the metrics with their associated data
data = {
    "Metric Name": [
        "Total Visitors", "Pageviews", "Bounce Rate",
        "Total Followers Growth", "Engagement Rate (Likes, Comments, Shares)",
        "Open Rate", "Click-Through Rate (CTR)", "Unsubscribe Rate",
        "Organic Traffic Growth", "Keyword Ranking Changes", "Backlink Count",
        "Cost Per Click (CPC)", "Conversion Rate", "Return on Ad Spend (ROAS)",
        "Customer Lifetime Value (CLV)", "Churn Rate", "Average Order Value (AOV)"
    ],
    "Metric Value": [
        random.randint(2000, 50000), random.randint(5000, 100000), random.uniform(30.0, 70.0),
        random.randint(1000, 50000), random.uniform(1.0, 10.0),
        random.uniform(10.0, 30.0), random.uniform(2.0, 10.0), random.uniform(0.5, 5.0),
        random.uniform(5.0, 20.0), random.randint(1, 100), random.randint(100, 2000),
        random.uniform(0.5, 5.0), random.uniform(1.0, 10.0), random.uniform(1.5, 5.0),
        random.uniform(100, 1000), random.uniform(2.0, 10.0), random.uniform(20.0, 150.0)
    ],
    "Date": []
}

# Generate random dates for 12 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for month in months:
    days_in_month = random.sample(range(1, 32), random.randint(5, 10))  # Random days for each month
    for day in days_in_month:
        data['Date'].append(f"{month} {day}")

# Adjust the length of the 'Date' list to match the number of metrics
metric_count = len(data["Metric Name"])
assert len(data['Date']) == metric_count, "Date list length doesn't match metric count."

# Create DataFrame
df = pd.DataFrame(data)

# Function to generate dynamic suggestions based on the metric values
def get_dynamic_suggestion(metric_name, metric_value):
    suggestions = {
        # Website & Traffic Analytics
        "Total Visitors": "Monitor the trend of unique visitors month over month. If you're seeing a consistent increase, consider investing more in marketing efforts to capitalize on that growth.",
        "Pageviews": "Identify pages with high traffic and optimize them for conversions. If certain pages are underperforming, consider improving content or SEO.",
        "Bounce Rate": "A high bounce rate indicates that visitors are not finding what they expect. Analyze the content on landing pages to ensure it aligns with their search intent.",
        
        # Social Media Metrics
        "Total Followers Growth": "If follower growth is stagnating, consider collaborations or new strategies to boost organic reach.",
        "Engagement Rate (Likes, Comments, Shares)": "High engagement suggests that your content resonates well with the audience. Focus on replicating these successful tactics.",
        
        # Email Marketing Metrics
        "Open Rate": "If your open rates are low, test new subject lines and send times. Segment your audience better for more personalized content.",
        "Click-Through Rate (CTR)": "Low CTR may suggest the need for more compelling calls to action or better-targeted email campaigns.",
        "Unsubscribe Rate": "A high unsubscribe rate could indicate dissatisfaction with the content you're sending. Consider adjusting the frequency or relevance of emails.",
        
        # SEO Metrics
        "Organic Traffic Growth": "An increase in organic traffic is a positive sign. Invest more in SEO efforts to continue this growth.",
        "Keyword Ranking Changes": "Focus on improving rankings for keywords that are slipping. Optimize your content around these keywords.",
        "Backlink Count": "A growing backlink count is a sign that your content is gaining credibility. Pursue more outreach for additional backlinks.",
        
        # Paid Advertising Metrics
        "Cost Per Click (CPC)": "A high CPC might indicate that your bids are too high. Consider adjusting your bids and targeting to reduce costs.",
        "Conversion Rate": "If conversion rates are low, revisit your landing page, ad copy, or offer to increase conversion rates.",
        "Return on Ad Spend (ROAS)": "A high ROAS indicates successful campaigns. Increase your budget allocation to campaigns with a high ROAS.",
        
        # Customer Retention & Revenue Metrics
        "Customer Lifetime Value (CLV)": "An increasing CLV suggests effective customer retention. Focus on upselling and cross-selling to further increase this metric.",
        "Churn Rate": "If your churn rate is rising, consider improving customer support, loyalty programs, or reducing product dissatisfaction.",
        "Average Order Value (AOV)": "Increasing AOV is a good sign. Upsell and cross-sell products to further boost this metric."
    }

    # Example of recommendations based on metric value
    if metric_value < 20:
        return "Consider increasing efforts in this area, as this is below expected performance."
    elif metric_value > 50:
        return "Excellent performance. Maintain your current strategy to continue this success."
    else:
        return suggestions.get(metric_name, "Monitor this metric and make adjustments as needed.")

# Function to plot metrics with recommendations
def plot_metrics_with_recommendations():
    plt.figure(figsize=(10, 6))
    
    for index, row in df.iterrows():
        metric_name = row["Metric Name"]
        metric_value = row["Metric Value"]
        date = row["Date"]
        suggestion = get_dynamic_suggestion(metric_name, metric_value)

        # Use scatter plot for each metric value over the date range
        plt.scatter([date], [metric_value], label=metric_name)
        
        # Add recommendation text on the chart, avoiding overlap
        plt.text(date, metric_value + 0.5, suggestion, ha='center', va='bottom', fontsize=10, wrap=True)

    plt.title("Metrics Overview with Recommendations")
    plt.xlabel("Date")
    plt.ylabel("Metric Value")
    
    # Rotate x-axis labels for clarity
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig(f"{output_folder}/metrics_overview_with_recommendations.png")
    plt.show()

# Plot the metrics with recommendations
plot_metrics_with_recommendations()
