# Grading

### Bare Minimum earns you 50%
- [x] Readme checkmarks filled out accurately (10 pts)
- [x] The user can see all the products the store sells; minimum of 10 products. (10 pts)
- [x] The user can see all the products in a specific category; minimum of 3 categories. (10 pts)
- [x] Database schema and scripts to create and populate the tables. (10 pts)
  - This must be kept in the `store_schema.sql` file.
- [x] Minimal web interface: web page does not look professional, minimal styling, no form checks. (10 pts)


### Base level takes you to 85% 
- [x] The user can search for a specific item by name. (7 pts)
- [x] The user can login, but not create a new account. (7 pts)
  - Users who are not in the DB can't login.
  - Must include a sample user named `testuser` with password `testpass`
- [x] The logged in user can view, add to, edit, check out or delete their cart. (7 pts)
  - The cart should be stored as a session variable.
- [x] The database is updated when a user checks out. (7 pts)
- [x] The store doesn't let a user buy negative amounts or more than is in the inventory. (7 pts)

### Medium level takes you to 95%
- [x] A new user can sign up. (3 pts)
- [x] A logged in user can see his/her previous order history. (2 pts)
- [x] The front end is user friendly: website is easy and intuitive to navigate, no server error messages are presented to to user (if an error occurs, give a user friendly message). (3 pts)
- [x] Website style: products have pictures. (2 pts)

### Prime level takes you to 100%
- [ ] Implement client-side validation for input forms (e.g. quantity added to cart can't be negative) using Javascript. (2 pt)
- [x] The logged in user can sort its orders by date. (1 pt)
- [x] The logged in user can search for a product in his/her past orders. (1 pt)
- [x] Website inspires a professional look: has logo, product descriptions, etc. (1 pt)

TOTAL: 98 / 100