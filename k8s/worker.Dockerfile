FROM rayproject/ray:2.41.0-py39-cpu-aarch64

RUN pip install --no-cache-dir tensorflow-aarch64 numpy Pillow python-multipart
