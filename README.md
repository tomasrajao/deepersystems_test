# Instructions to install

### Installing dependencies

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Building Docker image and create a container (Mongo)

```
docker pull mongo
docker run --name mongo-container -d -p 27017:27017 mongo_db
```

### To run the application

```
python app.py
```
(available at localhost:5000)



### Import udata.json with parser.py

```
python parser.py
```

### Running Frontend

```
cd frontend
nvm use 18.20 
npm install
npm run dev
```
(available at localhost:5173)


### Available endpoints

GET localhost:5000/users - List users \
POST localhost:5000/users - Create user\
GET localhost:5000/users/<id> - Retrieve a specific user\
PUT localhost:5000/users/<id> - Update a user\
DELETE localhost:5000/users/<id> - Delete a user

