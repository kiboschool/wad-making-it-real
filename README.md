# Making it real

This exercise will let you practice connecting to a SQLite database from Python, executing SQL queries, and handling the results of the query. You will also practice refactoring code to use a real database instead of mock data.

## Mock Data

Mock data is dummy or placeholder data that is used in place of real data when developing or testing an application. It is often used to simulate real data when the actual data is not yet available, or when the real data is not appropriate for the current stage of development or testing.

Mock data is useful in several ways when building an application:

- Prototyping: When prototyping an application, developers often don't have real data to work with. Mock data allows developers to quickly create a functioning prototype, which can be used to get feedback from stakeholders or to test the usability of the application.
- Simulation: Mock data can be used to simulate different scenarios or edge cases that may not be possible or practical to test with real data. This can include things like testing how the application behaves under high load or when dealing with large amounts of data.
- Development speed: Using mock data can speed up the development process since developers do not need to wait for real data or do not need to go through the process of cleaning data.

In this exercise, you'll take an application that uses mock data and convert it
to one that relies actual database queries.

## Instructions

1. Begin by creating a Python script that uses mock data to display a list of products. The script should define a list of dictionaries, where each dictionary represents a product and contains the following keys: id, name, price, and quantity.
2. Next, create a SQLite database named products.db and create a table called products with the following columns: id, name, price, and quantity.
3. Populate the products table with the mock data from the Python script.
4. Modify the Python script to connect to the products.db database and retrieve the list of products from the products table. Use the sqlite3 module to connect to the database and execute a SELECT query to retrieve the data.
5. Update the script to display the products from the database, instead of the mock data.
6. Test the script to ensure that it correctly retrieves and displays the data from the products table in the database.
7. Next, add functionality to the script such as adding new products, updating product details and deleting products from the database.
8. Finally, write test cases to check the correctness of the application using the unittest library.

