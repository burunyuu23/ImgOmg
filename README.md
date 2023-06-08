<p align="center">
  <img src="https://github.com/burunyuu23/ImgOmg/blob/master/frontend/favicon.ico" alt="Логотип проекта">
  <div  align="center">
    <h1 font-weight="900">ImgOmg</h1>
    <h4>krutoi editor photo (по крайней мере он таким задумывался)</h4>
  </div>
<hr/>
</p>

## Оглавление
1. [Возможности](#возможности)
    - [Регистрация и вход](#Регистрация)
    - [Наглядная демонстрация функционала редактора](#Наглядно)
      - [Цвет](#Цвет)
      - [Размер](#Размер)
      - [Сжатие](#Сжатие)
      - [Приколы](#Приколы)
      - [Слои](#Слои)
    - [Профиль пользователя](#Профиль)
2. [Стек технологий](#Стек)
    - [Frontend](#Frontend)
      - [Адаптивность](#Адаптивность)
    - [Backend](#Backend)
      1. [Микросервис авторизации](#Микросервис-1)
          - [Структура](#Микросервис-1-структура)
      2. [Микросервис редактирования изображений](#Микросервис-2)
          - [Структура](#Микросервис-2-структура)
    - [База данных](#База-данных)
    - [Nginx](#Nginx)
3. [Запуск](#Запуск)

<hr/>

# Документация ~~, но на самом деле это отчёт по практике, я подумал почему бы и нет. Не будет же она просто так валяться.~~

  <div  align="center">
    <a href="https://github.com/burunyuu23/ImgOmg/files/11682407/Documentation.pdf">Документацион</a>
</div>

<hr/>

# Проект представляет из себя веб-ресурс для простейших манипуляций над изображениями.

<p align="center">
  <img src="https://github.com/burunyuu23/ImgOmg/assets/34377854/86f41afb-566b-4e66-b756-d298b35139da" alt="Главный экран">
  <br>
  <em>Главный экран</em>
</p>

<a id="Возможности"></a>

# Возможности
- **https**:

<p align="center">
  <img src="https://github.com/burunyuu23/ImgOmg/assets/34377854/80484b4f-8637-4525-b543-53ef38d1d953" alt="https">
  <br>
  <em>https</em>
  <em>сертификаты находятся в '/frontend/certs'</em>
</p>

<a id="Регистрация"></a>

- **Регистрация, идентификация, авторизация через jwt-токен**:


<p align="center">
  <img src="https://github.com/burunyuu23/ImgOmg/assets/34377854/01d7479a-87ec-4562-b641-6afe4743e466" alt="https">
  <br>
  <em>Меню регистрации</em>
  <hr/>
</p>
    
<p align="center">
  <img src="https://github.com/burunyuu23/ImgOmg/assets/34377854/4e21d9ef-0689-4550-94ee-26fc59e17c78" alt="https">
  <br>
  <em>Меню авторизации</em>
  <hr/>
</p>
    
<p align="center">
  <img src="https://github.com/burunyuu23/ImgOmg/assets/34377854/9ddf61f0-30a5-481c-b869-a86e7026aef5" alt="https">
  <br>
  <em>Красивое автозаполнение</em>
  <hr/>
</p>

<p align="center">
  <img src="https://github.com/burunyuu23/ImgOmg/assets/34377854/7aad02e5-e747-4378-969f-1ebcdec04b6e" alt="https">
  <br>
  <em>jwt в куках</em>
  <hr/>
</p>

<a id="Наглядно"></a>

- **Меню редактора**:

![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/d663eef9-0daa-4324-adfb-73564d393c4b)

<a id="Цвет"></a>

1. **Цвет**

> ***Можно сделать красиво***.
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/d0a92ca1-d172-4fe2-a83f-a5f675d2f5d7)

<a id="Размер"></a>

2. **Размер**

> Радужный прямоугольник выделяющий область для обрезки фотографии переливается радугой. 
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/a69fe11a-4dbd-4cc0-a4b7-ba303a1849c7)

> (теперь радужный прямоугольник ещё более радужный!)
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/c4ea17c5-ae5a-4b08-a531-e95786f4a1aa)


<a id="Сжатие"></a>

3. **Сжатие**

> *ЖПЕГ*. (реализация *.ppeg*, а также *.ppega* будет добавлена в следующих версиях)
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/6397c299-7da5-4aa5-a7cf-a852ad6db880)

<a id="Приколы"></a>

4. **Приколы**

> *дрейн генг романчик-манчик сёма, влада карасёва, макс всем привет!*
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/39279f04-c83c-402d-8b70-a13f19b55fce)
> *Заставляет задуматься о бренности.*
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/a687302a-dab3-41a3-80e0-edd45abbb245)
> *Клепаем крипипасты.*
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/55a42545-bcf4-4c4c-ab0a-1b4ebf817718)

***Изображение после редактирования:*** 

![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/c60aa36c-2248-4c9d-ac25-30105367ca67)
АХЫФДАФЫЗЛАЛЗЩЙЦЛЩАЗЙЦ, пока делал ридми нашел ~~баг~~фичу с конфликтом пост-запросов компресса и приколов..

<a id="Слои"></a>

5. **Поддержка слоёв**

> можно нажать на любой из слоёв и вы сбросите картинку до него
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/8df155f4-ec7a-43c9-bf61-b218dcfb3918)
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/29c8e369-150a-4c4f-924c-bcc7b3902b4e)

> ещё одно изображение после редактирования, но уже со всеми пруфами
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/9febb351-3f19-42ed-852c-401c4d91de38)

---

<a id="Профиль"></a>

- **Профиль пользователя**:

![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/82a4852c-7e91-4cdf-8e78-fd3d3bcd1615)

*Сайт пока что не адаптивен... Нам правда жаль, мы это исправим.*

---

<a id="Стек"></a>

# Ну а теперь самое интересное. Стек технологий и в целом его структура.

<a id="Frontend"></a>

## Frontend:
1. **Vue 3 + Vite**
2. **Vuetify**
3. **Vuex**
4. Куча плагинов, по типу: **js-cookie, axios, bcryptjs** (помоему уже не используется), **file-saver**, ...
5. Компоненты: **@vuepic/vue-datepicker** и **mdi**-шки, хотелось конечно использовать **fa**-шки, но как-то руки не дошли.
6. Кривой дизайн
7. Огромная куча запутанного кода, который не подлежит рефакторингу. 
   1. Его остаётся лишь сжечь и просить богов о милости.
8. немного адаптивности не помешает?

<a id="Адаптивность"></a>
![image](https://github.com/burunyuu23/ImgOmg/assets/34377854/137c7e1c-56a7-465b-a0c8-5e36afba0a29)


<a id="Backend"></a>

## Backend:

<a id="Микросервис-1"></a>

### Микросервис для реги, автори и идентифи:
  - **FastAPI + uvicorn** (роутинг и запуск)
  - **psycopg2 + pydantic** (дб, бд и модели)
  - **PyJWT + bcrypt** (шифровка, проверка и генерация жвт)
  И куча всякой фигни. Надо бы реализовать всё на sqlalchemy, но крайний срок вчера сказал потом. 
  Кстати там к фастапи сваггер прилагается, так что пируем за чужой счет.
  
<a id="Микросервис-1-структура"></a>

  #### Структура:
  Есть класс **PostgreConn**, который принимает даннные для захода в бдшку и там всё колдует.
  1. **/user/signup**:
  - Регистрация. Нужно куча данных, которые инсертаются PC.insert_user. Пароль хешируется сразу.  Возвращает жвтшку.
  2. **/user/check**:
  - Возвращает данные о юзере, данные которого мы кинули ему на растерзание. Если чето вернулось проверяет пароли у pass_hash.py.
  3. **/user/login**:
  - Проверяет юзера предыдущим пунктом, если проходит проверку возвращает жвтшку на основе user.login + "/" + user.email.
  - Прикол в том, что в форме можно вводить либо почту либо логин, поэтому колхозим так.
  4. **/user/profile**:
  - Декодирует токен и селектает пользователя по декодированным данным (либо логин либо пошта)
  5. **/user/logout**:
  - Продолжаем колхозить, дамы и господа, поэтому возвращаем здесь пустой набор необходимых данных.
  6. ```python
      @app.get("/", dependencies=[Depends(jwtBearer())])
      async def pong():
          return {
              'id': 0,
              'name': 'John',
              'surname': 'Doe'
          }
      ```


<a id="Микросервис-2"></a>

### Микросервис для редактирования фото:
  - **Flask** (роутинг и запуск)
  - **PIL** (Цвета, обрезание, сжатие, наложение дрейнгенг эффекта и элегантного)
  - **cv2** (Кривое выгрызание фона)
  - **base64** (декодирование и кодирование картинок оттуда сюда)
  - **re, io, os, numpy, ...** (понятно)
  И куча всякой фигни. 
  Не успел реализовать сохранение картинок у пользователя в бдшке, чтобы можно было работы в профиле смотреть.
  > Ну и ладно
  
  <a id="Микросервис-2-структура"></a>
  
  #### Структура:
  Есть класс **Editor**, который переправляет запросы для каждого из модулей (цвет, размер, сжатие и приколы) и после обработки возвращает данные.
  1. **/upload**:
  - Собстна, загрузка фотографии в Едитор. 
  - Сначала декодирует картинку из base64 в PIL image.
  - Потом проходит по каждому модулю, там определяется че надо ченить или пофик скипаем.
  - Возвращается снова base64 из пил картинки.
  2. **/compress_size**:
  - Компрессирует и возвращает картинку и размер полученной картинки.
  - Помоему я забил на размер картинки и считаю её на фронте.
  3. **/pre_prikol**:
  - Прикалываемся, но не полностью.
  - Здесь мы рандомно прикалываемся из дрейн эффектов и выкидываем картинку и файл.
  - Файлом мы потом в аплоад заходим и гарантированно тот эффект который нам нужен применяем.
  Всё это приправленно криворукостью, неоптимизированным кодом и тихим ужасом, а иногда даже и громким.

<a id="База-данных"></a>

## Database:
  - Было бы странно увидеть здесь, что-то кроме **PostgreSQL**.
  - В нём две таблицы с юзерами и категориями юзеров.
  - Переменные окружения в **database.env**
  - Остальное в докер композе.
  - Кстати я перевёл постгру на алпину, но еще не запускал. Надеюсь оно будет нормально и не захватит заложников.

<a id="Nginx"></a>

## Nginx:
  - Пока что не знаю, что написать.

<a id="Запуск"></a>

# Запуск.
  **НИКАКИХ БОЛЬШЕ ПУНКТОВ!!!**
  
  <a>1.</a> Открываете терминал в рут папке проекта!
 
  <a>1.</a> Пишите `docker-compose up`
  
  <a>1.</a> Радуетесь!!!

******круто****

ставте пять звезд лайк и подписывайте на меня свои завещания. всем пока!
