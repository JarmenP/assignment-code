step1
	Install virtualenv and virtualenvwrapper¶
	pip install virtualenvwrapper-win
	mkvirtualenv myproject
	workon myproject
step2
	pip install -r requrements.txt

step3
	data dump to db for that run below command
	python data_dump.py
	
stpe4
	python manage,py runserver 