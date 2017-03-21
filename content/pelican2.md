Title: Створюємо простий блог за допомогою Pelican (Частина 2)
Slug: pelican2
Lang: uk
Date: 2017-02-08
Category: Web
Tags: web, python, pelican
Status: draft

Встановлення.

Встановлюється Pelican просто, за умови якщо у Вас інстальовано Python . Якщо у Вас  Mac чи Linux, ви вже маєте Python встановленим. Якщо ж у Вас Windows, то його треба встановити. Pelican підтримується Python 2.7.x or 3.3+,  таким чином ви можете обирати. В мене Ubuntu та встановлено обидві версії Python.  Далі все описано саме для Ubuntu. 

Саме встановлення Pelican  напрочуд просте:

```
> pip install pelican Markdown
```

Далі вам потрібно створити  каталог, де буде  розташовано блог. В мене це:
```
~/datablog/
```

 У вас, наприклад, хай це буде 
 ```
 ~/myblog/
 ```
    
    
```
mkdir ~/myblog/
cd  ~/myblog/
pelican-quickstart
```

Остання команда запускає скрипт першого налаштування блога. І хоча там немає нічого складного, я наведу відповіді:

```
> Where do you want to create your new web site? [.] .
> What will be the title of this web site? Test Pelican blog
> Who will be the author of this web site? username
> What will be the default language of this web site? [en] ru
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y             
> What is your URL prefix? (see above example; no trailing slash) https://example.com
> Do you want to enable article pagination? (Y/n) y
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] Europe/Kiev
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> What is the name of your S3 bucket? [my_s3_bucket] example.com
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) n
Done. Your new project is available at /home/username/pelicanblog
```

Після того, як скрипт pelican-quickstart відпрацює, структура каталогу буде виглядати наступним чином:

```
.
├── content
├── develop_server.sh
├── fabfile.py
├── include
├── lib
├── local
├── Makefile
├── output
├── pelicanconf.py
├── pelicanconf.pyc
└── publishconf.py
```


Додамо перший запис у блог. Для записів блогу використовується каталог content. Переходим в нього:

``` 
> cd content 

```


Cтворюємо файл з нашим першим записом у любому текстовому редакторі:

```
> vim first.md

```


Дописуємо туди наступні строчки:

```markdown
Title: Перший запис!
Date: 2017-002-20 
Author: username
Category: Some_Category
Tags: test, blog
Slug: first
Status: published

Зміст запису...
```

Опис параметрів заголовку статті:

| Параметр         | Опис                                                    |
|------------------|---------------------------------------------------------|
| Title            | Назва статті                                            |
| Date             | Дата публікації                                         |
| Category         | Категорія статті                                        |
| Tags             | Теги статті через кому                                  |
| Slug             | URL статті                                              |
| Status           | статус статті: draft - чорновик, published - публікація |




Генерація блогу

Каталог з блогом також містить Makefile, в якому вже створено команди для роботи з блогом. Сгенеруєм з їх допомогою:

```
> make html
pelican /home/alex/Datablog/content -o /home/alex/Datablog/output -s /home/alex/Datablog/pelicanconf.py 
WARNING: JINJA_EXTENSIONS setting has been deprecated, moving it to JINJA_ENVIRONMENT setting.
WARNING: Unable to find `./writing.md`, skipping url replacement.
Done: Processed 1 article, 0 drafts, 2 pages and 0 hidden pages in 0.36 seconds.
```


Запустимо локальний веб-сервер и подивимся що вийшло:

```
> make serve

```


