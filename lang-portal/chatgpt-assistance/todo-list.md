# TODO List for Language Learning Portal Backend API

## Backend Implementation

### Routes
- [ ] Implement GET /words
  - [ ] Add pagination support (default: page 1)
  - [ ] Add sorting by 'thai', 'english', 'correct_count', 'wrong_count' (default: 'thai')
  - [ ] Add order support ('asc' or 'desc', default: 'asc')
- [ ] Implement GET /groups
  - [ ] Add pagination support (default: page 1)
  - [ ] Add sorting by 'name', 'words_count' (default: 'name')
  - [ ] Add order support ('asc' or 'desc', default: 'asc')
- [ ] Implement GET /groups/:id
  - [ ] Add pagination support (default: page 1)
  - [ ] Add sorting by 'name', 'words_count' (default: 'name')
  - [ ] Add order support ('asc' or 'desc', default: 'asc')
- [ ] Implement POST /study_sessions
  - [ ] Accept `group_id` (required)
  - [ ] Accept `study_activity_id` (required)
- [ ] Implement POST /study_sessions/:id/review
  - [ ] Log review attempt for a word during a study session

### Database Setup
- [ ] Verify database schema matches models
  - [ ] `words` table
    - [ ] `id` (Primary Key)
    - [ ] `thai` (String, Required)
    - [ ] `english` (String, Required)
    - [ ] `parts` (JSON, Required)
  - [ ] `groups` table
    - [ ] `id` (Primary Key)
    - [ ] `name` (String, Required)
    - [ ] `words_count` (Integer, Default: 0)
  - [ ] `word_groups` table
    - [ ] `word_id` (Foreign Key)
    - [ ] `group_id` (Foreign Key)
  - [ ] `study_activities` table
    - [ ] `id` (Primary Key)
    - [ ] `name` (String, Required)
    - [ ] `url` (String, Required)
  - [ ] `study_sessions` table
    - [ ] `id` (Primary Key)
    - [ ] `group_id` (Foreign Key)
    - [ ] `study_activity_id` (Foreign Key)
    - [ ] `created_at` (Timestamp, Default: Current Time)
  - [ ] `word_review_items` table
    - [ ] `id` (Primary Key)
    - [ ] `word_id` (Foreign Key)
    - [ ] `study_session_id` (Foreign Key)
    - [ ] `correct` (Boolean, Required)
    - [ ] `created_at` (Timestamp, Default: Current Time)

### Relationships
- [ ] Ensure relationships are correctly set up
  - [ ] `word` belongs to `groups` through `word_groups`
  - [ ] `group` belongs to `words` through `word_groups`
  - [ ] `session` belongs to a `group`
  - [ ] `session` belongs to a `study_activity`
  - [ ] `session` has many `word_review_items`
  - [ ] `word_review_item` belongs to a `study_session`
  - [ ] `word_review_item` belongs to a `word`

## Frontend Integration
- [ ] Set up HTTP requests in frontend to call backend APIs
- [ ] Handle backend responses correctly in frontend

## Testing and Debugging
- [ ] Write unit tests for backend using `pytest`
  - [ ] Test all endpoints
  - [ ] Test database operations
- [ ] Thoroughly test frontend interactions with backend

## Deployment
- [ ] Set up deployment pipeline for frontend and backend
  - [ ] Dockerize the application
  - [ ] Set up CI/CD pipelines

## Documentation
- [ ] Document all parts of the application
  - [ ] API documentation
  - [ ] Setup instructions
  - [ ] Usage guides