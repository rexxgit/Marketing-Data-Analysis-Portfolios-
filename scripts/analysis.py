import matplotlib.pyplot as plt
import pandas as pd
import os

# Create the 'output of the analysis' folder if it doesn't exist
output_folder = 'output of the analysis'
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
            return "Great job! Continue monitoring the trend of unique visitors. If growth continues, consider scaling marketing efforts."
        else:
            return "Visitor growth is steady. Consider increasing visibility through paid promotions or partnerships to boost numbers."
    
    elif metric_name == "Pageviews":
        if metric_value > 100000:
            return "Your pageviews are high! Focus on optimizing high-traffic pages to convert visitors into customers."
        else:
            return "Low pageviews could indicate that content optimization is needed. Enhance internal linking and SEO strategies."
    
    elif metric_name == "Bounce Rate (%)":
        if metric_value < 40:
            return "Your bounce rate is excellent! Continue optimizing content to maintain low bounce rates."
        elif metric_value < 60:
            return "Your bounce rate is moderate. Consider revising landing page content to align better with visitor expectations."
        else:
            return "High bounce rates suggest issues with landing page relevance. Consider A/B testing content and improving page load speed."
    
    elif metric_name == "Total Followers Growth":
        if metric_value > 2000:
            return "Follower growth is strong! Keep engaging your audience and explore partnerships to maintain momentum."
        else:
            return "Follower growth is plateauing. Try diversifying content or running targeted ad campaigns to boost engagement."
    
    elif metric_name == "Engagement Rate (%)":
        if metric_value > 5:
            return "Excellent engagement! Focus on high-performing content formats to sustain engagement."
        else:
            return "Low engagement suggests the need for content reevaluation. Test different content types or adjust posting frequency."
    
    elif metric_name == "Open Rate (%)":
        if metric_value > 25:
            return "Your open rate is impressive! Keep experimenting with subject lines to maintain high open rates."
        else:
            return "Open rates are low. Try segmenting your audience more effectively or revising your email subject lines."
    
    elif metric_name == "Click-Through Rate (CTR %)":
        if metric_value > 3:
            return "Great click-through rate! Focus on optimizing your CTAs and visuals to maintain this performance."
        else:
            return "Low CTR suggests your CTAs or email content may need improvement. Test different messaging and layouts."
    
    elif metric_name == "Unsubscribe Rate (%)":
        if metric_value < 1:
            return "Your unsubscribe rate is low! Continue delivering valuable content to your subscribers."
        else:
            return "Unsubscribes are rising. Reassess the content you're sending to ensure it's in line with subscriber expectations."
    
    elif metric_name == "Organic Traffic Growth (%)":
        if metric_value > 20:
            return "Excellent organic growth! Consider scaling your SEO efforts further and investing in high-potential keywords."
        else:
            return "Organic traffic growth is slow. Revise your SEO strategy or consider investing in backlinks to boost rankings."
    
    elif metric_name == "Keyword Ranking Changes":
        if metric_value > 10:
            return "You're gaining significant rankings! Focus on maintaining these keywords and expand your SEO strategy."
        else:
            return "Ranking changes are limited. Focus on improving SEO for underperforming keywords and explore new content ideas."
    
    elif metric_name == "Backlink Count":
        if metric_value > 1000:
            return "Your backlink profile is strong! Keep building relationships for additional high-quality backlinks."
        else:
            return "Your backlink count is low. Consider outreach campaigns to earn more backlinks from authoritative sites."
    
    elif metric_name == "Cost Per Click (CPC $)":
        if metric_value < 1:
            return "Your CPC is low! Continue optimizing ad campaigns for cost-efficient results."
        else:
            return "High CPC suggests that your campaigns may need optimization. Try refining targeting or adjusting your ad creatives."
    
    elif metric_name == "Conversion Rate (%)":
        if metric_value > 3:
            return "Great conversion rate! Focus on maintaining this and experiment with upselling or cross-selling strategies."
        else:
            return "Conversion rate is lower than expected. Investigate potential drop-off points in the funnel and optimize landing pages."
    
    elif metric_name == "Return on Ad Spend (ROAS)":
        if metric_value > 4:
            return "Your ROAS is fantastic! Scale successful campaigns and continue to optimize high-performing channels."
        else:
            return "Low ROAS suggests a need for better campaign targeting or creative changes to improve profitability."
    
    elif metric_name == "Customer Lifetime Value (CLV $)":
        if metric_value > 500:
            return "Your CLV is healthy! Continue focusing on retention strategies and creating customer loyalty programs."
        else:
            return "Your CLV is on the low end. Investigate ways to increase customer retention and lifetime value."
    
    elif metric_name == "Churn Rate (%)":
        if metric_value < 5:
            return "Low churn rate indicates strong retention efforts. Keep up the great work!"
        else:
            return "High churn rate suggests customers may not be satisfied. Gather feedback and focus on improving customer experiences."
    
    elif metric_name == "Average Order Value (AOV $)":
        if metric_value > 75:
            return "Your AOV is strong! Consider promoting product bundles or upselling to increase this further."
        else:
            return "AOV is low. Look into strategies like upselling or cross-selling to encourage customers to spend more per order."

# Function to save unique plots for each metric
def save_unique_plot(metric_name, metric_value, suggestion, filename):
    plt.figure(figsize=(8, 5))
    
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
    
    # Other plot types can be similarly added based on your requirements...

    # Add the suggestion text on the plot
    plt.text(0.5, metric_value + 1, suggestion, ha='center', va='bottom', fontsize=10, color="black", wrap=True)
    
    plt.tight_layout()
    plt.legend()
    plt.savefig(f'{output_folder}/{filename}.jpg', format='jpg')

# Loop through the metrics and generate and save unique plots
for metric_name, metric_value in metrics.items():
    suggestion = get_dynamic_suggestion(metric_name, metric_value)
    filename = metric_name.replace(" ", "_").replace("(%", "").replace(")", "")
    save_unique_plot(metric_name, metric_value, suggestion, filename)

print("Unique plots with dynamic recommendations have been generated and saved in the 'output of the analysis' folder.")
