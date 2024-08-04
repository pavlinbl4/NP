from loguru import logger

selector_dict = {
    'date': "tplarticle-date",
    'name': "tplarticle-title",
    'image_src': "tplarticle-img lazyload"
}


def article_data(article):
    article_date = article.find("div", class_=selector_dict['date']).text.strip()  # дата публикации
    logger.info(f"Article Date: {article_date}")

    article_name = article.find("div", class_=selector_dict['name']).text.strip()  # заголовки статей
    logger.info(f"Article Name: {article_name}")

    image_src = article.find("img", class_=selector_dict['image_src']).get('data-src')
    logger.info(f"Image Source: {image_src}")

    return article_date, article_name, image_src
