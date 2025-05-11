import matplotlib.pyplot as plt

# 1. Website & Traffic Analytics
total_visits = 28750
pageviews = 97230
single_page_visits = 13980

bounce_rate = (single_page_visits / total_visits) * 100

website_analytics = {
    "Total Visitors": total_visits,
    "Pageviews": pageviews,
    "Bounce Rate (%)": round(bounce_rate, 2)
}

# Dynamic Recommendations for Website Traffic Analytics
def website_traffic_recommendations():
    recommendations = []
    if total_visits < 30000:
        recommendations.append("Total visitors are low. Consider improving your SEO and referral traffic strategies.")
    if bounce_rate > 60:
        recommendations.append("The bounce rate is high. You may need to enhance your landing page and optimize content for better engagement.")
    if pageviews / total_visits < 3:
        recommendations.append("Consider increasing pageviews per visit by improving internal linking and content discovery.")
    return recommendations

# Visualization for Website Traffic Analytics
def plot_website_traffic():
    plt.figure(figsize=(8, 5))
    categories = ['Total Visitors', 'Pageviews', 'Bounce Rate (%)']
    values = [total_visits, pageviews, round(bounce_rate, 2)]
    plt.bar(categories, values, color=['blue', 'green', 'red'])
    plt.title('Website & Traffic Analytics')
    plt.ylabel('Values')
    plt.savefig("website_traffic.png")
    plt.show()

plot_website_traffic()

# Save Recommendations for Website Traffic
def save_website_traffic_decisions():
    recommendations = website_traffic_recommendations()
    with open("website_traffic_decisions.txt", "w") as file:
        file.write("Website & Traffic Analytics Informed Decisions:\n")
        for rec in recommendations:
            file.write(f"- {rec}\n")

save_website_traffic_decisions()

# 2. Social Media Metrics
followers_start = 25600
followers_end = 29800
likes = 4200
comments = 860
shares = 530

followers_growth = followers_end - followers_start
engagement_rate = ((likes + comments + shares) / followers_end) * 100

social_media_metrics = {
    "Total Followers Growth": followers_growth,
    "Engagement Rate (%)": round(engagement_rate, 2)
}

# Dynamic Recommendations for Social Media Metrics
def social_media_recommendations():
    recommendations = []
    if followers_growth < 1000:
        recommendations.append("Follower growth is slower than expected. Try influencer partnerships or paid ads to boost follower acquisition.")
    if engagement_rate < 2:
        recommendations.append("Engagement rate is low. Consider revisiting your content strategy, focusing on higher-interaction posts.")
    return recommendations

# Visualization for Social Media Metrics
def plot_social_media_metrics():
    plt.figure(figsize=(8, 5))
    categories = ['Total Followers Growth', 'Engagement Rate (%)']
    values = [followers_growth, round(engagement_rate, 2)]
    plt.bar(categories, values, color=['purple', 'orange'])
    plt.title('Social Media Metrics')
    plt.ylabel('Values')
    plt.savefig("social_media_metrics.png")
    plt.show()

plot_social_media_metrics()

# Save Recommendations for Social Media
def save_social_media_decisions():
    recommendations = social_media_recommendations()
    with open("social_media_decisions.txt", "w") as file:
        file.write("Social Media Metrics Informed Decisions:\n")
        for rec in recommendations:
            file.write(f"- {rec}\n")

save_social_media_decisions()

# 3. Email Marketing Metrics
emails_sent = 10000
emails_opened = 2740
emails_clicked = 610
unsubscribed = 60

open_rate = (emails_opened / emails_sent) * 100
ctr = (emails_clicked / emails_sent) * 100
unsubscribe_rate = (unsubscribed / emails_sent) * 100

email_marketing_metrics = {
    "Open Rate (%)": round(open_rate, 2),
    "Click-Through Rate (CTR %)": round(ctr, 2),
    "Unsubscribe Rate (%)": round(unsubscribe_rate, 2)
}

# Dynamic Recommendations for Email Marketing Metrics
def email_marketing_recommendations():
    recommendations = []
    if open_rate < 20:
        recommendations.append("Open rate is low. Try refining your subject lines and segmenting your email list more effectively.")
    if ctr < 5:
        recommendations.append("CTR is low. Experiment with better calls-to-action (CTAs) and improved content.")
    if unsubscribe_rate > 1:
        recommendations.append("Unsubscribe rate is higher than usual. You may want to review the frequency and relevancy of your emails.")
    return recommendations

# Visualization for Email Marketing Metrics
def plot_email_marketing_metrics():
    plt.figure(figsize=(8, 5))
    categories = ['Open Rate (%)', 'Click-Through Rate (CTR %)', 'Unsubscribe Rate (%)']
    values = [round(open_rate, 2), round(ctr, 2), round(unsubscribe_rate, 2)]
    plt.bar(categories, values, color=['cyan', 'magenta', 'yellow'])
    plt.title('Email Marketing Metrics')
    plt.ylabel('Percentage (%)')
    plt.savefig("email_marketing_metrics.png")
    plt.show()

plot_email_marketing_metrics()

# Save Recommendations for Email Marketing
def save_email_marketing_decisions():
    recommendations = email_marketing_recommendations()
    with open("email_marketing_decisions.txt", "w") as file:
        file.write("Email Marketing Metrics Informed Decisions:\n")
        for rec in recommendations:
            file.write(f"- {rec}\n")

save_email_marketing_decisions()

# 4. SEO Metrics
organic_visits_start = 8000
organic_visits_end = 10600
ranking_change = 18
backlinks = 1345

