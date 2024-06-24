from src.class_api import FromHHru
from src.methods import ListVacancies
from src.sorting import sorting
from translation import vac_user

def interface():
    """Функция для взаимодействия с пользователем"""

    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = FromHHru()
    vacancies = hh.get_vacancies(user_vacancy)

    fv = ListVacancies()
    fv1 = fv.save_vacancies(vacancies)

    name_criterion = input('Введите критерий для отбора вакансий: \n')
    fv4 = fv.get_data(name_criterion)

    # Получение обработанных вакансий перед сортировкой
    processed_vacancies = vac_user()

    n = input('Введите количество вакансий для просмотра: \n')
    top_vacancies = sorting(processed_vacancies, int(n))  # Передаем данные обработанных вакансий

    # Вывод топовых вакансий
    for vac in top_vacancies:
        print(vac)  # Благодаря методу __str__ вывод будет форматированным

    name_exit = input('Завершим и очистим файл вакансий да/нет : \n')
    if name_exit == 'да':
        fv4 = fv.delete_vacancy()
    else:
        interface()

interface()
