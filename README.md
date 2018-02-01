A onetime secret sharing app.

Features

  - expiration based on number of views
  - expiration based on date
  - optionally require login to view
  - encrypted secret field
  - QR Code view

Install:

    docker-compose up --build
    docker-compose run app manage migrate
    docker-compose run app manage createsuperuser
