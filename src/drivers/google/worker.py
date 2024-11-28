from array import array

from src.drivers.google.request import Request


class ApiWorker:
    """
    Api worker class
    """
    endpoint = '/books/v1/volumes'

    def searchItem(self, string):
        """
        Makes an API request and processes data to be an array of items compatible with app's models.

        :param string: Search string
        :return array: Objects data
        """
        rq = Request.fromConfig()
        rq.build(self.endpoint, {'q': string})
        response = rq.make()
        items = []

        def authorsToString(authors):
            authors_string = ''
            for author in authors:
                authors_string += author + ', '
            return authors_string


        for i in range(0, min(50, len(response['items']))):
            item = {}
            item['id'] = response['items'][i]['id']
            item['title'] = response['items'][i]['volumeInfo']['title']

            if 'authors' in response['items'][i]['volumeInfo']:
                item['author'] = authorsToString(response['items'][i]['volumeInfo']['authors'])
            else:
                item['author'] = ''

            if 'publishedDate' in response['items'][i]['volumeInfo']:
                item['year'] = (response['items'][i]['volumeInfo']['publishedDate'].split('-'))[0]
            else:
                item['year'] = ''

            if 'imageLinks' in response['items'][i]['volumeInfo']:
                item['image'] = response['items'][i]['volumeInfo']['imageLinks']['thumbnail']
            else:
                item['image'] = ''

            identifiers = {}
            if 'industryIdentifiers' in response['items'][i]['volumeInfo']:
                for identifier in response['items'][i]['volumeInfo']['industryIdentifiers']:
                    identifiers[identifier['type']] = identifier['identifier']

                if 'ISBN_13' in identifiers.keys():
                    item['isbn'] = identifiers['ISBN_13']
                elif 'ISBN_10' in identifiers.keys():
                    item['isbn'] = identifiers['ISBN_10']
                elif len(identifiers) > 0:
                    k = list(identifiers)[-1]
                    item['isbn'] = identifiers[k]
            else:
                item['isbn'] = ''

            items.append(item)
        return items