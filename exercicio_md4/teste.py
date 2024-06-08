import requests
import time
import csv
import random
import concurrent.futures
from bs4 import BeautifulSoup
import os


# Global headers to be used for requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
}

MAX_THREADS = 5

def extract_movie_details(movie_link):
    time.sleep(random.uniform(0, 0.2))
    response = BeautifulSoup(requests.get(movie_link, headers=headers).content, 'html.parser')
    movie_soup = response

    title = date = rating = plot_text = None

    # Ajustar os seletores conforme a estrutura atual do site IMDb
    title_tag = movie_soup.find('h1')
    if title_tag:
        title = title_tag.get_text()

    date_tag = movie_soup.find('span', attrs={'class': 'sc-8c396aa2-2 itZqyK'})
    if date_tag:
        date = date_tag.get_text()

    rating_tag = movie_soup.find('span', attrs={'class': 'sc-7ab21ed2-1 jGRxWM'})
    if rating_tag:
        rating = rating_tag.get_text()

    plot_tag = movie_soup.find('span', attrs={'class': 'sc-16ede01-2 gkUxYY'})
    if plot_tag:
        plot_text = plot_tag.get_text().strip()

    print(f"Title: {title}, Date: {date}, Rating: {rating}, Plot: {plot_text}")

    return title, date, rating, plot_text

def extract_movies(soup):
    movies_table = soup.find('div', attrs={'data-testid': 'chart-layout-main-column'}).find('ul')
    movies_table_rows = movies_table.find_all('li')
    movie_links = ['https://imdb.com' + movie.find('a')['href'] for movie in movies_table_rows]

    threads = min(MAX_THREADS, len(movie_links))
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_url = {executor.submit(extract_movie_details, link): link for link in movie_links}
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                results.append(data)
            except Exception as exc:
                print(f'Generated an exception: {exc}')

    with open('./movies.csv', mode='w', newline='', encoding='utf-8') as file:
        movie_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        movie_writer.writerow(['Title', 'Date', 'Rating', 'Plot'])

        for result in results:
            if any(result):
                movie_writer.writerow(result)

def main():
    start_time = time.time()

    popular_movies_url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
    response = requests.get(popular_movies_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    print("Current directory:", os.getcwd())

    extract_movies(soup)

    end_time = time.time()
    print('Total time taken: ', end_time - start_time)

if __name__ == '__main__':
    main()
