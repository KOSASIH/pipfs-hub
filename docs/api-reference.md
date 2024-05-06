# API Reference

PiPFS Hub provides a REST API that you can use to interact with the platform programmatically. The API is based on the JSON:API specification and uses HTTP requests to perform CRUD operations on resources.

## API Endpoints

The following API endpoints are available:

- `/api/files`: Manage files.
- `/api/folders`: Manage folders.
- `/api/users`: Manage users.

## API Authentication

To authenticate with the PiPFS Hub API, you need to include an API key in the `Authorization` header of your requests. You can obtain an API key by registering for a PiPFS Hub account and creating an API key in the dashboard.

## API Response Format

The PiPFS Hub API returns responses in JSON format. Each response includes a `data` object that contains the requested resource, and a `meta` object that contains metadata about the response.

## API Errors

If an error occurs while processing a request, the PiPFS Hub API returns an HTTP status code in the 4xx or 5xx range, along with a JSON object that contains an error message.

## API Examples

Here are some examples of how to use the PiPFS Hub API:

- **Upload a file**: To upload a file, send a `POST` request to the `/api/files` endpoint with the file in the request body.
- **List files**: To list all the files, send a `GET` request to the `/api/files` endpoint.
- **Get a file**: To get a file, send a `GET` request to the `/api/files/{id}` endpoint, where `{id}` is the ID of the file.
- **Update a file**: To update a file, send a `PATCH` request to the `/api/files/{id}` endpoint with the updated file in the request body.
- **Delete a file**: To delete a file, send a `DELETE` request to the `/api/files/{id}` endpoint.
