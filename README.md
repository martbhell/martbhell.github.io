Source for the Blog where I blog about IT, Finnish Things and sometimes about Storage (but not so much anymore on this topic).

Workflow:
----
   - Test stuff locally with `pelican -l`
   - run `pelican content` without defining `SITE_URL`
     - in cloudflare deploy we set it to https://guldmyr.com
     - having it unset makes links work when developing locally
   - keep changes to output/content in separate commits than ones to:
     - any config files
     - posts
     - tests
   - merge request
     - sets up a preview page in cloudflare pages
     - when it looks OK merge yo

Directories:
----

   - content/
     - symlinks to posts in posts/
     - cd content; python MAKESYMLINKS.py
   - Makefile
   - output/
     - generated from `pelican content` and most of it should not be commited 
       as it's being built on every deploy in cloudflare
   - output/images
     - these are needed
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
