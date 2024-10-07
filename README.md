# AgentQL Python SDK Docker Example

This project demonstrates how to run the [AgentQL](https://www.agentql.com/) Python SDK in a Docker container, using MongoDB for storing basic inputs and outputs. It showcases the power of AgentQL for painless data extraction and web automation.

## Table of Contents

1. [Project Overview](#project-overview)
2. [What is AgentQL?](#what-is-agentql)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Getting Started](#getting-started)
6. [Services](#services)
7. [Environment Variables](#environment-variables)
8. [API Endpoints](#api-endpoints)
9. [Additional Resources](#additional-resources)

## Project Overview

- **Main Application**: Runs the AgentQL Python SDK
- **Database**: MongoDB for storing inputs and outputs
- **Admin Interface**: MongoDB Express for database management

## What is AgentQL?

AgentQL is an AI-powered tool that allows you to extract data and automate web interactions using natural language queries instead of fragile XPath or DOM selectors. It's designed to be robust, adapting to changes in website structures automatically.

Key features of AgentQL include:

- Semantic selectors
- Natural language queries
- Controlled output
- Deterministic results

## Project Structure

The project uses Docker Compose to orchestrate the following services:

1. `app`: The main application service running AgentQL Python SDK
2. `mongodb`: The MongoDB database service
3. `mongo-express`: A web-based MongoDB admin interface

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Set up environment variables:

   ```
   cp .env.example .env
   ```

   Open the `.env` file and update the `AGENTQL_API_KEY` with your own API key:

   ```
   AGENTQL_API_KEY=your_actual_api_key_here
   ```

3. Build and start the services:

   ```
   docker-compose up
   ```

4. Access the application at `http://localhost:8000`

5. Access the MongoDB Express admin interface at `http://localhost:8081`
   - Username: admin
   - Password: pass

## Services

### App

- Built from the Dockerfile in the project root
- Runs the AgentQL Python SDK
- Source code is mounted from `./app` directory
- Runs on port 8000

### MongoDB

- Uses the latest MongoDB image
- Stores basic inputs and outputs from the AgentQL SDK
- Data is persisted in a named volume `mongodb_data`
- Runs on port 27017

### Mongo Express

- Web-based MongoDB admin interface
- Runs on port 8081
- Default login credentials:
  - Username: `admin`
  - Password: `pass`

## Environment Variables

The project uses a `.env` file for configuration. Make sure the following variables are set up:

- `AGENTQL_API_KEY`: Your AgentQL API key
- `MONGODB_URI`: Set automatically in the docker-compose file
- Add any additional AgentQL SDK specific environment variables

**Remember to never commit your `.env` file with sensitive information to version control.**

## API Endpoints

### /ingest

- Method: POST
- Description: Ingests a URL for processing
- Request body:

```
curl --location 'localhost:8000/ingest' \
--header 'Content-Type: application/json' \
--data '{
    "url": "https://centrifuge.mirror.xyz/wQGnnIo89V0C1jIWvUcGGEQixrou5BjcZijjxQPNBlo?utm_source=rwa.xyz&utm_medium=referral&utm_campaign=news_aggregator"
}'
```

`/process` endpoint:

```
curl --location 'localhost:8000/process'
```

## Additional Resources

- [AgentQL Documentation](https://docs.agentql.com/)
- [AgentQL Python SDK](https://github.com/agentql/agentql-python)

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
