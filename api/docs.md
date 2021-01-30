# Introduction

The api subproject for sophia.


# Needs:
In this section, all needs are defined.
Only need defined here will be counted.

## Course

- Courses

`GET /api/courses`

Return a course list. In the backend, files for each course
are stored in a git repository. So the course list is
acctually repo list.

```json
  {
    'message': '',
    'data':[{
      'course_name': 'math'
    }],
    'code': 200
  }
```

`POST /api/courses`

Create a new course. In the backend, a git repo is created.
The user_id is used to query user info in a database so as
to store author info in git repo.

Data required:
```json
  {
    'course_name': 'advanced math',
    'user_id': 123456
  }
```

- Metadata for each Course.

`GET /api/course/<course_name>`

`course_name` is unique and is used to locate one course.
More course metadata will be stored in database.

```json
{
  'message': '',
  'data': {
    'description': 'an awesome math course.'
  },
  'code': 200
}
```

- Files for one Course

`GET /api/course/<course_name>/chapters`

The chapters is actully some files stored in the git repo.
This endpoint only returns the entories for this tree:
`HEAD->commit->tree`. If you want change into an dir,
you should use `sha` of a tree object to query the api.

```json
{
  message: '',
  'data':[{
    'file_name': 'An Introduction to math.md',
    'file_type': 'blob',
    'sha': '6e4f5d2612c4e3b371d7aa8b66ea6ef0050840dd'
  },
  {
    'file_name': 'imags',
    'file_type': 'tree',
    'sha': '4145a84554929211bd84da6c51a6853ba3587137'
  }
  ],
}
```
`Post /api/course/<course_name>/chapters`
Create a new file for the repo, aka created a new chapter
for the course.

Data required:
```json
{
  'file_name': 'Set Theory.md',
  'content': '# Introduction to set Theory\n What kind of set can you list in our life...',
  'user_id': 654321
}
```

- Content for each File.

`GET /api/course/<course_name>/chapter/<chapter_name>`

Return content of a chapter.
```json
{
  'message':'',
  'data':{
    'file_name': 'Set Theory.md',
    'content': '# Introduction to set Theory\n What kind of set can you list in our life...'
  },
  'code': 200
}
```

`PUT /api/course/<course_name>/chapter/<chapter_name>`

:construction:​

Change some content of a chapter. The changed content is required. The changes will be pushed into a stage area. 
The course manager will decide whether to accept this change.

```json
{
  'file_name': 'Set Theory.md',
  'content': '# Introduction to set Theory\n What kind of set can you find in our life...',
  'user_id': 654322
}
```

`PATCH /api/course/<course_name>/chapter/<chapter_name>`

:construction:​

This endpoint is designed for course manager to decide
whether to accept a request or not. This function is
similar to pull request.

The endpoint is not designed well.

## User

