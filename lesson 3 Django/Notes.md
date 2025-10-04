# Django

- Used to make websites more dynamic as thing change in your web application

- The protocol that used for request/response is called http

HTTP Status Code

<ul>
    <li>200 --- OK </li>
    <li>301 --- Moved Permanently </li>
    <li>403 --- Forbidden </li>
    <li>404 --- Not Found </li>
    <li>500 --- Internal Server Error </li>
</ul>

Install django 

# Start a Django app

- python manage.py startapp <"name of the app">
- then you will have to add the installed app in the django project you created, in this case is "lesson3". Inside the settings.py under the "INSTALLED_APPS" section, add the "name of the app" you created, in this case it is "hello" 

# Need to create a urls file in the new app created "hello"

- used to tell django when a particular function should run

# CSRF verification

- whenever we are submitting sensitive information, we need to make sure that the data is secure using the auto generated token from CsrfViewMiddleware in the 'MIDDLEWARE' section in the projects settings.py file 

# Summary 

- So now we've really just scratched the surface of what Django has to offer.
But we see now the ability it has to be able to create dynamic web
applications.
Instead of just displaying HTML and CSS that's the same every time,
using Django, we now have the ability to be
able to generate programmatically custom HTML and CSS, either saying hello
to a person's name based on what name is provided inside of URL,
or the ability to say-- to check the current date
and conditionally display something if the date is one thing versus another,
and the ability to store data on a session basis,
to be able to store information about a user's to do list,
for example, such that on subsequent visits,
they can see their list of things they need
to do with a different list for each of these possible users.
And here really is just the beginning of where Django has to offer.
Where Django gets very powerful is when it comes towards storing data inside
of databases, and manipulating that data,
and interacting with that data in various different ways.
And that's ultimately where a lot of the power of a web framework like this
ultimately comes in.
We'll explore more of that next time.
But for now, that was just a look at Django
and how we can use it to be able to build these sorts of web applications.
This was "Web Programming with Python and JavaScript."
We'll see you next time.

