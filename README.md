SETUP INSTRUCTIONS:

I. About the library being used in the project, they all are available to be installed,
use command "pip install " + library-name to install lacking libraries OR instead we can install libraries
by using file requirement.txt with command 'pip install -r requirement.txt'

II. To start the application: run cmd: "flask --app blog_post run"

III. For database initiation: I already created, so just use the existing one, if there is any issue, lets delete
file inside path: migrations/versions/... and then un commands: 'flask --app blog_post db migrate' =>
'flask --app blog_post db upgrade'


=======================================================================================================
ABOUT THE IDEA FOR DESIGNING APPLICATION:

1. User who is able to sign in to application is also author of blog post therefor, when they query blog post,
they can only work with their posts

2. About the authentication: I use JWT as the token to authenticate between client and server because it's much
secured than using basic authen, and password being saved in db is encrypted. Whenever we want to call API, we have to set header
with key - value: Authorization-Bearer + 'token' with 'token' is the returned value when we call api login: '/api/auth/login'. 
This API will return 'access_token' for authenticating API and "refresh_token" to serve for
function changing password or logout(those functions could be implemented later)

3. For better API design, I use blueprint to register different groups of API. In each group(auth, blog_post),
'routes.py' contains API, 'utils.py' handle logic, 'schemas.py' is for validation

4. For handling exception, I create exception handlers for different types of exception

5. For validating, I use marshmallow library

6. Also leave comments while writing code for easy understanding and when I update a blog post, I use deepdiff
to find the differences and log them

7. For DB, I choose sqlite because when application scale up, we with have many complicated constraints among
table, and I use AQLAchemy to interact with DB. For current application: relationship between 'user' and 'blog-post'
is 'one to many'

8. Endpoint List:
   - login: 
     + Method: POST
     + Endpoint: /api/auth/login
     + Payload example:
      {
         "email": "user1@gmail.com",
         "password": "test"
      }
   
   - sign up: 
     + Method: Post
     + Endpoint:/api/auth/sign-up
     + Payload example:
      {
         "email": "user1@gmail.com",
         "password": "test"
      }
     
   - Creating a new blog post: 
     + Method: Post
     + Endpoint: /api/blog-post/
     + Payload example:
      {
          "content": "Content one update",
          "title": "Title one"
      }
     
   - Update a new blog post: 
     + Method: Post
     + Endpoint: /api/blog-post/
     + Payload example:
      {
          "content": "Content one update",
          "id": 4,
          "title": "Title one"
      }
     
   - Find all the blog posts: 
     + Method: Get
     + Endpoint: /api/blog-post/

   - Find blog post by id: 
     + Method: Get
     + Endpoint: /api/blog-post/<id>
   
   - Delete blog post by id: 
     + Method: Delete
     + Endpoint: /api/blog-post/<id>
   
   #   b l o g - p o s t - a p i  
 