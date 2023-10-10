# Contributing

- [Contributing](#contributing)
  - [Contributing Code](#contributing-code)

---

## Contributing Code

_Note: Theses instructions are for linux base systems. Please, adapt them if you are using another operating system._

1. Clone the repository to your local disk

   ```sh
   git clone https://github.com/colosseum-project/app-bisellium.git
   cd app-bisellium
   ```

2. Create then activate a virtual environment

   ```sh
   python3 -m venv venv
   . venv/bin/activate
   ```

3. Install the requirements and the project

   ```sh
   pip3 install -r requirements-dev.txt
   pip3 install -e .
   ```

4. Set environment

   ```sh
   export FLASK_APP=bisellium
   export FLASK_ENV=development
   export PROMETHEUS_MULTIPROC_DIR=./.metrics
   export LUDUS_ENDPOINT=http://localhost:8081
   export DEBUG_METRICS=1 # only for debugging Prometheus metrics (WARNING: high disk usage)
   ```

   _Preferably, as `.env` files are supported, you can create such a file to set the environment variables._

5. Run the application

   ```sh
   flask run
   ```
