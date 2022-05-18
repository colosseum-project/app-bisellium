from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

PROMETHEUS_MULTIPROC_DIR = env.str("PROMETHEUS_MULTIPROC_DIR", default="./.metrics")
LUDUS_URL = env.str("LUDUS_URL", default="http://localhost:8081")
ARENA_URL = env.str("ARENA_URL", default="http://localhost:8082")
