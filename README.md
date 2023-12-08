## The Analysis of Tweets with #ChatGPT
Name: Ruixin Han

### Background 
When ChatGPT launched, the information about the new technology went viral on social media. On Twitter, users can easily have first-hand updates on what the big companies have discussed and their next move in the current competitive environment. This analysis investigates the tweets that have hashtag #chatgpt at the time during January 22-24, 2023, and specifically looks into the content of the tweets and the external links within the tweets. 

The datasets I use for this analysis are: Twitter dataset, Forbes 2000 Global Companies from Kaggle, external links that are linked in the tweet content

### Hypotheses
- Tweets containing external links are more likely to direct users to websites of major technology companies, or established news outlets, compared to tweets without external links. Tweets containing external links that belong to major technology companies have more retweets and likes than tweets without external links.
- In the dataset of tweets, those featuring specific ethics-related keywords or hashtags are observed at a lower frequency compared to those expressing enthusiasm. Furthermore, tweets with ethics-related content are anticipated to garner more likes and retweets, surpassing both the general average engagement for tweets lacking these markers and the engagement metrics of similar tweets from a prior timeframe. 
  - ethics_related_keywords = ['ethics', 'moral', 'justice', 'fairness', 'equity', 'rights', 'duty', 'responsibility', 'transparency', 'bias', 'accountability', 'safety', 'privacy', 'governable']
  - enthusiasm_expressing_keywords = ['excited', 'enthusiastic', 'eager', 'thrilled', 'passionate', 'keen', 'animated', 'spirited', 'zealous', 'ardent', 'joyful', 'exhilarated', 'motivated', 'inspired']
- Tweets linking to AI-related academic papers that contain the keywords 'ChatGPT', 'model', and 'human' in their titles or abstracts will receive a higher number of likes and retweets compared to tweets linking to AI-related academic papers without these keywords.
  - Specify the AI-related academic papers
  - Fetch the linked URL and save the title and abstract in the JSON file
  - Compare tweets that have keywords and those without keywords

Note: for your best experience of browsing through all the files, please first delete the urls.json file (this JSON file is for the purposes of grading by the instructor) and then try running all the Jupyter Notebook and the test in the functions.py. 
