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

        for i in range(0, min(50, len(response['items']))):
            items.append(self.processObject(response['items'][i]))
        return items

    def getItem(self, id):
        rq = Request.fromConfig()
        ep = self.endpoint + '/' + id
        print(ep)
        rq.build(ep, {})
        response = rq.make()
        print(response, 'rp')
        if(type(response) is dict):
            return self.processObject(response)
        return None

    def processObject(self, data):
        def authorsToString(authors):
            authors_string = ''
            for author in authors:
                authors_string += author + ', '
            return authors_string

        item = {}
        item['id'] = data['id']

        if 'title' in data['volumeInfo']:
            item['title'] = data['volumeInfo']['title']
        else:
            item['title'] = ''

        if 'authors' in data['volumeInfo']:
            item['author'] = authorsToString(data['volumeInfo']['authors'])
        else:
            item['author'] = ''

        if 'publishedDate' in data['volumeInfo']:
            item['year'] = (data['volumeInfo']['publishedDate'].split('-'))[0]
        else:
            item['year'] = ''

        if 'imageLinks' in data['volumeInfo']:
            item['image'] = data['volumeInfo']['imageLinks']['thumbnail']
        else:
            item['image'] = ''

        identifiers = {}
        if 'industryIdentifiers' in data['volumeInfo']:
            for identifier in data['volumeInfo']['industryIdentifiers']:
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

        return item

