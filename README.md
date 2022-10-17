# Проект Афиша

Карта с отмеченными предстоящими меропритяими и их описанием. [Перейти](http://traderdaniil.pythonanywhere.com/)

## Запуск

Для запуска блога у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите сервер командой `python3 manage.py runserver`

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.


Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `STATIC_URL` — по-умолчанию это `'/static/'`. [Что такое STATIC_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_URL).
- `STATIC_ROOT` — по-умолчанию это `'None'`, т.е. текущая папка. [Что такое STATIC_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_ROOT).
- `MEDIA_URL` — по-умолчанию это `'/media/'`. [Что такое MEDIA_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_URL).
- `MEDIA_ROOT` — по-умолчанию это `'media'`. [Что такое MEDIA_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_ROOT). 

## Адреса

Доступны следующие url адреса:
- Начальная страница [127.0.0.1:8000](http://127.0.0.1:8000), на которой представлена карта с мероприятиями
- Станица с информацией о мероприятии в формате json [Крыши_24](http://127.0.0.1:8000/places/2) в виде `places/<id_мероприятия>`


```yaml
{
    "title": "Японский сад",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/52aea6b37037f7aab7cc82301f77e314.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/3cce16840a41f2eafbe47ac72a61da12.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6b3a9e0c004531ca87414eefe1a93509.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/618dc376701574400887d909b5c80f1e.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/761adc74dd5f348d3e7c34d12bee8d24.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/21d6835554ca82259ff201af7da32fe3.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/2095714fb0148a8be9140aadaad302be.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/34b72d0d1819947fe385d0a1986dc962.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6c07645902cc90a2839b63896645021a.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/9b3bc5b446f1aaa8eeed2bb81a04d472.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/9c32261372fa061aad9b1f8827f87b7f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0cd397dc43f864e55dc1ef458ead9d69.jpg"
    ],
    "description_short": "Удивительное и романтичное место, где вы сможете в полной мере ощутить единение человека и природы.",
    "description_long": "<p>Японский сад был торжественно открыт в 1987 году как дар Японии Советскому Союзу. Он стал живописной иллюстрацией японской культуры, в основе которой лежит идея единения человека и природы. Большое внимание в оформлении уделили символическим элементам, благодаря которым пейзаж превратится в величественное святилище, которое не терпит суеты и праздности. Здесь приятно прогуливаться по дорожкам, или, сидя напротив цветущей сакуры, размышлять о бытии, которое в этом чудесном уголке отделяется от лихорадочного московского шума и течёт в размеренном, непривычном ритме.</p><p>Японский сад открыт с конца апреля до середины октября, вход платный. Стоимость входных билетов для взрослых по вторникам, средам и пятницам — 250 рублей, для студентов и детей старше семи лет — 100 рублей, для пенсионеров — 50 рублей. По субботам и воскресеньям взрослые могут посетить сад за 300 рублей, дети — за 150 рублей, пенсионеры — за 50 рублей. С малышей до семи лет плата не взимается. По вторникам с 12:00 до 15:00 вход для пенсионеров, инвалидов и многодетных семей бесплатный. По понедельникам и четвергам сад закрыт для посетителей.</p><p>В Японском саду проводятся экскурсии для индивидуальных посетителей и групп продолжительностью 60 минут, стоимость — 500 рублей с человека. За 1500 рублей можно посетить полуторачасовую экскурсию-лекцию, посвящённую садовой культуре Японии.</p>",
    "coordinates": {
        "lng": "37.58996699999999",
        "lat": "55.84419699999997"
    }
}