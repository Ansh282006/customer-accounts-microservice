# User Story Template

Use this template for every user story in the project.

## Story

**As a** `<role>`
**I need** `<function>`
**So that** `<benefit>`

### Details and Assumptions
* Add any assumptions, constraints, or background information here.
* Example: The account service is available and the database is running.

### Acceptance Criteria

```gherkin
Given <some context>
When <some action is carried out>
Then <a particular set of observable consequences should obtain>
```

---

## Example

**As a** customer service representative
**I need** to be able to read an account from the service
**So that** I can view the customer's details

### Details and Assumptions
* The account already exists in the database.
* The account ID is known.

### Acceptance Criteria

```gherkin
Given an account exists with ID 1
When I send a GET request to /accounts/1
Then I should receive a 200_OK response
And the response body should contain the account details
```
