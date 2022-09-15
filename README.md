# 📜Blog Site using Flask & Jinja of Python

🌟A basic Blog Website created using HTML & CSS for design and Python Flask as the backend. In order to avoid creating new HTML file for each post, the use of templating 
is done with Jinja. This helps load different posts with same design template by passing parameters and phrasing the url for these pages.

👉In the 'index.html' and 'post.html' files, the website structure is defined. Using the 'styles.css' file, the fonts, blocks, page design is added. As of yet, no contents
are added to the files.

👉In the 'main.py' file, the Flask framework is imported to run a local server to host the website. Using the Flask decorator functions the website routes are created.

👉Now, in the home route(/) the contents of blogsite are fetched using the requests module to make GET request to a api which returns simple blog contents. The response
is stored in json format, equivalent to Pyhton dictionaries.

👉This acquired data is now passed to the html file to render the contents. The 'render_templates()' method is used to render the respestive html files and the contents of
website are passed as parameter during this function call.

👉In the 'index.html' file,  Jinja templating is used to render the contents passesd as parameter in above function call. The use of syntax : '{{ }}' is done to add Python
code in html file and this allows to render all the contents from passed parameter using Python for loops, if-else conditions etc.

![Home Page](https://github.com/bellaryyash23/Blog_Flask_Jinja_1/blob/master/samples/site.jpg?raw=true)

👆Home Page of Blog site rendered using Jinja👆

👉Now, each Blog post can be further expanded into its subsequent web-page. This functionaliy is added using Jinja. When a user presses to expand a post a function call
is generated because of the 'url_for()' method of Jinja which calls the respective function from the 'main.py' file. In this function call, the parameter like the blog id
also gets passed. All this is from the 'index.html' file.

👉Next this passed parameter is caught in the respective function and also by the Flask decorator function to build a url for each different post. This makes rendering 
posts with same body style but different contents on different urls possisble.

👉Similar to the 'index.html' route function, the api call is generated and data is fetched and passed as parameter to the 'post.html' file. Then Jinja is used to render
the contents but, this time the blog id is used as a condition and only the post matching that id gets rendered. This id is also visible in the designed url for the post.

![Posts Page](https://github.com/bellaryyash23/Blog_Flask_Jinja_1/blob/master/samples/post.jpg?raw=true)

👆Post Page of a particular Blog👆

👉Thus the overall working of the website can be see as follows, where how the url and contents get dynamically loaded and none of the html files are hard coded texts.

![Blog site Working](https://github.com/bellaryyash23/Blog_Flask_Jinja_1/blob/master/samples/site.gif?raw=true)

👆Final Blog Site Working👆

(Note: This is the part 1 of project being created all new parts will be created in diiferent repos consecutively.)
