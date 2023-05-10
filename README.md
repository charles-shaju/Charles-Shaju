- 👋 Hi, I'm currently making breaking and healing my code.
- 👀 I’m interested in ML and Cyber Security.
- 🌱 I’m currently learning ML and Datascience.
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me [Twitter](www.twitter.com/@Mr___CS)

<!---
Charles-Shaju/Charles-Shaju is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

Create a sample Database and create 'restaurants' collection using MongoDB. Then insert the following values.

restaurant_id

name

cuisine

borough

zipcode

30075445

Morris Park Bake Shop

bakery

Bronx

10462

Code

> use sample

switched to db sample

> db.createCollection("restaurants")

{ "ok" : 1 }

> db.restuarants.insert({"restaurantid":"30075445","name":"Morris park bake shop","cuisine":"Bakery","borough":"bronx","zipcode":"10462"})

WriteResult({ "nInserted" : 1 })

> db.restuarants.find().pretty()

{

        "_id" : ObjectId("6181cdf88d7ae7258d1a1b46"),

        "restaurantid" : "30075445",

        "name" : "Morris park bake shop",

        "cuisine" : "Bakery",

        "borough" : "bronx",

        "zipcode" : "10462"

}

Create a sample Database and create 'university' collection using MongoDB. Then insert the following values.

country

city

name

students

year

number

spain

salamanca

usal

2014

24774

 

 

 

2015

23166

 

 

 

2016

21913

code

      >db.university.insert({"country":"spain","city":"salamanca","name":"usal","students":[{"year":"2014","number":"24774"},{"year":"2015","number":"23166"},{"year":"2016","number":"21913"}]})

WriteResult({ "nInserted" : 1 })

> db.university.find().pretty()

{

        "_id" : ObjectId("6181d1ba8d7ae7258d1a1b47"),

        "country" : "spain",

        "city" : "salamanca",

        "name" : "usal",

        "students" : [

                {

                        "year" : "2014",

                        "number" : "24774"

                },

                {

                        "year" : "2015",

                        "number" : "23166"

                },

                {

                        "year" : "2016",

                        "number" : "21913"

                }

        ]

}

Insert the following documents into a “posts” collection.

username : GoodGuyGreg

title : Passes out at party

body : Wakes up early and cleans house

username : GoodGuyGreg

title : Steals your identity

body : Raises your credit score

username : GoodGuyGreg

title : Reports a bug in your code

body : Sends you a Pull Request

Answer the following query:

Sort the documents based on the ‘title’ in descending order

Delete one document from the collection.

Code

> db.posts.insert([

... {

... "username":"GoodGuyGreg",

... "title":"Passed out at party",

... "body":"Wakes up early and cleans house"

... },

... {

... "username":"GoodGuyGreg",

... "title":"Steals your identity",

... "body":"Raises your credit score"

... },

... {

... "username":"GoodGuyGreg",

... "title":"Reports a bug in your code",

... "body":"Sends you a pull request"

... }

...] )

> db.posts.find().pretty()

> db.posts.find().pretty().sort({"title":-1})

> db.posts.remove({"title":"Passed out at party"})

Consider a sample collection and count the number documents in a collection, delete a particular document.

>db.students.insertMany([

{ “_id”:”1001”, “test1”:”95”, “test2”:”92”,” test3”: “90” }

	{“_id”:”1002”, “test1”:” 98”, “test2”: “100”,” test3”: “102” }

	{“_id”:”1003”,”test1”:”95”,”test2”:”110”,”test3”:”108”}

])

>db.students.find().pretty()

>db.students.count()

>db.students.remove({“_id”:”1002”})

>db.students.find().pretty()

