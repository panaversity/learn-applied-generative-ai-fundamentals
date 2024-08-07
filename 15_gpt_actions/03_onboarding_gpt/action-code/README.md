# Onboarding Service Action

This project sets up an onboarding GPT Action with a PostgreSQL database, exposed via a Cloudflare tunnel. It uses Docker Compose for easy setup and management. This is the bare base template for creating GPT Actions.

## Feat Features:

- **Automatic Tunnel Setup**: On running `docker compose up`, the Cloudflare tunnel starts automatically.
- **Integration with PostgreSQL and FastAPI Onboarding Microservice**: A PostgreSQL database is set up, accessed by onboarding microservice.
- **Repository Design Pattern for Database Crud Operations using CRUDBase class as a generic repository**.
- **Router Pattern and combines it with Factory Pattern elements to dynamically create API routes in a FastAPI application.**

## Prerequisites

- Docker
- Docker Compose

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone ...
   cd onboarding-action
   ```

2. **Add Environment Variables**

In onboarding service rename .env.example to .env

Get Stripe Secret and setup a WebHook.

3. **Start the Services**

Before setting up WebHook 

Run the following command to start all services, including the Cloudflare tunnel:

`docker-compose up --build`

Get the CloudFlare URL and then setup webhook on Stripe with following. You will need the WebHook Secret as well so copy and add to .env variable.

In WebHook you will have to pass the following
- endpoint: https://domain.trycloudflare.com/api/v1/enrollments/webhook
- events: checkout

Pro Tip: After update any env variable you can change main.py lifespan function print statement to restart server and load env vars.

4. **Get CloudFlare Tunnel Url**

The onboarding service is accessible at:

http://localhost:9010/

and In Logs we will have the CloudFlare URL. It shall be something like:

https://walt-roll-protecting-silly.trycloudflare.com

```
--------------------------------+
cloudflared-1           | 2024-06-16T17:55:13Z INF |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
cloudflared-1           | 2024-06-16T17:55:13Z INF |  https://walt-roll-protecting-silly.trycloudflare.com                                      |
cloudflared-1           | 2024-06-16T17:55:13Z INF +--------------------------------------------------------------------------------------------+
```

5. **Access PGAdmin In Browser**

Open localhost:8010 in browser

      - PGADMIN_DEFAULT_EMAIL=mjunaid@gmail.com
      - PGADMIN_DEFAULT_PASSWORD=SuperSecret

Now In Servers the DB is already configured - it's password is ``


5. **Create Custom GPT**

Refer to readme.md in onboard-action to to create custom gpt!