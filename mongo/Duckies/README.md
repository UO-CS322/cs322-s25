# Duckies App

A Flask app for managing a collection of rubber duckies.

* MongoDB setup: [Mongodb.md](./Mongodb.md)
* Docker setup: [DockerCompose.md](./DockerCompose.md)

## Files
```
├── app.py : Main Flask app - handles web requests and talks to the database
├── requirements.txt : Python packages needed to run the app
├── templates/index.html : The webpage you see in your browser
└── tests/ : Code that checks if everything works correctly
```

## What It Does
- Store duck data in MongoDB (like a digital filing cabinet)
- Search ducks by name (find your favorite duck)
- Web interface for adding and finding ducks (no coding needed)

## Run Locally
1. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Start MongoDB (see [Mongodb.md](./Mongodb.md)) - this is where your duck data lives
3. Run the app:
   ```bash
   python app.py
   ```
4. Open http://localhost:5005

## Run Tests
```bash
pytest tests
```
This checks if everything works as expected in the Flask app (`tests/test_flask.py`) and the Web interface (`tests/test_selenium.py`).

A successful run looks like this:
```
...
collected 7 items                                                                    

 tests/test_flask.py ✓✓✓✓✓                                              71% ███████▎  
 tests/test_selenium.py ✓✓                                             100% ██████████
```

## Run with Docker
```bash
docker-compose up
```
This starts both the app and database in containers (like separate computers). Example output:
```
[+] Building 10.1s (11/11) FINISHED                                                      docker:desktop-linux
 => [app internal] load build definition from Dockerfile                                                 0.0s
 => => transferring dockerfile: 486B                                                                     0.0s
 => [app internal] load metadata for docker.io/library/python:3.10-slim                                  1.0s
 => [app internal] load .dockerignore                                                                    0.0s
 => => transferring context: 2B                                                                          0.0s
 => [app 1/5] FROM docker.io/library/python:3.10-slim@sha256:e1013c40c02a7875ae30c78c69b68ea7bee31713e8  0.1s
 => => resolve docker.io/library/python:3.10-slim@sha256:e1013c40c02a7875ae30c78c69b68ea7bee31713e8ac1c  0.1s
 => [app internal] load build context                                                                    0.8s
 => => transferring context: 434.98kB                                                                    0.8s
 => CACHED [app 2/5] WORKDIR /app                                                                        0.0s
 => CACHED [app 3/5] COPY requirements.txt .                                                             0.0s
 => CACHED [app 4/5] RUN pip install --no-cache-dir -r requirements.txt                                  0.0s
 => [app 5/5] COPY . .                                                                                   0.8s
 => [app] exporting to image                                                                             7.0s
 => => exporting layers                                                                                  4.9s
 => => exporting manifest sha256:cc3c4b7dabb31eafda72fc33e889251ad1704e8e0f4d515fb076443767008ecd        0.0s
 => => exporting config sha256:a59e0f3cf25b9d089ad9e601d307e56fd42ad0654a79292ed40d4561727c4919          0.0s
 => => exporting attestation manifest sha256:36a2e930024f49d0dbd908b9fdfd8150d1c9535a6d38e47cc9410d36c2  0.0s
 => => exporting manifest list sha256:8017c4dfadbf58ce05df1bdb7784ac53932e5a21e056dd656ff0945879225291   0.0s
 => => naming to docker.io/library/duckies-app:latest                                                    0.0s
 => => unpacking to docker.io/library/duckies-app:latest                                                 2.0s
 => [app] resolving provenance for metadata file                                                         0.0s
[+] Running 4/4
 ✔ app                          Built                                                                    0.0s 
 ✔ Network duckies_default      Created                                                                  0.2s 
 ✔ Container duckies-mongodb-1  Created                                                                  0.4s 
 ✔ Container duckies-app-1      Created                                                                  0.4s 
Attaching to app-1, mongodb-1
...
app-1      |  * Serving Flask app 'app'
app-1      |  * Debug mode: on
mongodb-1  | {"t":{"$date":"2025-05-13T03:19:07.288+00:00"},"s":"I",  "c":"WTRECOV",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":{"ts_sec":1747106347,"ts_usec":288441,"thread":"1:0x7f8352743680","session_name":"txn-recover","category":"WT_VERB_RECOVERY_PROGRESS","category_id":34,"verbose_level":"DEBUG_1","verbose_level_id":1,"msg":"Recovering log 2 through 2"}}}
app-1      | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
app-1      |  * Running on all addresses (0.0.0.0)
app-1      |  * Running on http://127.0.0.1:5005
app-1      |  * Running on http://172.22.0.3:5005
app-1      | Press CTRL+C to quit
..... lots and lots of mongodb logs ....
```

