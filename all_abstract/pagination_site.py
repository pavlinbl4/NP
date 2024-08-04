"""
Теперь осталось перебрать нужное нам количество страниц
и придумать ключ, по которому перебор страниц будет прекращаться
"""
from all_abstract.get_data_from_page import work_with_selected_page
from all_abstract.page_items import check_all_articles_and_extract_data
from all_abstract.work_with_article_data import work_with_article_data


def stop_function(count):
    # Define the condition to stop the pagination cycle
    return count < 10


def pagination_cycle(count=0):
    while stop_function(count):
        count += 1
        articles = work_with_selected_page(count)
        articles_on_page = check_all_articles_and_extract_data(articles)

        work_with_article_data(articles_on_page)

    print("Cycle stopped")


if __name__ == '__main__':
    pagination_cycle()
