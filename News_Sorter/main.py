from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='365dc81095b74a678207acf11027b2b1')

sports_headlines = newsapi.get_top_headlines(
    category='sports',
    language='en',
    country='us'
)

'''for article in sports_headlines['articles']:
    print(f'Title: {article['title']}')
    print(f'Source: {article['source']['name']}')
    print(f'URL: {article['url']}')
    print(f'Published: {article['publishedAt']}')
    print('-------')'''

spurs_articles = newsapi.get_everything(
    q='Tottenham',
    language='en',
    sort_by='publishedAt',
    from_param='2026-01-28',
    to='2026-02-01'
)

for article in spurs_articles['articles']:
    print(f'Title: {article['title']}')
    print(f'Source: {article['source']['name']}')
    print(f'URL: {article['url']}')
    print(f'Published: {article['publishedAt']}')
    print('----------')