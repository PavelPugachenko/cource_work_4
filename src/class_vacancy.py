class FromVacancy:

    def __init__(self, name, salary, currency, url, requirement='Информация отсутствует'):
        self.name = name
        self.salary = salary
        self.currency = currency
        self.url = url
        self.requirement = requirement

    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Зарплата: {self.salary} {self.currency}\n'
                f'Требования: {self.requirement}\n'
                f'Ссылка на вакансию: <{self.url}>\n')

    def __gt__(self, other):
        return self.salary['to'] > other.salary['to']

    def __lt__(self, other):
        return self.salary['to'] < other.salary['to']