## Task:

### Implement an API endpoint for the scenario below:

- Imagine that a frontend design has been drafted to present data that we already have in our DB: `Posts` and `Comments`. 

  * The design is an infinite scrolling list of `Posts`.

- The list of `Posts` should be ordered by timestamp, latest first. 

- Some `Posts` will have `Comments`. 

- For each `Post` in this list, we want to show up to 3 `Comments` for that `Post` (`Comments` also sorted latest first).

  * For each `Post`: we will need to display a `Post`'s text, timestamp, `Comment` count, and author's username.

  * For `Comments`: we will need to display a `Comment`'s text, timestamp, and author's username.

- Include basic documentation on how to use your new endpoint.

### Follow-up Q: 
- Instead of sorting comments by timestamp, how would you fetch 3 random comments associated to a given post?
  * You can leave your answer anywhere in the project codebase that you deem appropriate.

---

## To get started:

1. Set up a virtualenv for this project (The author used Python 3.10.14)

- Example: `pyenv local myvirtualenv` (or however you set up Python virtualenvs)

2. Install dependencies: `pip install -r requirements.txt`

3. Migrate database `python manage.py migrate`

4. Now head to apps/demo/views.py and complete the assignment!

- Run tests via `python manage.py test apps` or
- check server after running via `python manage.py runserver`



# Posts API Endpoint Documentation

## Endpoint Overview
This API endpoint provides a list of `Posts` with pagination and the ability to fetch up to 3 `Comments` for each post, with flexible ordering options.

### Base URL
`/posts/`

## Query Parameters

### `comment_mode` (optional)
Defines how comments for each post should be ordered.

**Possible Values:**
- `latest` (default): Comments are ordered by their timestamp in descending order.
- `random`: Comments are fetched randomly.

### `order_mode` (optional)
Defines how the posts are ordered.

**Possible Values:**
- `latest` (default): Posts are ordered by their timestamp in descending order.
- `random`: Posts are fetched randomly.

## Response Structure

Each post in the response includes the following fields:

### Post Fields
- **`id`**: Unique identifier for the post
- **`text`**: Content of the post
- **`timestamp`**: Timestamp of post creation
- **`author_username`**: Username of the post's author
- **`comment_count`**: Total number of comments associated with the post
- **`comments`**: List of up to 3 comments for the post

### Comment Fields
Each comment contains:
- **`id`**: Unique identifier for the comment
- **`text`**: Content of the comment
- **`timestamp`**: Timestamp of comment creation
- **`author_username`**: Username of the comment's author

## Example Request
```bash
GET /posts/?comment_mode=latest&order_mode=latest
```

## Example Response
```json
[
  {
    "id": 1,
    "text": "This is a post",
    "timestamp": "2024-11-21T10:00:00Z",
    "author_username": "john_doe",
    "comments": [
      {
        "id": 1,
        "text": "Great post!",
        "timestamp": "2024-11-21T10:10:00Z",
        "author_username": "jane_doe"
      },
      {
        "id": 2,
        "text": "I agree!",
        "timestamp": "2024-11-21T10:15:00Z",
        "author_username": "bob_smith"
      },
      {
        "id": 3,
        "text": "Very insightful.",
        "timestamp": "2024-11-21T10:20:00Z",
        "author_username": "alice_williams"
      }
    ],
    "comment_count": 5
  }
]
```

## Integration Guidelines

### 1. Pagination
- Uses `CursorPagination` class
- Returns 10 posts per page
- Use `cursor` parameter for navigation
- Ideal for infinite scrolling implementations

### 2. Ordering
- `order_mode` controls post ordering:
  - Default is timestamp-based (latest first)
  - Can be set to random selection
- `comment_mode` controls comment ordering:
  - Default is timestamp-based (latest first)
  - Can be set to random selection

### 3. Performance Optimization
- Comments are pre-fetched using Django's `Prefetch`
- Maximum of 3 comments returned per post to minimize payload size

## Potential Use Cases
- Social media feed
- Blog post listings
- Discussion forum post retrieval

## Notes
- Always include error handling for API calls
- Be prepared to handle pagination in client-side code
- Respect rate limiting and backend constraints


