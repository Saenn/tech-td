
class Sanitizer:

    def __init__(self):
        pass

    def transform_data(self, data: str):
        data = self._lower_text(data)
        data = self._replace_tab(data)

        # add more transformation here
        return data
    
    @staticmethod
    def _lower_text(data: str):
        lower_data = data.lower()
        return lower_data

    @staticmethod
    def _replace_tab(data: str):
        no_tab_data = data.replace('tab', '____')
        return no_tab_data
