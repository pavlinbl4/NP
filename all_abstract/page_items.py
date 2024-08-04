from all_abstract.final_item import article_data
from all_abstract.get_data_from_page import work_with_selected_page
from loguru import logger


def check_all_articles_and_extract_data(articles):
    articles_on_page = []
    for article in articles:
        try:
            one_article_data = article_data(article)
            articles_on_page.append(one_article_data)
        except Exception as e:
            logger.error(f"Error extracting data from article: {e}")
    return articles_on_page


if __name__ == '__main__':
    try:
        articles = work_with_selected_page(1)
        extracted_data = check_all_articles_and_extract_data(articles)
        logger.info(f"Extracted data: {extracted_data}")
    except Exception as e:
        logger.error(f"Error processing articles: {e}")