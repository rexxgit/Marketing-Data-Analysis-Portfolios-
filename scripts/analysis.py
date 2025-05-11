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

# Function to generate dynamic suggestions based on the metric values
def get_dynamic_suggestion(metric_name, metric_value):
    suggestions = {
        # Website & Traffic Analytics
        "Total Visitors": "Monitor the trend of unique visitors month over month. If you're seeing a consistent increase, consider investing more in marketing efforts to capitalize on that growth. If there's stagnation or decline, investigate your referral sources or content strategy.",
        "Pageviews": "Identify pages with high traffic and optimize them for conversions. If certain pages are underperforming, consider improving content or SEO. Pages with low pageviews may require better internal linking or promotional strategies.",
        "Bounce Rate": "A high bounce rate indicates that visitors are not finding what they expect. Analyze the content on landing pages to ensure it aligns with their search intent. A/B test content variations to see what reduces bounce rates.",
        
        # Social Media Metrics
        "Total Followers Growth": "A steady increase in followers indicates successful engagement strategies. Review which campaigns or content drove growth to replicate successful tactics. Conversely, if growth is plateauing, consider new channels or collaborations to engage your audience.",
        "Engagement Rate (Likes, Comments, Shares)": "High engagement suggests that your audience finds your content valuable. Focus on content formats that yield the highest engagement rates, and continue experimenting with new formats or themes. Low engagement may require revisiting your content strategy.",
        
        # Email Marketing Metrics
        "Open Rate": "Monitor open rates of email campaigns. If open rates are declining, consider modifying subject lines, segmenting your mailing list, or testing the timing of your sends to find the optimal configuration.",
        "Click-Through Rate (CTR)": "Analyze which email campaigns have the best CTR. Experiment with different content, CTAs, and visuals to see what resonates most with your audience. Low CTR might require reevaluating your value proposition in emails.",
        "Unsubscribe Rate": "A high unsubscribe rate could suggest misalignment with subscriber expectations. Review your content strategy—perhaps provide more targeted content or give subscribers the option to choose content types they wish to receive.",
        
        # SEO Metrics
        "Organic Traffic Growth": "If organic traffic is growing consistently, consider investing in additional SEO efforts or content marketing. If traffic is stagnant, conduct a competitive analysis, refresh existing content, or pursue backlinking opportunities.",
        "Keyword Ranking Changes": "Focus on keywords that are improving while analyzing those that are declining. Consider developing content around high-potential keywords and revisiting SEO tactics for keywords that are losing ranking.",
        "Backlink Count": "A strong backlink profile supports organic rankings. Identify sources contributing to your strongest backlinks and pursue similar domains for partnerships. Decrease in backlinks may require outreach initiatives to re-establish those links.",
        
        # Paid Advertising Metrics
        "Cost Per Click (CPC)": "Analyze your CPC by campaign. If you find campaigns with increasing CPC without a corresponding rise in conversions, rethink those campaigns. Consider reallocating budget to campaigns with a better ROI.",
        "Conversion Rate": "Track conversion rates closely. High conversion campaigns should receive additional funding. If conversions are below expectations, analyze the user funnel, landing pages, and offer to find potential drop-off points.",
        "Return on Ad Spend (ROAS)": "Campaigns with a high ROAS should be scaled. Conversely, campaigns with low ROAS may need to be refined or cut entirely. Understanding the channels contributing to high ROAS can inform future investments.",
        
        # Customer Retention & Revenue Metrics
        "Customer Lifetime Value (CLV)": "If CLV is increasing, this suggests strong customer fidelity or value from current offerings. Consider retention strategies like loyalty programs. A declining CLV may indicate a need to reevaluate pricing or customer satisfaction.",
        "Churn Rate": "A declining churn rate is positive and suggests effective retention strategies. If churn rates are high, identify common reasons for cancellation through customer feedback and make necessary changes to your offerings.",
        "Average Order Value (AOV)": "If AOV is increasing, analyze which products are driving this. Strategies to enhance AOV include cross-selling, upselling, and bundling products. If AOV is declining, consider revising pricing, product quality, or promotional strategies."
    }
    return suggestions.get(metric_name, "No suggestion available for this metric.")

# Function to plot individual metrics with the recommendation
def plot_individual_metrics():
    # Loop through each metric and plot individually
    for index, row in df.iterrows():
        metric_name = row["Metric Name"]
        metric_value = row["Metric Value"]
        suggestion = get_dynamic_suggestion(metric_name, metric_value)

        plt.figure(figsize=(6, 4))
        plt.bar([metric_name], [metric_value], color='skyblue')
        plt.title(f'{metric_name} Visualization')
        plt.ylabel('Metric Value')
        
        # Adding recommendation text on the chart
        plt.text(0, metric_value + 0.05, suggestion, ha='center', va='bottom', fontsize=10, wrap=True)

        plt.tight_layout()
        
        # Save each plot individually
        plot_filename = f"{output_folder}/{metric_name.replace(' ', '_').replace('(', '').replace(')', '')}_visualization_with_suggestion.png"
        plt.savefig(plot_filename)
        plt.show()

# Plot the individual metrics using the defined function
plot_individual_metrics()
