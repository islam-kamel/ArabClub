# Changelog ๐

All notable changes to this is App will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [Unreleased]

### Added โ

- Now users can personalize and settings their profile.
- Users can login with username, email
- add more forms to admin panel for staff and admin

### Fixed โ๏ธ

- Fixed normalize username
- Add Relations ship info  for user
- Fixed Null value in user tables

## [1.0.0]

### Added โ

- create endpoint for Update **_"first name, last name"_** for user
- create endpoint for update **_"username, email, date_of_birth"_** for user
- create endpoint for update _**"bio"**_
- create endpoint for Update **_"github url"_** for user
- create endpoint for update **_"address"_** for user
- create endpoint for update **_"skills"_** for user

### Fixedโ๏ธ

- Fixed get all data for user


### Feature ๐งโ๐ป
- **_update user info_** ๐ค
```json
endpint_url = "http://127.0.0.1:8000/account/user/<username>"
allowed_metho = ["GET", "PUT"]
{
    "id": 1,
    "usrname": "islam.admin",
    "email": "islam@admin.com",
    "date_of_birth": "1998-08-30"
}
```
---
- **_update person info_** ๐ง
```json
endpint_url = "http://127.0.0.1:8000/account/user/<username>/person-info"
allowed_method = ["GET", "PUT"]
{
    "first_name": "Islam",
    "last_name": "Kamel"
}
```
---
- **_update bio_** โน๏ธ
```json
endpint_url = "http://127.0.0.1:8000/account/user/<username>/bio"
allowed_method = ["GET", "PUT"]
{
    "bio": "Hello World"
}
```
---
- **_update skills_** ๐คน
```json
endpint_url = "http://127.0.0.1:8000/account/user/<username>/skills"
allowed_method = ["GET", "PUT"]
[
    {
        "id": 1,
        "skill_name": "Python",
        "user_id": 1
    },
    {
        "id": 2,
        "skill_name": "Docker",
        "user_id": 1
    },
    {
        "id": 3,
        "skill_name": "ReactJs",
        "user_id": 1
    }
]
```
---
- **_update GitHub Account_** ๐งพ
```json
endpint_url = "http://127.0.0.1:8000/account/user/<username>/github"
allowed_method = ["GET", "PUT"]

{
    "url": "https://www.github.com/",
    "user_id": 1
}
```
---
- **_update Phone Number_** ๐ค
```json
endpint_url = "http://127.0.0.1:8000/account/user/<username>/phone"
allowed_method = ["GET", "PUT"]

{
    "phone": "01XXXXXXXXXXX",
    "user_id": 1
}
```

## [1.0.1]

### Added โ

- create one endpoint for Update or create  **_" All data "_** for user

### Fixedโ๏ธ

- Fixed skills relationship
- Fixed user data serializer
- Fixed update data
- Fixed user details view
- Fixed list all users view for admin only
- Fixed Validate username and phone

### Feature ๐งโ๐ป
**_``One url to view all user data and change or add new data [GET, PUT]
Methods ๐``_**

- new endpoint url ``/account/user/islam.admin/`` I/O

```json
    {
        "id": 1,
        "name": {
            "first_name": "Islam",
            "last_name": "Kamel"
        },
        "username": "islam_admin",
        "email": "islam@admin.eg",
        "date_of_birth": "1998-06-13",
        "bio": {
            "bio": "Hello, Firend"
        },
        "skills": {
            "skill_name": "python"
        },
        "github_url": {
            "url": "https://github.com/"
        },
        "phone": {
            "phone": "01066373279"
        },
        "address": {
            "country": "Egypt",
            "city": "qus",
            "street_name": "Qus"
        }
    }
```
