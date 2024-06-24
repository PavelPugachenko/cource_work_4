from src.class_vacancy import FromVacancy
from src.translation import vac_user


user_vac = vac_user()


def sorting(vacancies, n: int):
    sort_vac = []
    for vac in vacancies:
        try:
            sort_vac.append(FromVacancy(vac['name'], vac['salary'], vac['url'], vac["snippet"]['requirement']))
        except TypeError as e:
            print(f"Ошибка при обработке вакансии: {vac}")
            print(e)
            continue

    # Сортируем по зарплате "to" и выдаем top n
    sorted_vacancies = sorted(sort_vac, key=lambda x: x.salary["to"], reverse=True)
    return sorted_vacancies[:n]