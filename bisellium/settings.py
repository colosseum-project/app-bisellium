from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

PROMETHEUS_MULTIPROC_DIR = env.str("PROMETHEUS_MULTIPROC_DIR", default="./.metrics")
LUDUS_ENDPOINT = env.str("LUDUS_ENDPOINT ", default="http://localhost:8081")
ARENA_ENDPOINT = env.str("ARENA_ENDPOINT ", default="http://localhost:8082")
