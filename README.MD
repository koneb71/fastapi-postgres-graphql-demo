# FastAPI + PostgreSQL + Graphql

### Database
- Users
  - name
  - address
  - phone_number
  - sex
  - timestamps
- Posts
  - user_id
  - title
  - body
  - timestamps
- Comments
  - user_id
  - post_id
  - body
  - timestamps
### Setup
Update Database information in `db.py`

```shell
pip install -r requirements.txt
orator migrate -c db.py
```

### Run
```shell
uvicorn main:app --reload
```


### GraphQL

#### Create user
```
mutation createUser {
  createUser(userDetails: {
    name: "Care",
    address: "Test Address",
    phoneNumber: "1234",
    sex: "male"
  })
  {
    id
    name
    posts {
      body
      comments {
        body
      }
    }
  }
}
```

#### Create Post
```
mutation createPost {
  createPost(postDetails: {
    userId: 2,
    title: "My first Post",
    body: "This is a Post"
  })
  {
    id
  }
}
```

#### Create Post Comment
```
mutation createComment {
  createComment(commentDetails: {
    userId: 2,
    postId: 1,
    body: "Another Comment"
  })
  {
    id
    body
  }
}
```

#### Get All Users
```
query getAllUsers {
  listUsers {
    id
    name
    posts {
      title
    }
  }
}
```

#### Get user
```
query getUser {
  getSingleUser(userId: 2) {
    name
    posts {
      title
      comments {
        body
      }
    }
    comments {
      body
    }
  }
}
```