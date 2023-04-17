Source for the Blog

Workflow:
----
 - Test stuff locally
 - run "pelican content" without defining SITE_URL
 - keep changes to output/content in separate commits than ones to:
   - any config files
   - posts
   - tests

Directories:
----

 - content/
   - symlinks to posts in posts/
   - cd content; python MAKESYMLINKS.py
 - Makefile
 - output/
   - generated from `pelican content`
 - pelicanconf.py
 - posts/
   - the posts are in here sorted by year
   - there's also a MODIFYTAGS.py here that was used to modify all the posts
 - publishconf.py
 - requirements.txt
 - security.txt
 - tag/
 - tasks.py
 - tests/
   - To Be Added:
     - Ensure only symlinks in content/
	 - Moar
	 - Profit
