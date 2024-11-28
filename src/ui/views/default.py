from src.ui.view import View


class VTemplate(View):

    @staticmethod
    def btnClicked():
        pass

    def getElements(self):
        return [
            {
                'type':'text',
                'content': 'Glowny widok',
                'width': 200
             },

                'type':'button',
                'content': 'Przejdz do drugiego widoku',
                'command': self.btnClicked,
                'width': 200,
            }
        ]