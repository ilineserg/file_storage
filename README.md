## Хранилище файлов с доступом по http

### Задание
Реализовать демон, который предоставит HTTP API для загрузки (upload) ,
скачивания (download) и удаления (delete) файлов.

##### Upload:
Получив файл от клиента, демон возвращает в отдельном поле http
response хэш загруженного файла демон сохраняет файл на диск в следующую структуру каталогов:

store/ab/abcdef12345..., где 
* "abcdef12345..." - имя файла, совпадающее с его хэшем.
* /ab/  - подкаталог, состоящий из первых двух символов хэша файла.
* Алгоритм хэширования - на ваш выбор.

##### Download:
Запрос на скачивание: клиент передаёт параметр - хэш файла. Демон ищет
файл в локальном хранилище и отдаёт его, если находит.

##### Delete:
Запрос на удаление: клиент передаёт параметр - хэш файла. Демон ищет
файл в локальном хранилище и удаляет его, если находит.


#### Реализация
##### Запросы
###### Список файлов
GET /files - Список сохраненных файлов(JSON)
###### Upload
POST /file/

Пример запроса с помощью утилиты curl:
 
    curl -i -X POST -- form file=@/путь/к/файлу http://hostname/file/ --insecure

###### Download
GET /file/filename_like_hash, где
* filename_like_hash - имя файла, совпадающее с хэшем файла (длина 32 символа)

###### Delete
DELETE /file/filename_like_hash, где
* filename_like_hash - имя файла, совпадающее с хэшем файла (длина 32 символа)

