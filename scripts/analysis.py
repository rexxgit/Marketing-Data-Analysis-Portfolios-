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
    suggestions = {
        "Total Visitors": "Great job! Continue monitoring the trend of unique visitors. If growth continues, consider scaling marketing efforts." if metric_value > 25000 else "Visitor growth is steady. Consider increasing visibility through paid promotions or partnerships to boost numbers.",
        "Pageviews": "Your pageviews are high! Focus on optimizing high-traffic pages to convert visitors into customers." if metric_value > 100000 else "Low pageviews could indicate that content optimization is needed. Enhance internal linking and SEO strategies.",
        "Bounce Rate (%)": "Your bounce rate is excellent! Continue optimizing content to maintain low bounce rates." if metric_value < 40 else "High bounce rates suggest issues with landing page relevance. Consider A/B testing content and improving page load speed.",
        "Total Followers Growth": "Follower growth is strong! Keep engaging your audience and explore partnerships to maintain momentum." if metric_value > 2000 else "Follower growth is plateauing. Try diversifying content or running targeted ad campaigns to boost engagement.",
        "Engagement Rate (%)": "Excellent engagement! Focus on high-performing content formats to sustain engagement." if metric_value > 5 else "Low engagement suggests the need for content reevaluation. Test different content types or adjust posting frequency.",
        "Open Rate (%)": "Your open rate is impressive! Keep experimenting with subject lines to maintain high open rates." if metric_value > 25 else "Open rates are low. Try segmenting your audience more effectively or revising your email subject lines.",
        "Click-Through Rate (CTR %)": "Great click-through rate! Focus on optimizing your CTAs and visuals to maintain this performance." if metric_value > 3 else "Low CTR suggests your CTAs or email content may need improvement. Test different messaging and layouts.",
        "Unsubscribe Rate (%)": "Your unsubscribe rate is low! Continue delivering valuable content to your subscribers." if metric_value < 1 else "Unsubscribes are rising. Reassess the content you're sending to ensure it's in line with subscriber expectations.",
        "Organic Traffic Growth (%)": "Excellent organic growth! Consider scaling your SEO efforts further and investing in high-potential keywords." if metric_value > 20 else "Organic traffic growth is slow. Revise your SEO strategy or consider investing in backlinks to boost rankings.",
        "Keyword Ranking Changes": "You're gaining significant rankings! Focus on maintaining these keywords and expand your SEO strategy." if metric_value > 10 else "Ranking changes are limited. Focus on improving SEO for underperforming keywords and explore new content ideas.",
        "Backlink Count": "Your backlink profile is strong! Keep building relationships for additional high-quality backlinks." if metric_value > 1000 else "Your backlink count is low. Consider outreach campaigns to earn more backlinks from authoritative sites.",
        "Cost Per Click (CPC $)": "Your CPC is low! Continue optimizing ad campaigns for cost-efficient results." if metric_value < 1 else "High CPC suggests that your campaigns may need optimization. Try refining targeting or adjusting your ad creatives.",
        "Conversion Rate (%)": "Great conversion rate! Focus on maintaining this and experiment with upselling or cross-selling strategies." if metric_value > 3 else "Conversion rate is lower than expected. Investigate potential drop-off points in the funnel and optimize landing pages.",
        "Return on Ad Spend (ROAS)": "Your ROAS is fantastic! Scale successful campaigns and continue to optimize high-performing channels." if metric_value > 4 else "Low ROAS suggests a need for better campaign targeting or creative changes to improve profitability.",
        "Customer Lifetime Value (CLV $)": "Your CLV is healthy! Continue focusing on retention strategies and creating customer loyalty programs." if metric_value > 500 else "Your CLV is on the low end. Investigate ways to increase customer retention and lifetime value.",
        "Churn Rate (%)": "Low churn rate indicates strong retention efforts. Keep up the great work!" if metric_value < 5 else "High churn rate suggests customers may not be satisfied. Gather feedback and focus on improving customer experiences.",
        "Average Order Value (AOV $)": "Your AOV is strong! Consider promoting product bundles or upselling to increase this further." if metric_value > 75 else "AOV is low. Look into strategies like upselling or cross-selling to encourage customers to spend more per order."
    }
    return suggestions.get(metric_name, "")

# Function to save unique plots for each metric
def save_unique_plot(metric_name, metric_value, filename):
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
    
    # Save the plot as PNG
    plt.tight_layout()
    plt.legend()
    plt.savefig(f'{output_folder}/{filename}.png', format='png')
    plt.close()

# Function to save recommendations as text files
def save_recommendation_text(metric_name, suggestion, filename):
    with open(f'{output_folder}/{filename}_recommendation.txt', 'w') as f:
        f.write(f"Recommendation for {metric_name}:\n\n{suggestion}")

# Loop through the metrics and generate and save unique plots and recommendations
for metric_name, metric_value in metrics.items():
    suggestion = get_dynamic_suggestion(metric_name, metric_value)
    filename = metric_name.replace(" ", "_").replace("(%", "").replace(")", "")
    save_unique_plot(metric_name, metric_value, filename)
    save_recommendation_text(metric_name, suggestion, filename)

print("Unique plots with recommendations have been generated and saved in the 'output_of_the_analysis' folder.")
