import os
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime

# Create the 'output_of_the_analysis' folder if it doesn't exist
output_folder = 'output_of_the_analysis'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Current date for referencing when the metrics were recorded
current_date = datetime.now().strftime('%Y-%m-%d')

# Define the metrics with their associated data (unique data for each metric)
data = {
    "Metric Name": [
        # Website & Traffic Analytics
        "Total Visitors", "Pageviews", "Bounce Rate",
        # Social Media Metrics
        "Total Followers Growth", "Engagement Rate (Likes, Comments, Shares)",
        # Email Marketing Metrics
        "Open Rate", "Click-Through Rate (CTR)", "Unsubscribe Rate",
        # SEO Metrics
        "Organic Traffic Growth", "Keyword Ranking Changes", "Backlink Count",
        # Paid Advertising Metrics
        "Cost Per Click (CPC)", "Conversion Rate", "Return on Ad Spend (ROAS)",
        # Customer Retention & Revenue Metrics
        "Customer Lifetime Value (CLV)", "Churn Rate", "Average Order Value (AOV)"
    ],
    "Metric Value": [
        # Website & Traffic Analytics
        random.randint(2000, 50000), random.randint(5000, 100000), random.uniform(30.0, 70.0),
        # Social Media Metrics
        random.randint(1000, 50000), random.uniform(1.0, 10.0),
        # Email Marketing Metrics
        random.uniform(10.0, 30.0), random.uniform(2.0, 10.0), random.uniform(0.5, 5.0),
        # SEO Metrics
        random.uniform(5.0, 20.0), random.randint(1, 100), random.randint(100, 2000),
        # Paid Advertising Metrics
        random.uniform(0.5, 5.0), random.uniform(1.0, 10.0), random.uniform(1.5, 5.0),
        # Customer Retention & Revenue Metrics
        random.uniform(100, 1000), random.uniform(2.0, 10.0), random.uniform(20.0, 150.0)
    ],
    # Correct the length of the "Date" list to match the length of the other lists (17 metrics)
    "Date": [current_date] * 17  # Now 17 dates for 17 metrics
}

# Check lengths of lists before proceeding
print(f"Length of 'Metric Name' list: {len(data['Metric Name'])}")
print(f"Length of 'Metric Value' list: {len(data['Metric Value'])}")
print(f"Length of 'Date' list: {len(data['Date'])}")

# Check if the lengths of lists match
metric_count = len(data["Metric Name"])
assert len(data["Metric Value"]) == metric_count, "The length of 'Metric Value' list doesn't match 'Metric Name'."
assert len(data["Date"]) == metric_count, "The length of 'Date' list doesn't match 'Metric Name'."

# Create DataFrame from the data
df = pd.DataFrame(data)

# Display the DataFrame to check
print("\nDataFrame:\n")
print(df)

# Function to generate dynamic suggestions based on the metric values
def get_dynamic_suggestion(metric_name, metric_value):
    suggestions = {
        # Website & Traffic Analytics
        "Total Visitors": f"Total Visitors: {metric_value}. Great! Focus on improving conversion rates for more qualified traffic.",
        "Pageviews": f"Pageviews: {metric_value}. Strong engagement! Try improving internal linking to boost further exploration.",
        "Bounce Rate": f"Bounce Rate: {metric_value}%. It's high. Consider improving landing page design and load speed.",
        
        # Social Media Metrics
        "Total Followers Growth": f"Followers Growth: {metric_value}. Well done! Engage more with followers to further increase growth.",
        "Engagement Rate (Likes, Comments, Shares)": f"Engagement Rate: {metric_value}%. Great interaction! Keep posting valuable content to maintain momentum.",
        
        # Email Marketing Metrics
        "Open Rate": f"Open Rate: {metric_value}%. Excellent! Experiment with subject lines and time of sending for more engagement.",
        "Click-Through Rate (CTR)": f"Click-Through Rate: {metric_value}%. Keep optimizing your CTAs and email content to increase clicks.",
        "Unsubscribe Rate": f"Unsubscribe Rate: {metric_value}%. It's a bit high. Analyze the content or frequency to reduce this.",
        
        # SEO Metrics
        "Organic Traffic Growth": f"Organic Traffic Growth: {metric_value}%. Good SEO strategy! Continue to focus on quality content and backlinks.",
        "Keyword Ranking Changes": f"Keyword Ranking Changes: {metric_value}. Keep improving your content and optimizing for high-value keywords.",
        "Backlink Count": f"Backlink Count: {metric_value}. Strong link profile! Focus on building even more quality backlinks for higher authority.",
        
        # Paid Advertising Metrics
        "Cost Per Click (CPC)": f"CPC: {metric_value}$. It's reasonable. Monitor to ensure optimal ROAS and adjust your targeting if needed.",
        "Conversion Rate": f"Conversion Rate: {metric_value}%. Solid! Consider A/B testing landing pages to improve conversions further.",
        "Return on Ad Spend (ROAS)": f"ROAS: {metric_value}$. Great return! Keep optimizing ad creatives and targeting to maintain or improve this.",
        
        # Customer Retention & Revenue Metrics
        "Customer Lifetime Value (CLV)": f"CLV: {metric_value}$. Excellent! Keep focusing on customer retention strategies to increase this further.",
        "Churn Rate": f"Churn Rate: {metric_value}%. It's a bit high. Improve customer satisfaction and post-purchase support.",
        "Average Order Value (AOV)": f"AOV: {metric_value}$. Great! Implement upsell and cross-sell strategies to increase it even further."
    }
    return suggestions.get(metric_name, "")

# Display DataFrame with metrics in a CSV-like format (visible in pandas DataFrame)
print("Metrics in Structured Format:\n")
print(df)

# Generate and display dynamic suggestions for each metric
for index, row in df.iterrows():
    metric_name = row["Metric Name"]
    metric_value = row["Metric Value"]
    suggestion = get_dynamic_suggestion(metric_name, metric_value)
    print(f"\nMetric: {metric_name}\nValue: {metric_value}\nSuggestion: {suggestion}")

# Function to plot visualizations for metrics
def plot_metrics():
    # Set the figure size for better visibility
    plt.figure(figsize=(10, 6))

    # Plotting the Metric Value Distribution (Bar Plot)
    plt.bar(df["Metric Name"], df["Metric Value"], color='skyblue')
    plt.xticks(rotation=90)  # Rotate labels for better readability
    plt.title('Metric Values Visualization')
    plt.ylabel('Metric Value')
    plt.tight_layout()

    # Save the plot to the 'output_of_the_analysis' folder
    plt.savefig(f"{output_folder}/metric_values_visualization.png")
    plt.show()

    # Generate more specific plots for individual metrics (example: Email Metrics)
    open_rate_value = df[df["Metric Name"] == "Open Rate"]["Metric Value"].values[0]
    click_rate_value = df[df["Metric Name"] == "Click-Through Rate (CTR)"]["Metric Value"].values[0]
    unsubscribe_rate_value = df[df["Metric Name"] == "Unsubscribe Rate"]["Metric Value"].values[0]

    # Plot Pie Chart for Email Performance
    plt.figure(figsize=(6, 6))
    labels = ['Open Rate', 'Click-Through Rate', 'Unsubscribe Rate']
    values = [open_rate_value, click_rate_value, unsubscribe_rate_value]
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99', '#ff6666'])
    plt.title('Email Performance Breakdown')
    plt.tight_layout()

    # Save the pie chart
    plt.savefig(f"{output_folder}/email_performance_pie_chart.png")
    plt.show()

# Plot the metrics using the defined function
plot_metrics()
