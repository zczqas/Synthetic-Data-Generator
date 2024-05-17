CSV_PROMPT_TEXT = """Output a CSV with 2 rows: the first row should contain column titles, and the second row should contain sample data for the specified category. Do not output any other text besides this CSV. The category will be specified dynamically and can include examples such as "twitter user data," "instagram user data," or "ethereum price data."

Examples of column titles and sample data:

Twitter User Data:
- Column Titles: User_ID, Username, Followers_Count, Following_Count, Tweet_Count, Joined_Date
- Sample Data: 123456789, sample_user, 1500, 300, 2500, 2020-01-01

Instagram User Data:
- Column Titles: User_ID, Username, Followers_Count, Following_Count, Post_Count, Joined_Date
- Sample Data: 987654321, insta_user, 2500, 180, 500, 2019-05-15

Ethereum Price Data:
- Column Titles: Date, Open_Price, High_Price, Low_Price, Close_Price, Volume
- Sample Data: 2024-01-01, 3000.50, 3100.75, 2950.25, 3050.60, 15000

Generate the CSV based on the specified category using these examples as a guide.

Category: {category}
"""