organic_traffic_growth = ((organic_visits_end - organic_visits_start) / organic_visits_start) * 100

seo_metrics = {
    "Organic Traffic Growth (%)": round(organic_traffic_growth, 2),
    "Keyword Ranking Changes": ranking_change,
    "Backlink Count": backlinks
}

# Dynamic Recommendations for SEO Metrics
def seo_recommendations():
    recommendations = []
    if organic_traffic_growth < 10:
        recommendations.append("Organic traffic growth is slower than desired. Focus on content marketing and backlinking strategies.")
    if ranking_change < 5:
        recommendations.append("Keyword ranking changes are minimal. Consider updating older content and pursuing additional SEO optimizations.")
    if backlinks < 1500:
        recommendations.append("Backlink count is low. Work on acquiring more backlinks from authoritative domains.")
    return recommendations

# Visualization for SEO Metrics
def plot_seo_metrics():
    plt.figure(figsize=(8, 5))
    categories = ['Organic Traffic Growth (%)', 'Keyword Ranking Changes', 'Backlink Count']
    values = [round(organic_traffic_growth, 2), ranking_change, backlinks]
    plt.bar(categories, values, color=['darkblue', 'green', 'brown'])
    plt.title('SEO Metrics')
    plt.ylabel('Values')
    plt.savefig("seo_metrics.png")
    plt.show()

plot_seo_metrics()

# Save Recommendations for SEO
def save_seo_decisions():
    recommendations = seo_recommendations()
    with open("seo_decisions.txt", "w") as file:
        file.write("SEO Metrics Informed Decisions:\n")
        for rec in recommendations:
            file.write(f"- {rec}\n")

save_seo_decisions()

# 5. Paid Advertising Metrics
total_cost = 1150  # dollars
total_clicks = 1000
total_conversions = 84
total_revenue = 4255

cpc = total_cost / total_clicks
conversion_rate = (total_conversions / total_clicks) * 100
roas = total_revenue / total_cost

paid_ads_metrics = {
    "Cost Per Click (CPC $)": round(cpc, 2),
    "Conversion Rate (%)": round(conversion_rate, 2),
    "Return on Ad Spend (ROAS)": round(roas, 2)
}

# Dynamic Recommendations for Paid Ads Metrics
def paid_ads_recommendations():
    recommendations = []
    if cpc > 1:
        recommendations.append("CPC is high. Consider refining your targeting or optimizing ad copy to lower costs.")
    if conversion_rate < 5:
        recommendations.append("Conversion rate is low. Test different ad creatives, landing pages, and offers.")
    if roas < 3:
        recommendations.append("ROAS is below target. Focus on improving your ad copy and optimizing conversion paths.")
    return recommendations

# Visualization for Paid Advertising Metrics
def plot_paid_ads_metrics():
    plt.figure(figsize=(8, 5))
    categories = ['CPC ($)', 'Conversion Rate (%)', 'ROAS']
    values = [round(cpc, 2), round(conversion_rate, 2), round(roas, 2)]
    plt.bar(categories, values, color=['lightblue', 'lightgreen', 'lightcoral'])
    plt.title('Paid Advertising Metrics')
    plt.ylabel('Values')
    plt.savefig("paid_ads_metrics.png")
    plt.show()

plot_paid_ads_metrics()

# Save Recommendations for Paid Ads
def save_paid_ads_decisions():
    recommendations = paid_ads_recommendations()
    with open("paid_ads_decisions.txt", "w") as file:
        file.write("Paid Advertising Metrics Informed Decisions:\n")
        for rec in recommendations:
            file.write(f"- {rec}\n")

save_paid_ads_decisions()

# 6. Customer Retention & Revenue Metrics
total_revenue_customers = 64550
total_customers = 100
customers_lost = 12
total_orders = 825

clv = total_revenue_customers / total_customers
churn_rate = (customers_lost / total_customers) * 100
aov = total_revenue_customers / total_orders

customer_metrics = {
    "Customer Lifetime Value (CLV $)": round(clv, 2),
    "Churn Rate (%)": round(churn_rate, 2),
    "Average Order Value (AOV $)": round(aov, 2)
}

# Dynamic Recommendations for Customer Retention Metrics
def customer_revenue_recommendations():
    recommendations = []
    if clv < 600:
        recommendations.append("CLV is on the lower end. Consider enhancing customer loyalty programs and offering personalized products.")
    if churn_rate > 10:
        recommendations.append("Churn rate is high. Improve customer retention strategies, such as email engagement or discounts.")
    if aov < 80:
        recommendations.append("AOV is low. Implement upselling and cross-selling techniques to boost average order values.")
    return recommendations

# Visualization for Customer Retention & Revenue Metrics
def plot_customer_metrics():
    plt.figure(figsize=(8, 5))
    categories = ['CLV ($)', 'Churn Rate (%)', 'AOV ($)']
    values = [round(clv, 2), round(churn_rate, 2), round(aov, 2)]
    plt.bar(categories, values, color=['lightyellow', 'pink', 'lightgreen'])
    plt.title('Customer Retention & Revenue Metrics')
    plt.ylabel('Values')
    plt.savefig("customer_metrics.png")
    plt.show()

plot_customer_metrics()

# Save Recommendations for Customer Retention & Revenue
def save_customer_decisions():
    recommendations = customer_revenue_recommendations()
    with open("customer_decisions.txt", "w") as file:
        file.write("Customer Retention & Revenue Metrics Informed Decisions:\n")
        for rec in recommendations:
            file.write(f"- {rec}\n")

save_customer_decisions()

print("Reports and recommendations have been generated and saved.")
