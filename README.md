# PERSONAL BLOG APP
## By `devjamesnjoroge`



## ABOUT

### A blog app where a writer can write their views and other users can comment on the blogs

## USER STORIES

A user can:
- view the blog posts on the site.
- comment on blog posts
- view the most recent posts.
- Receive an email alert when a new post is made by joining a subscription..
- see random quotes on the site.
- Submit a pitch in any category.
- View the different categories.

A writer can:
- sign in to the blog.
- create a blog from the application.
- delete comments that they find insulting or degrading.
- update or delete blogs I have created.

## TECHNOLOGIES USED

- HTML
- CSS
- PYTHON
- POSTGRESQL

## REQUIREMENTS

- Local machine
- A code editor e.g. VSCODE
- Installed postgresql

## INSTALLATION

```
git clone https://github.com/devjamesnjoroge/my-blog/
cd best-impressions
```

**Launch virtual environment**
```
python -m venv virtual

source virtual/bin/activate
```

**Install all the app dependencies**
```
pip install -r requirements.txt 
```

**Database Setup**
edit the sqlalchemy url in config.py
replace with your database in the format:
```
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

```
change the production string in manage.py to development

**Environmental variables**

Create a start.sh file in root folder 
Edit file
```
export SECRET_KEY=<YOURS>
export MAIL_USERNAME=<your email>
export MAIL_PASSWORD=<mail password>
python3 manage.py server
```

## AUTHORS INFO

* [Linkedin](https://www.linkedin.com/in/devjamesnjoroge)
* [Email](njorogehjames20@gmail.com)

## LICENSE

[MIT LICENSE](LICENSE)

[Go back to the top](#)

