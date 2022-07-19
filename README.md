# ArabiansDevWorld 👌
[README EN](translation/README_en.md)
```
هذا المشروع هو طموح لانشاء اكبر منصة لتجمع المطورين العرب
ومهندسي الحاسب الآلي من حول العالم
لنشر خبراتهم ومساعدة المقدمين علي دخول مجال البرمجة وهندسة الحاسوب
وتعزيز المحتوي العربي التقني علي الانترنت
```

سوف اقوم بناء هذا المشروع باستخدام مبادئ  الخدمات المصغرة `Microservices`

---
سوف اقوم بعمل مشروع خاص بي العميل `Client`  وهو مسئول عن عرض البيانات من ال `APIs`

وبالطبع انشاء مشروع `APIs`

### user_read_api : URLs
```shell
GET:     users/list       `Admin only`
GET:     users/<username>
```
### user_write_api : URLs
```shell
POST:     users/list       `Admin only`
PUT:      users/<username>
POST:     token            `genration token`
POST:     token/refresh    `Refresh token`
```

### feed_read_api : URLs
```shell
GET:      feed/                         `View All Posts`
GET:      feed/<post_slug>-<post_id>    `Read Post`
```

### feed_write_api : URLs
```shell
POST:     feed/                         `View All Posts`
PUT:      feed/<post_slug>-<post_id>    `Update Post`
DELETE:   feed/<post_slug>-<post_id>    `Delete Post`
```
