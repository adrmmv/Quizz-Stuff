# Quizz-Stuff

## BUILD APP

Download docker: https://docs.docker.com/docker-for-windows/install/

```commandline
#Download and build dependencies
docker-compose build
#Start server
docker-compose up
```

Docker is started in port 5000 (localhost:5000)

## ENDPOINTS

### CREATE QUESTION

[POST]  host/create-quizz

**Request body**

```json
{
  "data" :{
      "question" : "blabla?",
      "answers" : [
      "ans_a",
      "ans_b",
      ...
      "ans_z"
      ],
      "correct-answer" : "ans_b"
  }
}
```

**Response Status**: 200 OK

### GET QUESTION

[GET]  host/get-question?id={idNumber}

**Response body**

```json
{
  "data" :{
      "question" : "blabla?",
      "answers" : [
      "ans_a",
      "ans_b",
      ...
      "ans_z"
      ],
      "correct-answer" : "ans_b"
  }
}
```

**Response Status**: 200 OK