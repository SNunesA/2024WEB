
python3 manage.py runserver
python3 
import django
exit()
deslogar e logar novamente
django-admin startproject nome do projeto
python3 manage.py runserver cria o arquivo db.sqlite que é o banco de dados

caso a porta 8000 esteja em uso
python3 manage.py runserver 8080

python3 manage.py startapp nome do app
vai em settings e coloca o app em instaled apps

depois que cria uma view, tem que atualizar a url do projeto
cria um urls.py pro app e atualiza tambem
atualiza o models do app

sempre que fizer uma atualizaçao tem que fazer as migrações com os comandos
python3 manage.py makemigrations 
python3 manage.py migrate

toda vez q criar um modulo
registra urls do modulo e projeto
habilita o app no settings.py do projeto
habilita o acesso do app no admin.py do modulo

habilita o crud pela interface do admin

python3 manage.py createsuperuser
conta SNunesA e senha aluno

criar modulos novos no models
atualizar no admin.py criando o register
e fazer migrações

manipulando django pelo terminal
python3 manage.py shell


DJANGO REST
python3 -m pip install django djangorestframework
habilitando no settings installed apps 
'rest_framework'
para cada apps coloca no settings

cria o serializer.py no app