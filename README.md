My name is Nenad Nikolic and I am a beginner in Python/Django world.

I am creating a Django project funtograph.



// Heroku Git push
// It will collectstatic automatically
cd nnpicksdj
git add -A
git commit -am "versionx"
git push heroku master

// Heroku issue a command to specific app
heroku <command> --app funtograph-dev

// Heroku migrate django models
heroku run python manage.py migrate --app funtograph-dev
heroku run python manage.py migrate --app funtograph-prod

// collect static files
heroku run python manage.py collectstatic

// Heroku status - you have to be in deployment directory
cd funtograph
heroku ps
heroku logs

//Heroku environment settings
heroku config:set S3_KEY=8N029N81
heroku config:set DJANGO_SETTINGS_MODULE=funtograph.settings.devheroku --app funtograph-dev
heroku config:set DJANGO_SETTINGS_MODULE=funtograph.settings.prodheroku --app funtograph-prod
heroku config:set SECRET_KEY="jdsjdsdhsjdh"

//Heroku check for problems
heroku run "python manage.py check" --app funtograph-dev

//Heroku add domain
heroku domains:add www.funtograph.com --app funtograph-dev

//Windows Powerhell environment variable setup
$env:DJANGO_SETTINGS_MODULE="nnpicksdj.settings.local"
//Windows cmd
set DJANGO_SETTINGS_MODULE=funtograph.settings.local

//Heroku maintenace mode
heroku maintenance:on --app funtograph-prod
heroku maintenance:off --app funtograph-prod

// requirements.txt - Heroku
1. Add this string without quotes to the end of requrements.txt. "-r requirements_heroku.txt" 2. Convert requirements.txt file in Notepad++ to Encoding > Encode in ANSI

// Hwow to remove already commited file from Git
git rm -r --cached .idea
-> update .gitignore
git commit -m "some text"
git push
