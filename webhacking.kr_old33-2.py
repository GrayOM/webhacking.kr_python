import requests

url="https://webhacking.kr/challenge/bonus-6/lv2.php"

post_1_2 = {"post" : "hehe" , "post2" : "hehe2"} #post,post2 : 를통해 name : value 로 될수있음

re_post = requests.post(url,data=post_1_2) #data -> Post대한 매개변수

print(re_post.text)