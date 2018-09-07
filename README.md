# Coding challenge ETL

#####Requirements:
* Python3.x
* Postgres DB
* JSON-based document-oriented storage solution of your choice (MongoDB)

The short version:
We want you to build a server that converts an old-school, columnar data set into a JSON-based format, and store it in a NoSQL DB.

Now, this is where the fun starts; we have some specific requirements that we'd like this server to fulfill - we hope this will force you to think, make tough decisions and learn new stuff.
This is what we do at Seerene regularly, so this is also what we want to speak about when we talk about the code you send in. 

Completed challenges should be compressed in a zip file and sent to us by mail. Feel free to also contact us for any questions, clarifications or requests. 

Please do not post your completed challenge on a public repository - that wouldn't be a nice thing to do.

##### Expected behavior:
* The server will receive the connection details to a Postgres DB (host, credentials, database, table etc.) in an HTTP request.
* The server will check whether it can read the data in the table using the provided connection details.
* The server will then proceed to convert each entry in the table to JSON format and store each entry is in a document-oriented storage. 
* The server will reply with a 200 status immediately when the conversion to JSON has successfully started. Processing will happen in the background.

A non-200 response will be returned if the connection details provided do not allow the server to read data from the table or JSON conversion could not start for some reason.
The identifier for each entry in the document-oriented storage should be identical to the table's primary key.
The table's structure is unknown. You may assume that it will contain only basic types (int, float, char and boolean).

#### Expected practices:
Your code should be production-ready and we want to know what you consider to be production-ready. Feel free to cut corners, but be ready to explain them.
Assume your code will be maintained by other developers. Assume those other developers are armed and know where you live.
Please provide documentation for local deployment and server usage. Automated deployment is a nice bonus.
We will be testing your solution on several table formats - so should you.

Notes:
* We know you may not have worked with all the libraries, paradigms and solutions you will need to complete this test. That's OK, we want to see how you learn new stuff - it is an integral part of our day-to-day.
* You can ask for more time. You can cut corners. You can write bad code. You can do everything - but be ready to defend your choices.
* We are OK with scaffolding tools and pre-made templates, but please tell us what you used.
* Bonus points if you surprise us. What would be an awesome feature we haven't thought of?
