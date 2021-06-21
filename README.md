Django CRUD
READ: https://github.com/Rakeshpandithts/Django_CRUD_DOCKER_Postgres/blob/main/ReadME.pdf

*To Run the project inside project directory run
 docker-compose up
Testing:
For Swagger dashboard http://127.0.0.1:8000/assignment/swagger/


	For api testing I used Postman and Swagger
I am adding those test screenshots here.
Create Assignment
Post http://127.0.0.1:8000/assignment/create/
Input =
{
    "name": "Social",
    "title": "Panipat",
    "description": "This assignment is from chapter 1 and 10",
    "type": "Multiple choice",
    "duration": "02:00:00",
    "tags": [  "Social",   "Multiple"]
}
Output 
Success =  {'message': 'success' }
Bad Request =  {"error": "There was a problem in request data"}, 	    		status=status.HTTP_400_BAD_REQUEST
	

   Get Assignment by id
GET http://127.0.0.1:8000/assignment/id={id}/
Input = {id}
Example = Id = {2}
Output 
Success = { "id": 2,  "name": "Maths", "title": "Linear Algebra",  "description": "This assignment is from chapter 1", "type": "Multiple choice", "duration": "06:00:00", "tags": [ "Maths", "Multiple"]}
Not Found = ( {"error": "Data Not found"},  status=status.HTTP_404_NOT_FOUND)
	
Get Assignments by tag
GET http://127.0.0.1:8000/assignment/tag={tag}/
Input = {tag}
Example  = tag = {Maths}
Output 
Success = [ { "id": 2,   "name": "Maths", "title": "Linear Algebra", "description": "This assignment is from chapter 1", "type": "Multiple choice", "duration": "06:00:00", "tags": [  "Maths", "Multiple"] },  { "id": 3,   "name": "Maths", "title": "Algebra", "description": "This assignment is from chapter 1 and 3", "type": "Multiple choice", "duration": "06:00:00",  "tags": ["Maths", "Multiple"] }]
Not Found = ( {"error": "Data Not found"},  status=status.HTTP_404_NOT_FOUND)


Database Schema:
Here I used Postgress DB for the assignment

Database schema diagram: https://drawsql.app/rakesh/diagrams/assignment


