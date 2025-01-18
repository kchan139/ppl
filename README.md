# Principles of Programming Languages - HCMUT - HK242

#### Build the environment
```bash
docker-compose build
```

#### Start an interactive shell in the container
```bash
docker-compose run --rm minigo
```

#### Once inside the container, you can:
```bash
cd src
python run.py gen                 # Generate ANTLR files
python run.py test LexerSuite     # Run tests
```