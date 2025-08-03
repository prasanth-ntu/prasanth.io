---
tags:
  - softwareengineering
---
A REST API (Representational State Transfer Application Programming Interface) is an architectural style that defines a set of rules and constraints for creating web services. Think of it as a translator that allows different software applications to communicate with each other over the internet, typically using the HTTP protocol. It's a common way for client applications (like a mobile app or a website) to request and manipulate data from a server.

# HTTP Methods
## GET
- **Purpose**: To retrieve or "get" data from a server.
- **Data Location**: Data is appended to the URL as query parameters (e.g., `www.example.com/users?id=123`).
- **Characteristics**:
	- **Idempotent**: Making the same GET request multiple times produces the same result.
	- **Visible Data**: Since data is in the URL, it's visible in browser history and server logs, making it insecure for sensitive information like passwords.
	- **Limited Length**: The length of a URL is limited, so you can only send a small amount of data.
	- Can be bookmarked and cached.

## POST
- **Purpose**: To send data to a server to create a new resource (e.g., creating a new user account).
- **Data Location**: Data is sent in the body of the HTTP request, hidden from the URL.
- **Characteristics**:
    - **Not Idempotent**: Making the same POST request multiple times will create multiple new resources.
    - **Secure Data**: Data is not exposed in the URL, making it suitable for sensitive or large amounts of data.
    - **No Length Limit**: Can send much more data than a GET request.
    - Cannot be bookmarked or cached.

## PUT
Replaces an existing resource entirely with the data provided. If the resource doesn't exist, it can create it. It is idempotent.

## PATCH
Applies a partial modification to an existing resource. For example, updating only a user's email address without changing their other details.

## DELETE
Removes a specific resource from the server.

## HEAD
Similar to a GET request, but it only returns the response headers and not the actual data (the body). It's useful for quickly checking a resource's metadata, like its size or last modified date, without downloading the content.

## OPTIONS
Describes the communication options (i.e., which HTTP methods are allowed) for the target resource