import requests


def get_amount_of_links(link):
    try:
        response = requests.get(link)

        return response.text.count('<a')
    except requests.RequestException:
        print('Wystąpił błąd.')


print(get_amount_of_links('https://www.youtube.com/'))
