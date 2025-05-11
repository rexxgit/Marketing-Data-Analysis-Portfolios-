import matplotlib.pyplot as plt
import pandas as pd
import os

# Create the 'output_of_the_analysis' folder if it doesn't exist
output_folder = 'output_of_the_analysis'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the metrics and their values
metrics = {
    "Total Visitors": 28750,
    "Pageviews": 97230,
    "Bounce Rate (%)": (13980 / 28750) * 100,
    "Total Followers Growth": 29800 - 25600,
    "Engagement Rate (%)": ((4200 + 860 + 530) / 29800) * 100,
    "Open Rate (%)": (2740 / 10000) * 100,
    "Click-Through Rate (CTR %)": (610 / 10000) * 100,
    "Unsubscribe Rate (%)": (60 / 10000) * 100,
    "Organic Traffic Growth (%)": ((10600 - 8000) / 8000) * 100,
    "Keyword Ranking Changes": 18,
    "Backlink Count": 1345,
    "Cost Per Click (CPC $)": 1150 / 1000,
    "Conversion Rate (%)": (84 / 1000) * 100,
    "Return on Ad Spend (ROAS)": 4255 / 1150,
    "Customer Lifetime Value (CLV $)": 64550 / 100,
    "Churn Rate (%)": (12 / 100) * 100,
    "Average Order Value (AOV $)": 64550 / 825
}

# Function to generate dynamic suggestions based on the metric values
def get_dynamic_suggestion(metric_name, metric_value):
    if metric_name == "Total Visitors":
        if metric_value > 25000:
            return "Great job! Continue monitoring the trend of unique visitors."
        else:
            return "Consider increasing visibility through paid promotions or partnerships."
    
    elif metric_name == "Pageviews":
        if metric_value > 100000:
            return "Focus on optimizing high-traffic pages to convert visitors into customers."
        else:
            return "Enhance internal linking and SEO strategies."
    
    elif metric_name == "Bounce Rate (%)":
        if metric_value < 40:
            return "Excellent! Continue optimizing content to maintain low bounce rates."
        elif metric_value < 60:
            return "Consider revising landing page content."
        else:
            return "Test landing page variations and improve page load speed."
    
    elif metric_name == "Total Followers Growth":
        if metric_value > 2000:
            return "Strong growth! Keep engaging and explore partnerships."
        else:
            return "Try diversifying content or running targeted campaigns."
    
    elif metric_name == "Engagement Rate (%)":
        if metric_value > 5:
            return "Great engagement! Continue with high-performing content."
        else:
            return "Test different content types or adjust posting frequency."
    
    elif metric_name == "Open Rate (%)":
        if metric_value > 25:
            return "Keep experimenting with subject lines."
        else:
            return "Segment your audience or revise subject lines."
    
    elif metric_name == "Click-Through Rate (CTR %)":
        if metric_value > 3:
            return "Great CTR! Focus on optimizing CTAs."
        else:
            return "Test different messaging and layouts."
    
    elif metric_name == "Unsubscribe Rate (%)":
        if metric_value < 1:
            return "Your unsubscribe rate is low! Continue delivering valuable content."
        else:
            return "Reassess the content you're sending."
    
    elif metric_name == "Organic Traffic Growth (%)":
        if metric_value > 20:
            return "Consider scaling your SEO efforts further."
        else:
            return "Revise your SEO strategy or consider backlinks."
    
    elif metric_name == "Keyword Ranking Changes":
        if metric_value > 10:
            return "Focus on maintaining rankings and expanding SEO."
        else:
            return "Improve SEO for underperforming keywords."
    
    elif metric_name == "Backlink Count":
        if metric_value > 1000:
            return "Keep building relationships for high-quality backlinks."
        else:
            return "Consider outreach campaigns to earn more backlinks."
    
    elif metric_name == "Cost Per Click (CPC $)":
        if metric_value < 1:
            return "Optimize ad campaigns for cost-efficient results."
        else:
            return "Refine targeting or adjust creatives."
    
    elif metric_name == "Conversion Rate (%)":
        if metric_value > 3:
            return "Focus on maintaining this rate and consider upselling."
        else:
            return "Investigate potential drop-off points and optimize landing pages."
    
    elif metric_name == "Return on Ad Spend (ROAS)":
        if metric_value > 4:
            return "Scale successful campaigns and optimize high-performing channels."
        else:
            return "Better targeting or creative changes needed."
    
    elif metric_name == "Customer Lifetime Value (CLV $)":
        if metric_value > 500:
            return "Focus on retention strategies and customer loyalty programs."
        else:
            return "Increase retention efforts."
    
    elif metric_name == "Churn Rate (%)":
        if metric_value < 5:
            return "Low churn rate indicates strong retention."
        else:
            return "Focus on improving customer experience."
    
    elif metric_name == "Average Order Value (AOV $)":
        if metric_value > 75:
            return "Consider promoting product bundles."
        else:
            return "Encourage upselling or cross-selling."

# Function to save unique plots for each metric
def save_unique_plot(metric_name, metric_value, filename):
    plt.figure(figsize=(10, 6))
    
    # Different plot types based on the metric name
    if metric_name == "Total Visitors" or metric_name == "Organic Traffic Growth (%)":
        plt.plot([1, 2, 3, 4], [25000, 26000, 28000, metric_value], marker='o', color='blue', label=metric_name)
        plt.title(f"{metric_name} - Trend Over Time")
        plt.xlabel("Time (months)")
        plt.ylabel("Value")
    
    elif metric_name == "Pageviews":
        plt.bar([1], [metric_value], color='green', label=metric_name)
        plt.title(f"{metric_name} - Total Pageviews")
        plt.xlabel("Pageviews")
        plt.ylabel("Count")
    
    elif metric_name == "Bounce Rate (%)":
        plt.bar([1], [metric_value], color='red', label=metric_name)
        plt.title(f"{metric_name} - Bounce Rate")
        plt.xlabel("Bounce Rate (%)")
        plt.ylabel("Percentage")
    
    elif metric_name == "Total Followers Growth":
        plt.plot([1, 2, 3, 4], [26000, 27000, 28000, 29800], marker='o', color='purple', label=metric_name)
        plt.title(f"{metric_name} - Followers Growth Over Time")
        plt.xlabel("Time (months)")
        plt.ylabel("Followers")
    
    elif metric_name == "Engagement Rate (%)":
        plt.bar([1], [metric_value], color='orange', label=metric_name)
        plt.title(f"{metric_name} - Engagement Rate")
        plt.xlabel("Engagement Rate (%)")
        plt.ylabel("Percentage")
    
    plt.tight_layout()
    plt.legend()
    plt.savefig(f'{output_folder}/{filename}.png', format='png')

# Function to save the recommendation as a text file
def save_recommendation(metric_name, suggestion, filename):
    with open(f'{output_folder}/{filename}.txt', 'w') as file:
        file.write(f"Recommendation for {metric_name}: \n{suggestion}\n")

# Loop through the metrics and generate and save unique plots and recommendations
for metric_name, metric_value in metrics.items():
    suggestion = get_dynamic_suggestion(metric_name, metric_value)
    filename = metric_name.replace(" ", "_").replace("(%", "").replace(")", "")
    
    # Save plot
    save_unique_plot(metric_name, metric_value, filename)
    
    # Save recommendation in a text file
    save_recommendation(metric_name, suggestion, filename)

print("Unique plots and dynamic recommendations have been saved in the 'output_of_the_analysis' folder.")
